__plugin_name__ = '每日壁纸'
__plugin_usage__ = r"""
必应每日壁纸
发送：壁纸
"""

from io import BytesIO
from PIL import Image
from nonebot import on_command, CommandSession, on_natural_language, NLPSession, IntentCommand
from aiocqhttp import MessageSegment

from Bot.services.dailyWallpaper import get_wallpaper


@on_command('wallpaper', aliases=('每日壁纸','壁纸'))
async def dailyWallpaper(session: CommandSession):

    img =Image.open(BytesIO(await get_wallpaper()))
    img.save('onebot/img/daily.jpg')
    seq = MessageSegment.image('img/daily.jpg')
    await session.send(seq)


@on_natural_language(keywords={'壁纸'})
async def _(session: NLPSession):
    # 返回意图命令，前两个参数必填，分别表示置信度和意图命令名
    return IntentCommand(90.0, 'wallpaper')