from fastapi import APIRouter
from fastapi.responses import RedirectResponse

redirect_router = APIRouter()


@redirect_router.get('/')
async def redirect_to_webapp():
    return RedirectResponse(url='/index.html')


@redirect_router.get('/bot/{bot_args:path}')
async def redirect_to_webapp_with_bot_args(bot_args: str, url: str = ''):
    secure, botname = bot_args.split('/')
    secure = 'false' if secure == 'false' else 'true'
    return RedirectResponse(url=f'/index.html?botname={botname}&secure={secure}&url={url}')
