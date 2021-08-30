import discord
import requests
import asyncio

#pegando as informacoes na api, atualmente para BNB - Binance coin
URL ='https://api.coingecko.com/api/v3/simple/price?ids=binancecoin&vs_currencies=usd&include_24hr_change=true'
r = requests.get(url=URL)
data = r.json()
valor=data['binancecoin']['usd']
porcentagem=data['binancecoin']['usd_24h_change']

#mero visual
if porcentagem>0:
  seta=u'\u2197'
else:
  seta=u'\u2198'

client = discord.Client()

@client.event
async def on_ready():
  print(f'You have logged in as {client}')
  channel = discord.utils.get(client.get_all_channels(),name='general')
  await client.change_presence(activity=discord.Game(name=f"${valor}     {seta}   {porcentagem:,.2f}% "))

async def trocarStatus():
  await client.wait_until_ready()
  while not client.is_closed():

    URL ='https://api.coingecko.com/api/v3/simple/price?ids=binancecoin&vs_currencies=usd&include_24hr_change=true'
    r = requests.get(url=URL)
    data = r.json()
    valor=data['binancecoin']['usd']
    porcentagem=data['binancecoin']['usd_24h_change']

    if porcentagem>0:
      seta=u'\u2197'
    else:
      seta=u'\u2198'
    
    await client.change_presence(activity=discord.Game(name=f"${valor}     {seta}  {porcentagem:,.2f}% "))
    #aqui pode trocar o tempo de atualizacao do bot
    await asyncio.sleep(30)
client.loop.create_task(trocarStatus())

#aqui é inserido o token do seu bot de discord
BOT_TOKEN = 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'
client.run(BOT_TOKEN)
