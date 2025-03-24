
import redis
r = redis.Redis('localhost',decode_responses=True)

token = '7962314645:AAFECynKGWblzc5eKq81iuIlLEZehN3eujo'
Dev_Zaid = token.split(':')[0]
sudo_id = 125205235
botUsername = 'Leioobot'
from kvsqlite.sync import Client as DB
ytdb = DB('ytdb.sqlite')
sounddb = DB('sounddb.sqlite')
wsdb = DB('wsdb.sqlite')