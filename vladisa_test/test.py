from telethon import TelegramClient
from telethon.tl.custom import Button

from telethon.tl.functions.channels import JoinChannelRequest
from telethon.tl.functions.channels import GetParticipantsRequest
from telethon.tl.functions.channels import GetFullChannelRequest
from telethon.tl.types import ChannelParticipantsSearch
from telethon.tl.functions.messages import ImportChatInviteRequest

import json
from pprint import pprint

# Remember to use your own values from my.telegram.org!
api_id = 5934336
api_hash = 'fdc97b0948be76b51059bd16820f4037'
bot_token = '1180457199:AAF9mxKfFrSKcb4SK9F9HCGs4763MyHsqdU'

chat = 'https://t.me/joinchat/UNmC0UT8drk91MbfNGoQrQ'

bot = TelegramClient('bot', api_id, api_hash).start(bot_token=bot_token)

client = TelegramClient('vladisa_s', api_id, api_hash)


async def main():
    # Getting information about yourself
    me = await client.get_me()

    mes = await client.send_message(293556094, 'саламм')
    mes = await client.forward_messages(673553041, 126039, 1180457199)

    # Илин номер 673553041

    # async for dialog in client.iter_dialogs():
    #     print(dialog.name, 'has ID', dialog.id)

    # await client.send_message(293556094, 'Салам алекум братьям с ингушетии', buttons=[
    #     [Button.url('Заходи скорее!',
    #                 'https://jt2qxn4n7l.execute-api.us-east-2.amazonaws.com/v1/user?id={0}'.format(673553041))]
    # ])

    print(me)

    # user_list = await client.get_participants(chat)
    #
    # print(len(user_list))
    #
    # for user in user_list:
    #
    #     id = user.id
    #
    #     print(id)
    #
    #     user = user.to_dict()
    #
    #     r = json.dumps(user, indent=4, sort_keys=True, ensure_ascii=False, default=str)
    #
    #     r = json.loads(r)
    #
    #     print('{}'.format(r['bot']))
    #
    #     if r['bot'] == False :
    #
    #         if user['status']['_'] == 'UserStatusOffline':
    #             print(user['status']['_'])
    #
    #     # print(user)
    #
    # res = await client(JoinChannelRequest(chat))
    #
    # res = res.to_dict()
    #
    # r = json.dumps(res, indent=4, sort_keys=True, ensure_ascii=False, default=str)
    #
    #
    # print('{}'.format(r))

    # permissions = client.iter_messages(-1001250671663)
    # # messages = await bot.get_stats(-1001250671663)
    # async for mess in client.iter_messages(-1001250671663):
    #
    #     mess = mess.to_dict()
    #
    #     r = json.dumps(mess, indent=4, sort_keys=True, ensure_ascii=False, default=str)
    #
    #     print('{}'.format(r))

# async def main():
#     # Getting information about yourself
#     me = await bot.get_me()
#     print(await bot.(-1001250671663))

with client:
    client.loop.run_until_complete(main())
#
# with bot:
#     bot.loop.run_until_complete(main())

    # "me" is a user object. You can pretty-print
    # any Telegram object with the "stringify" method:
    # print(me.stringify())



# async def main():
#     # Getting information about yourself
#     me = await client.get_me()
#
#     # "me" is a user object. You can pretty-print
#     # any Telegram object with the "stringify" method:
#     print(me.stringify())
#
#     # When you print something, you see a representation of it.
#     # You can access all attributes of Telegram objects with
#     # the dot operator. For example, to get the username:
#     username = me.username
#     print(username)
#     print(me.phone)
#
#     # You can print all the dialogs/conversations that you are part of:
#     async for dialog in client.iter_dialogs():
#         print(dialog.name, 'has ID', dialog.id)
#
#     # You can send messages to yourself...
#     await client.send_message('me', 'Hello, myself!')
#     # ...to some chat ID
#     await client.send_message(-100123456, 'Hello, group!')
#     # ...to your contacts
#     await client.send_message('+34600123123', 'Hello, friend!')
#     # ...or even to any username
#     await client.send_message('username', 'Testing Telethon!')
#
#     # You can, of course, use markdown in your messages:
#     message = await client.send_message(
#         'me',
#         'This message has **bold**, `code`, __italics__ and '
#         'a [nice website](https://example.com)!',
#         link_preview=False
#     )
#
#     # Sending a message returns the sent message object, which you can use
#     print(message.raw_text)
#
#     # You can reply to messages directly if you have a message object
#     await message.reply('Cool!')
#
#     # Or send files, songs, documents, albums...
#     await client.send_file('me', '/home/me/Pictures/holidays.jpg')
#
#     # You can print the message history of any chat:
#     async for message in client.iter_messages('me'):
#         print(message.id, message.text)
#
#         # You can download media from messages, too!
#         # The method will return the path where the file was saved.
#         if message.photo:
#             path = await message.download_media()
#             print('File saved to', path)  # printed after download is done

