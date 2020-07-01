import sys, os, inspect
import discord
import requests
import json
import confuse
import logging
current_dir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parent_dir = os.path.dirname(current_dir)
sys.path.insert(0, parent_dir)
from server import Server
from discord.ext import commands

class ServerCog(commands.Cog, name='Server'):
    def __init__(self, bot):
        self.config = confuse.Configuration("MinecraftDiscordBot", __name__)
        self.server = Server(self.config['serverId'], self.config['apiKey'])
        self.bot = bot

    @commands.group(invoke_without_command=True, name='server')
    async def server(self, ctx):
        await ctx.send(
            '''Available commands:
        server on
        server off
        server status
        server send [command]
        minecraft on
        minecraft off''')

    @server.command(pass_content=True, aliases=['start', 'on'])
    async def server_start(self, ctx):
        """Start the digitalocean server and minecraft server"""
        await ctx.send("Server starting...")
        response = self.server.server_start()
        logging.info(f"[server_start] Response: {response}")
        await ctx.send("Server started successfully" if response.ok else "Error starting server")

    @server.command(pass_content=True, aliases=['stop', 'off'])
    async def server_stop(self, ctx):
        """Stop the digitalocean server and minecraft server"""
        await ctx.send("Server stopping...")
        response = self.server.server_stop()
        logging.info(f"[server_stop] Response: {response}")
        await ctx.send("Server stopped successfully" if response.ok else "Error stopping server")

    @server.command(pass_content=True, aliases=['reboot', 'restart'])
    async def server_reboot(self, ctx):
        """Restart the digitalocean server and minecraft server"""
        await ctx.send("Server restarting...")
        response = self.server.server_reboot()
        logging.info(f"[server_reboot] Response: {response}")
        await ctx.send("Server rebooted successfully" if response.ok else "Error rebooting server")

    @server.command(aliases=['status', 'state'])
    async def server_status(self, ctx):
        """Show the status of the server"""
        await ctx.send(f'''
        Server: {self.server.server_online()}
        Minecraft: {self.server.minecraft_online()}
        State: {self.server.pending_state()}
        IP: {self.server.ip_address()}
        Domain: {self.server.domain()}
        World Download: {self.server.download()}''')

    @server.command(aliases=['send', 'exec', 'command'])
    async def send_command(self, ctx, command:str):
        """Send a command to the minecraft server"""
        response = self.server.send_command(command)
        logging.info(f"[send_command] Response: {response}")
        await ctx.send("Command sent")


    @commands.group(invoke_without_command=True)
    async def minecraft(self, ctx):
        await ctx.send('''Available commands
                minecraft on
                minecraft off''')

    @minecraft.command(pass_content=True, aliases=['start', 'on'])
    async def minecraft_start(self, ctx):
        """Starts the minecraft server"""
        await ctx.send('Minecraft starting...')
        response = self.server.minecraft_start()
        logging.info(f"[minecraft_start] Response: {response}")
        await ctx.send("Minecraft started successfully" if response.ok else "Error starting minecraft")

    @minecraft.command(pass_content=True,  aliases=['stop', 'off'])
    async def minecraft_stop(self, ctx):
        """Stops the minecraft server"""
        await ctx.send('Minecraft stopping...')
        response = self.server.minecraft_stop()
        logging.info(f"[minecraft_stop] Response: {response}")
        await ctx.send("Minecraft stopped successfully" if response.ok else "Error stopping minecraft")

    @minecraft.command(pass_content=True, aliases=['restart', 'reboot'])
    async def minecraft_reboot(self, ctx):
        await ctx.send("Rebooting server...")
        minecraft_stop()
        minecraft_start()


def setup(bot):
    bot.add_cog(ServerCog(bot))
    logging.info("Server cog loaded")
