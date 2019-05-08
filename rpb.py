import discord
from discord.ext import commands
from discord.ext.commands import Bot
from discord.voice_client import VoiceClient
from discord import VoiceChannel
import asyncio
import random

token = 'NTc1Mzk0MTQ1NjE1NzQwOTY4.XNHUdg.RQZphZ6q--Roevu-Y7FNVD9A12Q'
client = commands.Bot(command_prefix="!")

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))


@client.command()
async def join(ctx):
    # recupera quem enviou a mensagem
    author = ctx.message.author

    # recupera qual canal o membro está
    try:
        channel = author.voice.channel
    except:
        print('primeiro conecte-se a um servidor de voz')
        return

    # se connecta ao canal do membro
    try:
        vc = await channel.connect()
    except:
        print('já conectado a um servidor')
        return


@client.command()
async def leave(ctx):
    # recupera quem enviou a mensagem
    author = ctx.message.author

    # recupera qual cliente de voz o membro está
    vc = author.guild.voice_client

    # disconecta o bot desse cliente
    try:
        await vc.disconnect()
    except:
        print('não conectado a nenhum servidor')


@client.command()
async def d(ctx, num_dado, bonus='0'):

    # verifica se é um bonus ou uma penalidade
    if int(bonus) >= 0:
        type = "Bonus"
    else:
        type = "Penalidade"

    # exibe uma mensagem do dado que será rolado
    # caso seja apenas um dado permite somar o bonus
    await ctx.channel.send('Rolando 1 D' + num_dado + ' com ' + type + ' ' + bonus)

    rand = random.randint(1, int(num_dado))
    num_final = rand + int(bonus)

    # exibe qual o valor do dado rolado e realiza a soma com o bonus ou penalidade
    await ctx.channel.send('O dado rolou '+str(rand)+' somado a(ao) '+type+' '+str(num_final))


@client.command()
async def md(ctx, num_dado, num_dados=str(1)):

    # caso seja mais de um dados ignora o bonus
    if int(num_dados) >= 1:
        await ctx.channel.send('Rolando ' + str(num_dados) + ' D' + num_dado)

    valores = []

    # caso seja mais de um dado, exibe os valores dos dados

    for i in range(int(num_dados)):
        valores.append(random.randint(1, int(num_dado)))
    response = 'Os dados rolaram os valores: '
    valores.sort()
    for x in valores:
        response += str(x) + " "
    await ctx.channel.send(response)


client.run(token)

