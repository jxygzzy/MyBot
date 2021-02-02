from services.common import get_caihong_data


async def get_caihong() -> []:
    url = 'https://api.muxiaoguo.cn/api/caihongpi'
    return await get_caihong_data(url)