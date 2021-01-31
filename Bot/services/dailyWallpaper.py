from aiocache import cached

from Bot.services.common import get_wall_content


@cached(ttl=60)
async def get_wallpaper() :
    url = 'http://www.bing.com/HPImageArchive.aspx?format=js&idx=0&n=1&mkt=en-US'

    return await get_wall_content(url)