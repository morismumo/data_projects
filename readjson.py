import json

with open('data.json','r') as f:
    data = json.load(f)

    print('-'*30)
    print(data['records'][:2])

    print('-'*30)
    print(data['records'][0]['name'])

    print('-'*30)
