import json
import random
import sys
import time

from telethon import TelegramClient

MESSAGE = None


async def create_bot(client: TelegramClient, botcounter: int, user: str):
    global MESSAGE
    await client.send_message(user, "/newbot")
    wait()
    check_success("Alright, a new bot. How are we going to call it?", await get_last_message(client, user))
    wait()
    try:
        await client.send_message(user, json.load(open("config_of_bot.json", encoding='utf-8'))["name"])
    except:
        print("Something with config_of_bot")
        sys.exit(1)
    wait()
    check_success("Good. Now let's choose a username for your bot.", await get_last_message(client, user))
    wait()
    await client.send_message(user, f"nudifier_ai_{botcounter}bot")
    wait()
    MESSAGE = await get_last_message(client, user)
    wait()

    while MESSAGE == "Sorry, this username is already taken. Please try something different." or MESSAGE == ("Sorry, this "
                                                                                                             "username is invalid."):
        botcounter += 1
        await client.send_message(user, f"nudifier_ai_{botcounter}bot")
        wait()
        MESSAGE = await get_last_message(client, user)
        wait()

    split = MESSAGE.split('\n')
    f = open("apikeys.txt", "a")
    f.write(f"nudifier_ai_{botcounter}bot - {split[3]}\n")
    f.close()

    wait()
    await client.send_message(user, "/mybots")
    wait()
    await client.start()
    wait()
    await edit_bot(client, user, botcounter)
    print(f"nudifier_ai_{botcounter}bot successfully created.")


async def edit_bot(client: TelegramClient, user: str, botcounter: int):
    messages = await client.get_messages(user)
    await messages[0].click(text=f'@nudifier_ai_{botcounter}bot')
    wait()
    messages = await client.get_messages(user)
    await messages[0].click(text=f'Edit Bot')
    wait()
    messages = await client.get_messages(user)
    await messages[0].click(text=f'Edit About')
    wait()
    try:
        await client.send_message(user, json.load(open("config_of_bot.json", encoding='utf-8'))["about"])
    except:
        print("Problems with config_of_bot.json")
    wait()
    check_success("Success! About section updated.", await get_last_message(client, user))
    messages = await client.get_messages(user)
    await messages[0].click(0)
    wait()
    messages = await client.get_messages(user)
    await messages[0].click(text=f'Edit Bot')
    wait()
    messages = await client.get_messages(user)
    await messages[0].click(text=f'Edit Description')
    wait()
    await client.send_message(user, json.load(open("config_of_bot.json", encoding='utf-8'))["description"])
    wait()
    check_success("Success! Description updated.", await get_last_message(client, user))
    wait()
    messages = await client.get_messages(user)
    await messages[0].click(0)
    wait()
    messages = await client.get_messages(user)
    await messages[0].click(text=f'Edit Bot')
    wait()
    messages = await client.get_messages(user)
    await messages[0].click(text=f'Edit Botpic')
    wait()
    try:
        await client.send_file(user, 'avatar.png')
    except:
        print("cannot find avatar.png")
        sys.exit(1)
    wait()
    check_success("Success! Profile photo updated.", await get_last_message(client, user))
    wait()
    messages = await client.get_messages(user)
    await messages[0].click(0)
    wait()
    messages = await client.get_messages(user)
    await messages[0].click(text=f'Edit Bot')
    wait()
    messages = await client.get_messages(user)
    await messages[0].click(text=f'Edit Privacy Policy')
    wait()
    await client.send_message(user, "https://nudifier.ai/privacy.pdf")
    wait()
    check_success("Success! Privacy policy updated.", await get_last_message(client, user))
    wait()
    messages = await client.get_messages(user)
    await messages[0].click(0)
    wait()
    messages = await client.get_messages(user)
    await messages[0].click(text=f'Edit Bot')
    wait()
    messages = await client.get_messages(user)
    await messages[0].click(text=f'Edit Commands')
    wait()
    await client.send_message(user, "menu - Menu")
    wait()
    check_success("Success! Command list updated.", await get_last_message(client, user))
    wait()
    messages = await client.get_messages(user)
    await messages[0].click(0)
    wait()
    messages = await client.get_messages(user)
    await messages[0].click(text="Bot Settings")
    wait()
    messages = await client.get_messages(user)
    await messages[0].click(text="Configure Mini App")
    wait()
    messages = await client.get_messages(user)
    await messages[0].click(text="Enable Mini App")
    wait()
    await client.send_message(user, "https://nudifier.ai/webapp/painter")
    wait()
    check_success("Success! Mini App settings updated.", await get_last_message(client, user))


def check_success(text_of_success, text_from_client):
    if text_of_success in text_from_client:
        pass
    else:
        print(text_from_client)
        sys.exit(1)


def wait():
    time.sleep(random.randint(3, 5))


async def get_last_message(client, user) -> str:
    messages = await client.get_messages(user)
    return messages[0].text
