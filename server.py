import sys
sys.path.append('..')
import discord
import requests
import json
from discord.ext import commands
from secrets_file import api_key, server_id

class ServerCog(commands.Cog, name='Server'):
    base_url = f'https://gamocosm.com/servers/{server_id}/api/{api_key}/'

    def __init__(self, bot):
        self.bot = bot

    @commands.group(invoke_without_command=True)
    async def server(self, ctx):
        await ctx.send(
            '''Available commands:
        server on
        server off
        minecraft on
        minecraft off''')

    @server.command(pass_content=True, name='on')
    async def server_on(self, ctx):
        await ctx.send("Server turning on...")
        response = requests.post(self.base_url + 'start')
        await ctx.send("Server starting, wait 2 minutes" if response.ok else "Error starting server")

    @server.command(name='status')
    async def server_status(self, ctx):
        response = requests.get(self.base_url + 'status')
        content = json.loads(response.text)
        print(content)
        await ctx.send("Server online" if content['server'] else "Server offline")
        await ctx.send("Minecraft online" if content['minecraft'] else "Minecraft offline")
        await ctx.send(f"Server status: {content['status']}" if content['status'] != None else "Server status: active")
        await ctx.send(f"Server IP: {content['domain']}")

    @server.command(pass_content=True, name='off')
    async def server_off(self, ctx):
        await ctx.send("Server turning off...")
        response = requests.post(self.base_url + 'stop')
        await ctx.send("Server offline" if response.ok else "Error stopping server")

    @commands.group(invoke_without_command=True)
    async def minecraft(self, ctx):
        await ctx.send('''Available commands
                server minecraft on
                server minecraft off''')

    @minecraft.command(pass_content=True, name='on')
    async def minecraft_on(self, ctx):
        await ctx.send("Minecraft turning on...")
        response = requests.post(self.base_url + 'resume')
        await ctx.send("Minecraft server online" if response.ok else "Error starting server")

    @minecraft.command(pass_content=True,  name='off')
    async def minecraft_off(self, ctx):
        await ctx.send("Minecraft turning off...")
        response = requests.post(self.base_url + 'pause')
        await ctx.send("Minecraft server offline" if response.ok else "Error stopping server")


def setup(bot):
    bot.add_cog(ServerCog(bot))
    print("Server cog loaded")
