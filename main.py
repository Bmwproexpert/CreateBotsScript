import telethon
import BotScript
import json
import sys


def init(config_path: str) -> (str, int, str, str):
    try:
        config = json.load(open(config_path, encoding='utf-8'))
        name_session = config["name"]
        api_id = int(config["api_id"])
        api_hash = config["api_hash"]
        deleteAfter = config["deleteAfter"]
        return name_session, api_id, api_hash, deleteAfter
    except FileNotFoundError as e:
        print(f"bad filepath {config_path}")
        sys.exit(1)
    except json.decoder.JSONDecodeError as e:
        print(f"json parsing failed {e}")
        sys.exit(2)
    except Exception as e:
        print(f"unexpected error while parsing config {e}")
        sys.exit(-1)


name_session, api_id, api_hash, deleteAfter = init("config_auth.json")
client = telethon.TelegramClient(name_session, api_id, api_hash)


async def main():
    user = 'BotFather'
    botcounter = int(input("Insert botcounter variable -- "))
    amount = int(input("Insert amount -- "))
    await client.send_message(user, "/start")
    for i in range(amount):
        await BotScript.create_bot(client, botcounter, user)
    if deleteAfter == "true":
        await client.delete_dialog(user)
        await client(telethon.functions.contacts.BlockRequest(id=user))
    print("Script ended")


with client:
    client.loop.run_until_complete(main())
