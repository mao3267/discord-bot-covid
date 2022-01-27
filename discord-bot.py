import discord
import random
from bs4 import BeautifulSoup
from discord.utils import get
import requests

client = discord.Client()


@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))
    

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    
    hello = {'嘿嘿','co co','CO CO'}
    keywords = {'機器人','哭阿'}
    kaku  = {'阿鵝','肥鵝'}
    dian = {'電'}
    what ={"這是什麼",'這啥','這什麼鬼','這三小'}
    buy ={"買嗎"}
    baby = {'嬰兒','阿姆姆','瑞斯開剁'}
    alan = {'生日快樂'}

    response = '你已被 relaxing234 永久禁言'
    response3 = '有人找你'
    response4 = '我也想知道'
    response5 = ['嗨嗨你好，','找我嗎，','撒挖低咖~~']
    response6 = '關於這種問題我一律建議買爆'

    for keyword in keywords:
        if keyword in message.content:
            await message.channel.send(response)
    
    if "電" in message.content:
        emoji = '⚡'
        await message.add_reaction(emoji)
    
    if "我很爛" or "我好爛" in message.content:
        emoji = '😠'
        await message.add_reaction(emoji)

    for word in kaku:
        if word in message.content:
            await message.channel.send('<@638740556100665375>'+ response3)
  
    for word in what:
        if word in message.content:
            await message.channel.send(response4 + message.author.mention )

    for word in hello:
        if word in message.content:
            await message.channel.send(response5[random.randint(0,2)] + message.author.mention )

    for word in buy:
        if word in message.content:
            await message.channel.send(response6 )

    for word in alan:
        if word in message.content:
            await message.channel.send('<@528572870750633987>' + '生日快樂' )

    if 'yee' in message.content:
        await message.channel.send(file = discord.File('yee.jpg'))
    
    if '!covid' == message.content:
        url = "https://covid-19.nchc.org.tw/"

        html = requests.get(url,verify=False) #,verify=False

        soup = BeautifulSoup(html.text,"html.parser")
        local_covid = soup.select("div.col-lg-3.col-sm-6.col-6.text-center.my-5 p.text-muted span.country_confirmed_percent")
        total_covid = soup.select("div.col-lg-3.col-sm-6.col-6.text-center.my-5 h1.country_recovered.mb-1.text-info")
        print(local_covid[1].text)
        
        print("總新增病例"+total_covid[0].text)
        
        await message.channel.send("總新增病例"+total_covid[0].text+'\n'+local_covid[1].text)

