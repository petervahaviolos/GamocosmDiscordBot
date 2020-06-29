import sys
import discord
import requests
from discord.ext import commands
from bs4 import BeautifulSoup

login_url = 'https://gamocosm.com/users/sign_in'
dashboard_url = 'https://gamocosm.com/servers/b9c653c3-68d8-45ac-bd12-09b6176cb0a3'
username = 'vahaviolospeter@gmail.com'
password = '8fLw85P46GvsTjVN'
session_requests = ""

class ServerCog(commands.Cog, name='Server'):
    def __init__(self, bot):
        global session_requests
        print('Creating session')
        session_requests = requests.session()
        print('Loading website')
        result = session_requests.get(login_url)
        print("Website loaded successfully" if result.ok else "Failed to load website")
        soup = BeautifulSoup(result.text, 'html.parser')
        auth_token = soup.find_all('meta')[3].attrs['content']
        print('Sending post request')
        result = session_requests.post(login_url, data={'user[email]' : username,
                                                        'user[password]' : password,
                                                        'authenticity_token' : auth_token}, headers= dict(referer=login_url))
        print("Logged in" if result.ok else "Failed to log in")
        result = session_requests.get(dashboard_url)
        print("Dashboard loaded" if result.ok else "Error loading dashboard")
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
        global session_requests
        result = session_requests.get(dashboard_url + '/start')
        await ctx.send("Server turning on...")

    @server.command(pass_content=True, name='off')
    async def server_off(self, ctx):
        global session_requests
        result = session_requests.get(dashboard_url + '/stop')
        await ctx.send("Server turning off...")

    @commands.group(invoke_without_command=True)
    async def minecraft(self, ctx):
        await ctx.send('''Available commands
                server minecraft on
                server minecraft off''')

    @minecraft.command(pass_content=True, name='on')
    async def minecraft_on(self, ctx):
        global session_requests
        result = session_requests.get(dashboard_url + '/resume')
        await ctx.send("Minecraft turning on...")

    @minecraft.command(pass_content=True,  name='off')
    async def minecraft_off(self, ctx):
        global session_requests
        result = session_requests.get(dashboard_url + '/pause')
        await ctx.send("Minecraft turning off...")


def setup(bot):
    bot.add_cog(ServerCog(bot))
    print("Server cog loaded")
