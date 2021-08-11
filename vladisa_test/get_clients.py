import httplib2
import apiclient.discovery
from oauth2client.service_account import ServiceAccountCredentials

from datetime import datetime

from telethon import TelegramClient
from telethon.tl.functions.channels import JoinChannelRequest
from telethon.tl.functions.channels import GetParticipantsRequest
from telethon.tl.functions.channels import GetFullChannelRequest
from telethon.tl.types import ChannelParticipantsSearch
from telethon.tl.functions.messages import ImportChatInviteRequest

import json
from pprint import pprint

# Файл, полученный в Google Developer Console
CREDENTIALS_FILE = 'client_secret.json'
# ID Google Sheets документа (можно взять из его URL)
spreadsheet_id = '1bCkkreYMmVfn6fG7W5cjBgTYtip7kk2Z2jiE25L4V28'

# Добавляем все константы для работы с телеграм апи

api_id = 5934336
api_hash = 'fdc97b0948be76b51059bd16820f4037'
bot_token = '1180457199:AAF9mxKfFrSKcb4SK9F9HCGs4763MyHsqdU'

chat = 'https://t.me/joinchat/UNmC0USrWRAnW1Z67eQDCw'

bot = TelegramClient('bot', api_id, api_hash).start(bot_token=bot_token)

telegram_client = TelegramClient('vladisa_s', api_id, api_hash)



# Авторизуемся и получаем service — экземпляр доступа к API
credentials = ServiceAccountCredentials.from_json_keyfile_name(
    CREDENTIALS_FILE,
    ['https://www.googleapis.com/auth/spreadsheets',
     'https://www.googleapis.com/auth/drive'])
httpAuth = credentials.authorize(httplib2.Http())
service = apiclient.discovery.build('sheets', 'v4', http = httpAuth)


# достаем всех клиентов

spreadsheet = service.spreadsheets().get(spreadsheetId = spreadsheet_id).execute()
sheetList = spreadsheet.get('sheets')

# достаем чаты для поиска клиентов из таблички

for sheet in sheetList :
    if sheet['properties']['title'] == 'Чаты для поиска клиентов':
        rows_count = sheet['properties']['gridProperties']['rowCount']

addvertisement_chats = service.spreadsheets().values().get(
    spreadsheetId=spreadsheet_id,
    range='Чаты для поиска клиентов!A1:A' + str(rows_count),
    majorDimension='ROWS'
).execute()['values']


# chats_list = ['https://t.me/joinchat/xG6MdIuTAQY1NDcy']
chats_list = []

for chat in addvertisement_chats:
    chats_list.append(chat[0])



# Начинаем сбор клиентов из чатов
async def main(chats_list = 'false', ):
    user_list = []
    user_list_dict_format = []



    # Проходимся по каждому чату
    for chat in chats_list:

        try:
            user_list = await telegram_client.get_participants(chat)

            for user in user_list:

                user = user.to_dict()

                user = json.dumps(user, indent=4, sort_keys=True, ensure_ascii=False, default=str)

                user = json.loads(user)

                if user['bot'] == False:

                    try:
                        if user['status']['_'] == 'UserStatusOffline':
                            user_status = user['status']['was_online']

                            if datetime.strptime(user_status, '%Y.%m.%d') < datetime.date('2020.06.01'):
                                continue
                    except:
                        pass

                    try:
                        if user['status']['_'] == 'UserStatusRecently':
                            user_status = 'Недавно'
                    except:
                        pass

                    try:
                        if user['status']['_'] == 'UserStatusOnline':
                            user_status = 'Онлайн'
                    except:
                        pass

                    user_list_dict_format.append(
                        {user['id'] : {
                            'id' : user['id'],
                            'username' : user['username'],
                            'status' : user_status}
                        }
                    )



        except:
            pprint(chat + ' Чат не отвечает')
            continue

    user_list_to_append = []

    for sheet in sheetList:
        if sheet['properties']['title'] == 'Клиенты':
            rows_count = sheet['properties']['gridProperties']['rowCount']

    clients = service.spreadsheets().values().get(
        spreadsheetId=spreadsheet_id,
        range='Клиенты!A1:A' + str(rows_count),
        majorDimension='ROWS'
    ).execute()['values']

    clients_list = []

    for client in clients:
        try:

            clients_list.append(client[0])
        except:
            pass




    user_ids_list = []

    for user in user_list_dict_format:
        # Проверяем каждого пользователя бот он или нет
        user_info = list(user.values())[0]
        if str(user_info['id']) in clients_list:
            # try:
            #     service.spreadsheets().values().update(spreadsheetId=spreadsheet_id,
            #                                            range='Клиенты!C{0}:D{0}'.format(
            #                                                str(clients_list.index(str(user_info['id'])))),
            #                                            valueInputOption='USER_ENTERED',
            #                                            body={
            #                                                "majorDimension": "COLUMNS",
            #                                                "values": [[user_info['status']]]
            #                                            }
            #                                            ).execute()
            # except:
            #     pass

            continue


        else:

            if user_info['id'] not in user_ids_list:

                user_ids_list.append(user_info['id'])

                user_list_to_append.append([user_info['id'], user_info['username'], user_info['status']])

    service.spreadsheets().values().update(spreadsheetId=spreadsheet_id,
                                           range='Клиенты!N1',
                                           valueInputOption='USER_ENTERED',
                                           body={
                                               "majorDimension": "COLUMNS",
                                               "values": [[str(datetime.today())]]
                                           }
                                           ).execute()

    pprint(len(user_list_to_append))

    range_ = 'Клиенты!A2:C2'  # TODO: Update placeholder value.

    value_input_option = 'USER_ENTERED'

    # How the input data should be inserted.
    insert_data_option = 'INSERT_ROWS'

    value_range_body = {
        "majorDimension": "ROWS",
        "values": user_list_to_append
    }

    request = service.spreadsheets().values().append(spreadsheetId=spreadsheet_id,
                                                     range=range_,
                                                     valueInputOption=value_input_option,
                                                     insertDataOption=insert_data_option,
                                                     body=value_range_body)

    response = request.execute()

    pprint(response)

        # Проверяем клиентов после каждого обновления чтобы не было повторов

with telegram_client:
   telegram_client.loop.run_until_complete(main(chats_list))

