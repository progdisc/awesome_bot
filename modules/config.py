import json

# Delete config.json if new keys are added
DEFAULT_CONFIG = {
    "bot_cmd": "!bot",
    "voting": {
        "immuneRoles": ["Admins", "Mods"],
        "voteThreshold": 5,
        "timeout_in_minutes": 5
    },
    "xkcd": {
        "timeLimit": 60,
        "limitMessages": False
    },
    "weather": {
        "icons": {
            "clear-day": ":sunny:",
            "clear-night": ":crescent_moon:",
            "rain": ":cloud_rain:",
            "snow": ":cloud_snow:",
            "sleet": ":cloud_snow:",
            "partly-cloudy-day": ":partly_sunny:",
            "partly-cloudy-night": ":partly_sunny:",
            "fog": ":fog:",
            "cloudy":":cloud:",
            "wind": ":wind_blowing_face:"
        }
  },
    "info":{
        "repo":"rgoliveira/awesomebot"
    },
    "commands": [
        "help",
        "eval",
        "pro",
        "stream",
        "uptime",
        "vote",
        "xkcd",
        "weather",
        "server",
        "pbf",
        "quickref",
        "info"
    ]
}

DEFAULT_TOKENS = {
    "discord": "",
    "google_geocode": "",
    "darksky": "",
    "replit": ""
}

try:
    with open('config.json', 'r') as file:
        CONFIG = json.load(file)
# Generate config file if config doesnt already exist
except FileNotFoundError:
    with open('config.json', 'w+') as file:
        json.dump(DEFAULT_CONFIG, file)
        CONFIG = DEFAULT_CONFIG

try:
    with open('tokens.json', 'r') as file:
        TOKENS = json.load(file)
except FileNotFoundError:
    with open('tokens.json', 'w+') as file:
        json.dump(DEFAULT_TOKENS, file)
        TOKENS = DEFAULT_TOKENS