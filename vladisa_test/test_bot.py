import telebot

import httplib2
import apiclient.discovery
from oauth2client.service_account import ServiceAccountCredentials



def lambda_hendler(event,context):

    if event['message']['text'] == '/start':

        chat = event['message']['from']['id']
        print(chat)

        token = '1180457199:AAF9mxKfFrSKcb4SK9F9HCGs4763MyHsqdU'

        bot = telebot.TeleBot(token)
        bot.config['api_key'] = token

        mes = bot.send_message(chat, 'Спасибо что пришел, братишка!')

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