from telethon import TelegramClient
from telethon.tl.custom import Button

import httplib2
import apiclient.discovery
from oauth2client.service_account import ServiceAccountCredentials

# Remember to use your own values from my.telegram.org!
api_id = 5934336
api_hash = 'fdc97b0948be76b51059bd16820f4037'
bot_token = '1180457199:AAF9mxKfFrSKcb4SK9F9HCGs4763MyHsqdU'

# chat = 'https://t.me/joinchat/UNmC0UT8drk91MbfNGoQrQ'

bot = TelegramClient('bot', api_id, api_hash).start(bot_token=bot_token)

telegramClient = TelegramClient('vladisa_s', api_id, api_hash)




def lambda_handler(event, context):

    with bot:
        bot.loop.run_until_complete(main(event=event))



async def main(event=False):


    if event['message']['text'] == '/start':

        chat = event['message']['from']['id']

        mes = await bot.send_message(chat, 'Молодец что написал, хлопец! Здесь ты получишь уведомление о том, что проект запустился!')

        print(mes.id)
        print(mes)

        # Файл, полученный в Google Developer Console
        CREDENTIALS_FILE = 'client_secret.json'
        # ID Google Sheets документа (можно взять из его URL)
        spreadsheet_id = '1bCkkreYMmVfn6fG7W5cjBgTYtip7kk2Z2jiE25L4V28'

        # Авторизуемся и получаем service — экземпляр доступа к API
        credentials = ServiceAccountCredentials.from_json_keyfile_name(
            CREDENTIALS_FILE,
            ['https://www.googleapis.com/auth/spreadsheets',
             'https://www.googleapis.com/auth/drive'])
        httpAuth = credentials.authorize(httplib2.Http())
        service = apiclient.discovery.build('sheets', 'v4', http=httpAuth)

        # достаем всех клиентов

        spreadsheet = service.spreadsheets().get(spreadsheetId=spreadsheet_id).execute()
        sheetList = spreadsheet.get('sheets')

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


        if str(chat) in clients_list:
            res = service.spreadsheets().values().update(spreadsheetId=spreadsheet_id,
                                                         range='Клиенты!F{0}'.format(
                                                             str(clients_list.index(
                                                                 str(chat)) + 1)),
                                                         valueInputOption='USER_ENTERED',
                                                         body={
                                                             "majorDimension": "COLUMNS",
                                                             "values": [['Да']]
                                                         }
                                                         ).execute()


event = {
  "message": {
    "message_id": 31,
    "from": {
      "id": 293556094,
      "is_bot": False,
      "first_name": "Vladisa_S",
      "username": "vladisa_s",
      "language_code": "ru"
    },
    "chat": {
      "id": 293556094,
      "first_name": "Vladisa_S",
      "username": "vladisa_s",
      "type": "private"
    },
    "date": 1624549137,
    "text": "/start",
    "entities": [
      {
        "offset": 0,
        "length": 6,
        "type": "bot_command"
      }
    ]
  },
  "update_id": 592383905
}

lambda_handler(event,context=False)