# -*- coding: gbk -*-
from 地图研究 import getMap
import qq
from config import appid, token
import logging

logging.basicConfig(level=logging.DEBUG)

client = qq.Client()

@client.event
async def on_message(message: qq.Message):
    print(message.content)
    if "BO1地图" in message.content :
        mapbo1 = getMap(1,[])
        mapBO1 = str(mapbo1).replace('[','').replace(']','').replace("'","").replace("'","")
        await message.reply(mapBO1)
    if "BO3地图" in message.content :
        mapbo3 = getMap(3,[])
        mapBO3 = str(mapbo3).replace('[', '').replace(']', '').replace("'", "").replace("'", "")
        await message.reply(mapBO3)
    if "BO5地图" in message.content :
        mapbo5 = getMap(5,[])
        mapBO5 = str(mapbo5).replace('[', '').replace(']', '').replace("'", "").replace("'", "")
        await message.reply(mapBO5)
@client.event
async def on_ready():
    print("使用机器人登录成功。")


if __name__ == '__main__':
    try:
        client.run(token=f"{appid}.{token}")
    except Exception as e:
        logging.exception("发生错误：")
