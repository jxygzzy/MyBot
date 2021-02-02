

from services.common import get_joke_data


async def get_joke() -> str:
    url = 'https://api.muxiaoguo.cn/api/xiaohua'
    return await get_joke_data(url)
