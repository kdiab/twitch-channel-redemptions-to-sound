import os
from dotenv import load_dotenv
from playsound import playsound
from twitchAPI.pubsub import PubSub
from twitchAPI.twitch import Twitch
from twitchAPI.helper import first
from twitchAPI.types import AuthScope
from twitchAPI.oauth import UserAuthenticator
import asyncio
from pprint import pprint
from uuid import UUID

load_dotenv('settings')
APP_ID = os.getenv('APP_ID')
APP_SECRET = os.getenv('APP_SECRET')
USER_SCOPE = [AuthScope.CHANNEL_READ_REDEMPTIONS]
TARGET_CHANNEL = os.getenv('TARGET_CHANNEL')


async def callback_redemptions(uuid: UUID, data: dict) -> None:
    display_name = data['data']['redemption']['user']['display_name']
    sound_byte = data['data']['redemption']['reward']['title']
    print(display_name, 'redeemed', sound_byte)

    sound_list = []
    sound_byte_dir = os.scandir('sounds')
    for entry in sound_byte_dir:
        b = entry.name.split('.')
        sound_list.append(b[0])
    print(sound_list)

    if sound_byte in sound_list:
        playsound('sounds/'+sound_byte+'.mp3')


async def bot():
    # setting up Authentication and getting your user id
    twitch = await Twitch(APP_ID, APP_SECRET)
    auth = UserAuthenticator(twitch, [AuthScope.CHANNEL_READ_REDEMPTIONS], force_verify=False)
    token, refresh_token = await auth.authenticate()
    # you can get your user auth token and user auth refresh token following the example in twitchAPI.oauth
    await twitch.set_user_authentication(token, [AuthScope.CHANNEL_READ_REDEMPTIONS], refresh_token)
    user = await first(twitch.get_users(logins=[TARGET_CHANNEL]))

    # starting up PubSub
    pubsub = PubSub(twitch)
    pubsub.start()
    # you can either start listening before or after you started pubsub.
    uuid = await pubsub.listen_channel_points(user.id, callback_redemptions)
    print('press S to stop program')
    bot_active = True
    while bot_active:
        user_input = input()
        if user_input.lower() == 's':
            bot_active = False

    await pubsub.unlisten(uuid)
    pubsub.stop()
    await twitch.close()

asyncio.run(bot())
