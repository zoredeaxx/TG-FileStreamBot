# This file is a part of TG-FileStreamBot
# Coding : Jyothis Jayanth [@EverythingSuckz]

from os import getenv, environ
from dotenv import load_dotenv

load_dotenv()

class Var(object):
    API_ID = int(getenv('API_ID', '7523379'))
    API_HASH = str(getenv('API_HASH', 'ce43762f206dc2a2eb115986fbe3b4a2'))
    BOT_TOKEN = str(getenv('BOT_TOKEN', '5255266526:AAEAtb5U2QYzln_s2qAbb9Lg657tfYzrfAk'))
    SLEEP_THRESHOLD = int(getenv('SLEEP_THRESHOLD', '60'))
    WORKERS = int(getenv('WORKERS', '6'))
    BIN_CHANNEL = int(getenv('BIN_CHANNEL', '-1001308033853'))     
    PORT = int(getenv('PORT', 8080))
    BIND_ADDRESS = str(getenv('WEB_SERVER_BIND_ADDRESS', '0.0.0.0'))
    PING_INTERVAL = int(getenv('PING_INTERVAL', '1200')) # 20 minutes
    HAS_SSL = getenv('HAS_SSL', False)
    HAS_SSL = True if str(HAS_SSL).lower() == 'true' else False
    NO_PORT = getenv('NO_PORT', False)
    NO_PORT = True if str(NO_PORT).lower() == 'true' else False
    if 'DYNO' in environ:
        ON_HEROKU = True
        APP_NAME = str(getenv('APP_NAME'))
    else:
        ON_HEROKU = False
    FQDN = str(getenv('FQDN', BIND_ADDRESS)) if not ON_HEROKU or getenv('FQDN') else APP_NAME + '.herokuapp.com'
    if ON_HEROKU:
        URL = f"https://{FQDN}/"     
    else:
        URL = f"https://streamz-zoredeaxx.cloud.okteto.net"
