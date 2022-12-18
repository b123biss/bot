from nextcord.ext import commands
import nextcord
import datetime
import sqlite3
import pytz
import random as r
import os
from nextcord import SlashOption, ChannelType
from nextcord.abc import GuildChannel

intents = nextcord.Intents.default()
intents.members = True
intents.messages = True
client = commands.Bot(command_prefix='.', intents=intents)

token = 'OTY1MTk3NDYwMDc3MTU4NDAw.GbW17B.cm8f_rj1k_bpBXDkybGav9tTppZlAXoPPBofXI'
@client.event
async def on_ready():
  i = datetime.datetime.now()
  print(f"{client.user.name}봇은 준비가 완료 되었습니다.")
  print(f"[!] 참가 중인 서버 : {len(client.guilds)}개의 서버에 참여 중")
  print(f"[!] 이용자 수 : {len(client.users)}명과 함께하는 중")
  guild_list = client.guilds
  for i in guild_list:
    print("서버 ID: {} / 서버 이름: {} / 멤버 수: {}".format(i.id, i.name,
                                                    i.member_count))

@client.slash_command(name="문상", description="문상을 제조합니다.")
async def hell(inter: nextcord.Interaction) -> None:
  a = r.randint(0, 9)
  b = r.randint(0, 9)
  c = r.randint(0, 9)
  d = r.randint(0, 9)
  one = f'{a}{b}{c}{d}'
  a = r.randint(0, 9)
  b = r.randint(0, 9)
  c = r.randint(0, 9)
  d = r.randint(0, 9)
  two = f'{a}{b}{c}{d}'
  a = r.randint(0, 9)
  b = r.randint(0, 9)
  c = r.randint(0, 9)
  d = r.randint(0, 9)
  three = f'{a}{b}{c}{d}'
  a = r.randint(0, 9)
  b = r.randint(0, 9)
  c = r.randint(0, 9)
  d = r.randint(0, 9)
  four = f'{a}{b}{c}{d}'

  five = f'{one} {two} {three} {four}'
  return await inter.response.send_message(f'> **{five}**')
  print(f'{inter.user.id}님이 문상을 제조하였습니다.')
    
@client.slash_command(name="깊카", description="깊카를 제조합니다.")
async def hel(inter: nextcord.Interaction) -> None:
  b=[]
  amm = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','1','2','3','4','5','6','7','8','9','0']
  for i in range(4):
    a=r.sample(amm, 4)
    aa=''.join(a)
    b.append(aa)
  c=' '.join(b)
  return await inter.response.send_message(f'> **{c}**')
  print(f'{inter.user.id}님이 깊카를 제조하였습니다.')

@client.slash_command(name="니트로", description="니트로를 제조합니다.")
async def he(inter: nextcord.Interaction) -> None:
  amm = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','1','2','3','4','5','6','7','8','9','0']
  a=r.sample(amm, 24)
  b=''.join(a)
  return await inter.response.send_message(f'> **https://discord.gift/{b}**')
  print(f'{inter.user.id}님이 니트로를 제조하였습니다.')

@client.slash_command(name='초대코드', description="초대코드를 불러옵니다.")
async def h(inter: nextcord.Interaction) -> None:
  return await inter.response.send_message('> **https://discord.com/api/oauth2/authorize?client_id=965197460077158400&permissions=8&scope=bot**')
  print(f'{inter.user.id}님이 초대코드를 불러왔습니다.')

client.run(os.environ['token'])