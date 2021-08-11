from telethon import TelegramClient
from pprint import pprint
from telethon.tl.custom import Button
from telethon.tl.functions.messages import GetHistoryRequest
from telethon.tl.functions.channels import GetFullChannelRequest


import random
import json

# Remember to use your own values from my.telegram.org!

# Получаем данные твоего приложения после регистрации telegram.org
api_id = 6839459
api_hash = '0595d82ee8849cfa9942153e9dc32703'

# Токен бота получаем в @botFather в самой телеге, так изи думаю это ты уже сделал
bot_token = '1180457199:AAF9mxKfFrSKcb4SK9F9HCGs4763MyHsqdU'

bot = TelegramClient('bot', api_id, api_hash).start(bot_token=bot_token)

# parse_mode нужен для того чтобы можно было обрамлять текст как хочешь, те здесь стоит html поэтому можно использовать теги как при верстке
# напривем <b> <a> и тд
bot.parse_mode = 'html'



# создаем клиенты через которого будем осуществлять вход в телеграм, вписываем username без @ лучше использовать свой акк
telegramClient = TelegramClient('telemilk', api_id, api_hash)


# дальше пройдемся по каждому примеру
async def main():

    # например соберем все диалоги пользователя через которого ты зашел
    async for dialog in telegramClient.iter_dialogs():
        print(dialog.name, 'has ID', dialog.id)

    # для разбора будем использовать тестовый канал с id -1001250671663

    # если работать с функцией    channel_info = await telegramClient.get_stats(-1001250671663)
    # то можно словить трейс, о том что ты не являешься админом канала, возможно, поэтому лучше юзать get_entety
    # вот фулл трейс

    # telethon.errors.rpcerrorlist.ChatAdminRequiredError:
    # Chat admin privileges are required to do that in the specified chat
    # (for example, to send a message in a channel which is not yours),
    # or invalid permissions used for the channel or group (caused by GetBroadcastStatsRequest)

    # достаем инфу о канале с помощью метода get_entity

    full_channel_info = await telegramClient(GetFullChannelRequest(channel=-1001250671663))

    full_channel_info = full_channel_info.to_dict()
    full_channel_info = json.dumps(full_channel_info, indent=4, sort_keys=True, ensure_ascii=False, default=str)
    full_channel_info = json.loads(full_channel_info)

    print(full_channel_info)

    # достаем инфу о канале с помощью метода get_entity

    channel_info = await telegramClient.get_entity(-1001250671663)

    channel_info = channel_info.to_dict()
    channel_info = json.dumps(channel_info, indent=4, sort_keys=True, ensure_ascii=False, default=str)
    channel_info = json.loads(channel_info)

    print(channel_info)

    # Response :
    # {
    #     "_": "Channel",
    #     "access_hash": -8115980619907360606,
    #     "admin_rights": {
    #         "_": "ChatAdminRights",
    #         "add_admins": "True",
    #         "anonymous": "False",
    #         "ban_users": "True",
    #         "change_info": "True",
    #         "delete_messages": "True",
    #         "edit_messages": "True",
    #         "invite_users": "True",
    #         "manage_call": "True",
    #         "other": "True",
    #         "pin_messages": "True",
    #         "post_messages": "True"
    #     },
    #     "banned_rights": "None",
    #     "broadcast": "True",
    #     "call_active": "False",
    #     "call_not_empty": "False",
    #     "creator": "True",
    #     "date": "2021-04-08 13:27:52+00:00",
    #     "default_banned_rights": "None",
    #     "fake": "False",
    #     "gigagroup": "False",
    #     "has_geo": "False",
    #     "has_link": "False",
    #     "id": 1250671663,
    #     "left": "False",
    #     "megagroup": "False",
    #     "min": "False",
    #     "participants_count": "None",
    #     "photo": {
    #         "_": "ChatPhoto",
    #         "dc_id": 2,
    #         "has_video": "False",
    #         "photo_big": {
    #             "_": "FileLocationToBeDeprecated",
    #             "local_id": 54843,
    #             "volume_id": 200300000277
    #         },
    #         "photo_small": {
    #             "_": "FileLocationToBeDeprecated",
    #             "local_id": 54841,
    #             "volume_id": 200300000277
    #         }
    #     },
    #     "restricted": "False",
    #     "restriction_reason": [],
    #     "scam": "False",
    #     "signatures": "False",
    #     "slowmode_enabled": "False",
    #     "title": "Test Chanel",
    #     "username": "None",
    #     "verified": "False",
    #     "version": 0
    # };


    # достаем конкретный месседж по id с помощбю метода get_messages

    chosen_mess = (await telegramClient.get_messages(-1001250671663, 125))[0]

    chosen_mess = chosen_mess.to_dict()
    chosen_mess = json.dumps(chosen_mess, indent=4, sort_keys=True, ensure_ascii=False, default=str)
    chosen_mess = json.loads(chosen_mess)

    print(chosen_mess)

    # Response :
    # {
    #   '_': "Message" ,
    #   'date': '2021-05-21 09:43:56+00:00' ,
    #   'edit_date': None ,
    #   'edit_hide': False ,
    #   'entities': [
    #     {
    #       '_': 'MessageEntityTextUrl' ,
    #       'length': 6 ,
    #       'offset': 0 ,
    #       'url': 'https://ya.ru/'
    #     }
    #   ] ,
    #   'forwards': 0 ,
    #   'from_id': None ,
    #   'from_scheduled': False ,
    #   'fwd_from': None ,
    #   'grouped_id': None ,
    #   'id': 125 ,
    #   'legacy': False ,
    #   'media': {
    #     '_': 'MessageMediaPhoto' ,
    #     'photo': {
    #       '_': 'Photo' ,
    #       'access_hash': 7174488044190277104 ,
    #       'date': '2021-05-21 09:40:02+00:00' ,
    #       'dc_id': 2 ,
    #       'file_reference': "b'\\x04J\\x8b\\xbc/\\x00\\x00\\x00}`\\xf5\\xc1B\\xd3\\x1f\\xea\\xe2F\\x06z\\x9f]\\x1a \\x00\\xf9\\xd2A\\xcd'" ,
    #       'has_stickers': False ,
    #       'id': 5278307854241084266 ,
    #       'sizes': [
    #         {
    #           '_': 'PhotoStrippedSize' ,
    #           'bytes': "b'\\x01((\\xb1\\xbc\\xd3w\\xf3A\\xa8\\xe4\\xf3?\\x80/\\xe2k+\\x16O\\xe6\\x1cS\\x86\\xe3T\\xdb\\xed\\x05\\x0ev)\\x1d\\xc1\\xa5\\xb3\\x9ac!I>a\\x8c\\x83Um\\x05}l]\\x03\\x14Rf\\x8a\\x91\\x90\\xd1\\x8ek7\\xed\\x13\\xa3\\x94$\\xee\\x1d\\xb1R%\\xf9\\x1c:\\x8f\\xe5U`\\xb9\\xa0c\\xdf\\x13\\x0f\\xe2\\xedTVO*d# \\x03\\x82*d\\xbe\\x8c\\xaf9\\x15Vy\\xb7\\xcd\\xb8s\\xebUO{2&\\xae\\xae\\x8dl\\x83\\xc8\\xa2\\xaaCs\\x0f\\x96\\xaad\\x19\\x02\\x8a\\x86\\xacZ\\xd4\\x9b\\x1c\\xe6\\x86\\x8d\\\\a\\xd47\\xd4QE+\\x8c\\x88\\xd9@N|\\xbc}\\t\\xa6\\x9d>\\x12>]\\xca~\\xb9\\xa2\\x8a\\x14\\x98\\x9a#\\x1ah\\x0b\\xcc\\x87?J(\\xa2\\x9f3\\x0b#'" ,
    #           'type': 'i'
    #         } ,
    #         {
    #           '_': 'PhotoSize' ,
    #           'h': 320 ,
    #           'location': {
    #             '_': 'FileLocationToBeDeprecated' ,
    #             'local_id': 288596 ,
    #             'volume_id': 200236100633
    #           } ,
    #           'size': 16483 ,
    #           'type': 'm' ,
    #           'w': 320
    #         } ,
    #         {
    #           '_': 'PhotoSize' ,
    #           'h': 800 ,
    #           'location': {
    #             '_': 'FileLocationToBeDeprecated' ,
    #             'local_id': 288597 ,
    #             'volume_id': 200236100633
    #           } ,
    #           'size': 70015 ,
    #           'type': 'x' ,
    #           'w': 800
    #         } ,
    #         {
    #           '_': 'PhotoSizeProgressive' ,
    #           'h': 1280 ,
    #           'location': {
    #             '_': 'FileLocationToBeDeprecated' ,
    #             'local_id': 288594 ,
    #             'volume_id': 200236100633
    #           } ,
    #           'sizes': [
    #             18388 ,
    #             37436 ,
    #             52754 ,
    #             77034 ,
    #             173426
    #           ] ,
    #           'type': 'y' ,
    #           'w': 1280
    #         }
    #       ] ,
    #       'video_sizes': [ ]
    #     } ,
    #     'ttl_seconds': None
    #   } ,
    #   'media_unread': False ,
    #   'mentioned': False ,
    #   'message': 'ссылка' ,
    #   'out': True ,
    #   'peer_id': {
    #     '_': 'PeerChannel' ,
    #     'channel_id': 1250671663
    #   } ,
    #   'pinned': False ,
    #   'post': True ,
    #   'post_author': None ,
    #   'replies': None ,
    #   'reply_markup': None ,
    #   'reply_to': None ,
    #   'restriction_reason': [ ] ,
    #   'silent': False ,
    #   'ttl_period': None ,
    #   'via_bot_id': None ,
    #   'views': 4
    # }
    #


    # достанем все интересующие нас посты, в данном случае возьмем самый последний будем использовать
    # GetHistoryRequest, более подробно о данном методе здесь https://docs.telethon.dev/en/latest/modules/client.html?highlight=GetHistoryRequest#telethon.client.messages.MessageMethods.iter_messages


    posts = await telegramClient(GetHistoryRequest(
        peer= -1001250671663,
        limit= 1, # лимит на посты, поставим 1 пост
        offset_date=None, # посты за какую дату нам нужны здесь либо None либо дату в формате time если я не ошибаюсь
        offset_id=0, # id поста с которого начнется итерация
        max_id=0,
        min_id=0,
        add_offset=0, #
        hash=0))

    print((posts.messages[0]))

    post_data_to_json = posts.messages[0]
    post_data_to_json = post_data_to_json.to_dict()
    post_data_to_json = json.dumps(post_data_to_json, indent=4, sort_keys=True, ensure_ascii=False, default=str)
    post_data_to_json = json.loads(post_data_to_json)

    # print(post_data_to_json)

    # Мы забираем абсолютно любую инфу какую нужно, те это id сообщения, просмотры, репосты, вложения (из них составляются упоминания и так далее) и вообще все что нужно
    # Ниже будет ответ в формате JSON и просто объект

#{
#   "_": "Message",
#   "date": "2021-05-21 09:43:56+00:00",
#   "edit_date": "None",
#   "edit_hide": "False",
#   "entities": [
#     {
#       "_": "MessageEntityTextUrl",
#       "length": 6,
#       "offset": 0,
#       "url": "https://ya.ru/"
#     }
#   ],
#   "forwards": 0,
#   "from_id": "None",
#   "from_scheduled": "False",
#   "fwd_from": "None",
#   "grouped_id": "None",
#   "id": 125,
#   "legacy": "False",
#   "media": {
#     "_": "MessageMediaPhoto",
#     "photo": {
#       "_": "Photo",
#       "access_hash": -9025023940125615000,
#       "date": "2021-05-21 09:40:02+00:00",
#       "dc_id": 2,
#       "file_reference": "b",
#       "has_stickers": "False",
#       "id": 5278307854241084000,
#       "sizes": [
#         {
#           "_": "PhotoStrippedSize",
#           "bytes": "b",
#           "type": "i"
#         },
#         {
#           "_": "PhotoSize",
#           "h": 320,
#           "location": {
#             "_": "FileLocationToBeDeprecated",
#             "local_id": 288596,
#             "volume_id": 200236100633
#           },
#           "size": 16483,
#           "type": "m",
#           "w": 320
#         },
#         {
#           "_": "PhotoSize",
#           "h": 800,
#           "location": {
#             "_": "FileLocationToBeDeprecated",
#             "local_id": 288597,
#             "volume_id": 200236100633
#           },
#           "size": 70015,
#           "type": "x",
#           "w": 800
#         },
#         {
#           "_": "PhotoSizeProgressive",
#           "h": 1280,
#           "location": {
#             "_": "FileLocationToBeDeprecated",
#             "local_id": 288594,
#             "volume_id": 200236100633
#           },
#           "sizes": [
#             18388,
#             37436,
#             52754,
#             77034,
#             173426
#           ],
#           "type": "y",
#           "w": 1280
#         }
#       ],
#       "video_sizes": []
#     },
#     "ttl_seconds": "None"
#   },
#   "media_unread": "False",
#   "mentioned": "False",
#   "message": "ссылка",
#   "out": "False",
#   "peer_id": {
#     "_": "PeerChannel",
#     "channel_id": 1250671663
#   },
#   "pinned": "False",
#   "post": "True",
#   "post_author": "None",
#   "replies": "None",
#   "reply_markup": "None",
#   "reply_to": "None",
#   "restriction_reason": [],
#   "silent": "False",
#   "ttl_period": "None",
#   "via_bot_id": "None",
#   "views": 4
# }


    # Получим объект Message, то что в нем будет ниже в виде объекта
    # Message(
    # id=125,
    # peer_id=PeerChannel(channel_id=1250671663),
    # date=datetime.datetime(2021, 5, 21, 9, 43, 56, tzinfo=datetime.timezone.utc),
    # message='ссылка',
    # out=False,
    # mentioned=False,
    # media_unread=False,
    # silent=False,
    # post=True,
    # from_scheduled=False,
    # legacy=False,
    # edit_hide=False,
    # pinned=False,
    # from_id=None,
    # fwd_from=None,
    # via_bot_id=None,
    # reply_to=None,
    # media =
    #       MessageMediaPhoto(
    #               photo = Photo(
    #                   id=5278307854241084266,
    #                   access_hash=-9025023940125614762,
    #                   file_reference=b'\x02J\x8b\xbc/\x00\x00\x00}`\xf4!\xc0u)0A\xe3\xe6<\x85\x05\xb9\xd0\xb4?\xac\x98\xd3',
    #                   date=datetime.datetime(2021, 5, 21, 9, 40, 2, tzinfo=datetime.timezone.utc),
    #                   sizes= [PhotoStrippedSize(
    #                               type='i',
    #                               bytes=b'\x01((\xb1\xbc\xd3w\xf3A\xa8\xe4\xf3?\x80/\xe2k+\x16O\xe6\x1cS\x86\xe3T\xdb\xed\x05\x0ev)\x1d\xc1\xa5\xb3\x9ac!I>a\x8c\x83Um\x05}l]\x03\x14Rf\x8a\x91\x90\xd1\x8ek7\xed\x13\xa3\x94$\xee\x1d\xb1R%\xf9\x1c:\x8f\xe5U`\xb9\xa0c\xdf\x13\x0f\xe2\xedTVO*d# \x03\x82*d\xbe\x8c\xaf9\x15Vy\xb7\xcd\xb8s\xebUO{2&\xae\xae\x8dl\x83\xc8\xa2\xaaCs\x0f\x96\xaad\x19\x02\x8a\x86\xacZ\xd4\x9b\x1c\xe6\x86\x8d\\a\xd47\xd4QE+\x8c\x88\xd9@N|\xbc}\t\xa6\x9d>\x12>]\xca~\xb9\xa2\x8a\x14\x98\x9a#\x1ah\x0b\xcc\x87?J(\xa2\x9f3\x0b#'),
    #                           PhotoSize(
    #                               type='m',
    #                               location=FileLocationToBeDeprecated(
    #                                       volume_id=200236100633,
    #                                       local_id=288596),
#                                   w=320,
#                                   h=320,
#                                   size=16483),
#                               PhotoSize(
#                                   type='x',
#                                   location=FileLocationToBeDeprecated(
#                                           volume_id=200236100633,
#                                           local_id=288597),
#                                   w=800,
#                                   h=800,
#                                   size=70015),
#                               PhotoSizeProgressive(
#                                   type='y',
#                                   location=FileLocationToBeDeprecated(
#                                           volume_id=200236100633,
#                                           local_id=288594),
#                                   w=1280,
#                                   h=1280,
#                                   sizes=[18388, 37436, 52754, 77034, 173426])
#                          ],
#                           dc_id=2,
#                           has_stickers=False,
#                           video_sizes=[]),
#                     ttl_seconds=None),
#   reply_markup=None,
#   entities=[MessageEntityTextUrl(
#                   offset=0,
#                   length=6,
#                   url='https://ya.ru/')],
#   views=4,
#   forwards=0,
#   replies=None,
#   edit_date=None,
#   post_author=None,
#   grouped_id=None,
#   restriction_reason=[],
#   ttl_period=None)







with telegramClient:
    telegramClient.loop.run_until_complete(main())