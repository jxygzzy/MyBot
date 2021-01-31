from io import BytesIO

import httpx
from PIL import Image
from httpx import AsyncClient, HTTPError

from Bot.services.log import logger

UserAgent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36"


class ServiceException(Exception):
    'Base of exceptions thrown by the service side'

    def __init__(self, message: str) -> None:
        super().__init__(message)

    @property
    def message(self) -> str:
        return self.args[0]


async def fetch_text(uri: str) -> str:
    async with AsyncClient(headers={'User-Agent': UserAgent}) as client:
        try:
            res = await client.get(uri)
            res.raise_for_status()
        except HTTPError as e:
            logger.exception(e)
            raise ServiceException('API 服务目前不可用')
        return res.text


async def fetch_wall_url(url: str) -> str:
    async with httpx.AsyncClient() as client:
        try:
            resp = await client.get(url)
            resp.raise_for_status()
            result = resp.json()
        except HTTPError as e:
            logger.exception(e)
            raise ServiceException('获取图片地址失败')
        return result['images'][0]['url']


async def get_wall_content(url: str):
    async with httpx.AsyncClient(headers={'User-Agent': UserAgent}) as client:
        try:
            content_url = await fetch_wall_url(url)
            resp = await client.get("https://www.bing.com"+content_url)
        except HTTPError as e:
            logger.exception(e)
            raise ServiceException('获取图片失败')
        return resp.content

async def fetch_wikipedia(url: str) -> str:
    async with httpx.AsyncClient() as client:
        try:
            resp = await client.get(url)
            resp.raise_for_status()
            result = resp.json()
        except HTTPError as e:
            logger.exception(e)
            raise ServiceException('获取百科失败')
        return result['data']


async def get_wikipedia_text(url: str):
    async with httpx.AsyncClient(headers={'User-Agent': UserAgent}) as client:
        try:
            data = await fetch_wikipedia(url)
            res =[]
            if data['content']=='':
                msg = '==未找到该词条=='
                res.append(msg)
            else:
                msg = data['content']
                img = data['ImgUrl']
                res.append(msg)
                res.append(img)

        except HTTPError as e:
            logger.exception(e)
            raise ServiceException('获取整合百科失败')
        return res



async def fetch_set_data(url: str) -> str:
    async with httpx.AsyncClient(headers={
        "r18": "2",
        "size1200": "true",
        "user-agent": UserAgent
    }, proxies={"http": "https://www.pixiv.net"}) as client:
        try:
            resp = await client.get(url)
            result = resp.json()
            data = result['data'][0]
        except HTTPError as e:
            logger.exception(e)
            raise ServiceException('获取setu失败')
        return data


async def get_setu_data(url: str):
    async with httpx.AsyncClient(headers={
        "r18": "2",
        "size1200": "true",
        "user-agent": UserAgent
    },proxies={"http":"https://www.pixiv.net"}) as client:
        try:
            data = await fetch_set_data(url)
            msg="pid:"+str(data['pid'])+"\n"+"title:"+data['title']+"\n"\
                +"author:"+data['author']+"\n"+"url:"+data['url']+"\n"+\
                "tags:"+str(data['tags'])
            imgUrl=data['url']
            result=[]
            result.append(msg)
            result.append(imgUrl)
        except HTTPError as e:
            logger.exception(e)
            raise ServiceException('setu——msg整合失败')
        return result