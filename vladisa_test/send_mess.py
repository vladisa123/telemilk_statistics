from telethon import TelegramClient
from pprint import pprint
from telethon.tl.custom import Button

import random
import json

import httplib2
import apiclient.discovery
from oauth2client.service_account import ServiceAccountCredentials

# Remember to use your own values from my.telegram.org!
from telethon.tl.functions.messages import GetHistoryRequest

api_id = 6839459
api_hash = '0595d82ee8849cfa9942153e9dc32703'
bot_token = '1180457199:AAF9mxKfFrSKcb4SK9F9HCGs4763MyHsqdU'

# chat = 'https://t.me/joinchat/UNmC0UT8drk91MbfNGoQrQ'

bot = TelegramClient('bot', api_id, api_hash).start(bot_token=bot_token)

telegramClient = TelegramClient('telemilk', api_id, api_hash)
bot.parse_mode = 'html'


scripts_vars = {
    1 :
"""
<b><a href = "https://telemilk.tilda.ws">Telemilk</a></b> - первая полноценная платформа для бизнеса в Telegram!

<b>
- Управляй своим каналом
- Находи каналы для размещения рекламы
- Покупай, продавай, анализируй -  любой канал
- Пользуйся полноценной статистикой своей и чужой рекламы
- Совершай только безопасные сделки
- Ищи товары и услуги и размещай их рекламу на своем канале
- Автоматизируй все процессы
</b>

Запуск платформы уже в августе. Первым 100 клиентам промокод на  премиальные условия БЕСПЛАТНО!

Не опоздай!
  
"""
}

async def main():

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

    # spreadsheet = service.spreadsheets().get(spreadsheetId=spreadsheet_id).execute()
    # sheetList = spreadsheet.get('sheets')
    #
    # for sheet in sheetList:
    #     if sheet['properties']['title'] == 'Клиенты':
    #         rows_count = sheet['properties']['gridProperties']['rowCount']
    #
    # clients = service.spreadsheets().values().get(
    #     spreadsheetId=spreadsheet_id,
    #     range='Клиенты!A1:D1' + str(rows_count),
    #     majorDimension='ROWS'
    # ).execute()['values']
    #
    # clients_list = []
    #
    # for client in clients :
    #     try:
    #         if client[3] == 'Да':
    #             pass
    #         else:
    #             clients_list.append(client[0])
    #     except:
    #         clients_list.append(client[0])



    # for client in clients_list:
    #     try:
    #         clients_list.append(client[0])
    #     except:
    #         pass

    chats = [1777266622,673553041,293556094]
    # chats = [1777266622]

    for chat in chats:

        print(await telegramClient.get_me())
        print(await bot.get_me())

        number_of_script = random.randint(1, len(scripts_vars))

        await bot.send_message(
            1777266622,
            scripts_vars[number_of_script],
            buttons=[
                [Button.url('TELEMILK 🚀', 'https://890en48a9c.execute-api.us-east-2.amazonaws.com/v0/user?id={0}'.format(chat))]]
        )

        posts = await telegramClient(GetHistoryRequest(
            peer=1180457199,
            limit=1,
            offset_date=None,
            offset_id=0,
            max_id=0,
            min_id=0,
            add_offset=0,
            hash=0))

        print((posts.messages[0]).id)


        # достаем последнее отправленное ботом сообщение



        mes = await telegramClient.forward_messages(chat, int((posts.messages[0]).id) , 1180457199)

        # print(mes)

        # if str(chat) in clients_list:
        #     res = service.spreadsheets().values().update(spreadsheetId=spreadsheet_id,
        #                                                  range='Клиенты!D{0}:G{0}'.format(
        #                                                      str(clients_list.index(
        #                                                          str(chat)) + 1)),
        #                                                  valueInputOption='USER_ENTERED',
        #                                                  body={
        #                                                      "majorDimension": "COLUMNS",
        #                                                      "values": [['Да', mess_to_forward_id]]
        #                                                  }
        #                                                  ).execute()


with telegramClient:
    telegramClient.loop.run_until_complete(main())