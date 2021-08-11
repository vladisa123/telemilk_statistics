import requests

# Все файлы которые задеплоили лежат на рабочем столе в папке телемилк




# def lambda_handler(event,context):

headers = {
    'InvocationType' : 'Event'
}

# try:
r = requests.get("https://nqbg6odxhk.execute-api.us-east-2.amazonaws.com/v0/user?id=1461355505", headers = headers )

print('Response ', r)
    # except:
    #     pass

    # return {"location": 'https://telemilk.ru/'}

# https://jt2qxn4n7l.execute-api.us-east-2.amazonaws.com/v1/user?id=1224378215