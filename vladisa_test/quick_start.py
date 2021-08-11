from pprint import pprint

import httplib2
import apiclient.discovery
from oauth2client.service_account import ServiceAccountCredentials


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
service = apiclient.discovery.build('sheets', 'v4', http = httpAuth)


#Получаем листы

spreadsheet = service.spreadsheets().get(spreadsheetId = spreadsheet_id).execute()
sheetList = spreadsheet.get('sheets')



pprint(sheetList)

for sheet in sheetList :
    if sheet['properties']['title'] == 'Чаты для поиска клиентов':
        rows_count = sheet['properties']['gridProperties']['rowCount']

pprint(rows_count)


# Пример чтения файла
# values = service.spreadsheets().values().get(
#     spreadsheetId=spreadsheet_id,
#     range='A1:E10',
#     majorDimension='ROWS'
# ).execute()
# pprint(values)



addvertisement_chats = service.spreadsheets().values().get(
    spreadsheetId=spreadsheet_id,
    range='Чаты для поиска клиентов!A1:A100',
    majorDimension='ROWS'
).execute()['values']



# Пример записи в файл
# values = service.spreadsheets().values().batchUpdate(
#     spreadsheetId=spreadsheet_id,
#     body={
#         "valueInputOption": "USER_ENTERED",
#         "data": [
#             {"range": "B3:C4",
#              "majorDimension": "ROWS",
#              "values": [["This is B3", "This is C3"], ["This is B4", "This is C4"]]},
#             {"range": "D5:E6",
#              "majorDimension": "COLUMNS",
#              "values": [["This is D5", "This is D6"], ["This is E5", "=5+5"]]}
# 	]
#     }
# ).execute()

# values = service.spreadsheets().values().append(
#     spreadsheetId=spreadsheet_id,
#     range = "Клиенты!B1:L1",
#     valueInputOption = 'USER_ENTERED',
#     insertDataOption = 'INSERT_ROWS',
#     body = {
#           "majorDimension": "ROWS",
#           "values": [
#             ["Door", "$15", "2", "3/15/2016"],
#             ["Engine", "$100", "1", "3/20/2016"],
#           ],
#         }
# ).execute()