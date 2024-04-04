# -*- coding: gbk -*-
import qq
from config import appid, token
import logging

logging.basicConfig(level=logging.DEBUG)

client = qq.Client()

@client.event
async def on_message(message: qq.Message):
    print(message.content)
    if "!i" in message.content :
        await message.reply('44444')
    if "!b" in message.content :
        await message.reply('5555')

@client.event
async def on_ready():
    print("使用机器人登录成功。")


if __name__ == '__main__':
    try:
        client.run(token=f"{appid}.{token}")
    except Exception as e:
        logging.exception("发生错误：")
