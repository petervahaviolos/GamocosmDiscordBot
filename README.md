# Gamocosm Discord Bot

Discord Bot for controlling a gamocosm/discord minecraft server

## Discord Commands

- /server [start, stop] - Starts/stops the DigitalOcean server and creates a snapshot of the droplet if stopped
- /minecraft [start, stop] - Starts/stops only the Minecraft server
- /server status - View status of the DigitalOcean and Minecraft server, server ip address, and a URL to download the world
- /server send [command] - Sends a command to the Minecraft server

## Installation

## Discord
- Go to https://discord.com/developers/applications and create a new discord application
- Make the application a 'bot' (go to bot section under settings)
- Add the bot to your server (go to oauth2 section and click 'bot' under scopes, then copy the url)
- Copy the bot token (from the 'bot' section in settings) to .config/config_default.yaml

## Gamocosm
- Create an account on https://gamocosm.com/ and setup your DigitalOcean server
- Copy the server id from the URL (https://gamocosm.com/servers/SERVER_ID)
- Copy the api key from the advanced tab
- Place server id in .config/config_default.yaml
- Place api key in .config/config_default.yaml


## Usage

- Fill in the required data in .config/config_default.yaml
- Rename config_default.yaml to config.yaml
- Run bot.py
- Bot should be online and running on your server

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
[MIT](https://choosealicense.com/licenses/mit/)
