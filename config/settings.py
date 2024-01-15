from pathlib import Path
from configparser import ConfigParser

CONFIG_DIR = Path(__file__).resolve().parent

config = ConfigParser()
config.read(CONFIG_DIR / 'config.ini')

NAME = config['pyrogram']['name']
API_ID = config['pyrogram']['api_id']
API_HASH = config['pyrogram']['api_hash']

PROXY = {
    "scheme": config['proxy']['scheme'],
    "hostname": config['proxy']['hostname'],
    "port": int(config['proxy']['port']),
}
