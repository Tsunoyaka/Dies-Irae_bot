import json

def get_db(db):
    with open(f'JSON/{db}.json', 'r') as file:
        return json.load(file)

def write_db(db,data):
    with open(f'JSON/{db}.json', 'w') as file:
        json.dump(data, file, indent=4, ensure_ascii=False)

def get_photo_yazata(id):
    with open(f'gods/Yazata/{id}.jpg', 'rb') as f:
        return f.read()

def get_photo_evil_kings(id):
    with open(f'gods/Evil_Kings/{id}.jpg', 'rb') as f:
        return f.read()

def get_photo(id): 
    with open(f'gods/Gods/{id}.jpg', 'rb') as f:
        return f.read()


def get_album(db):
    with open(f'MUSIC/{db}.json', 'r') as file:
        return json.load(file)

def get_id(message):
    user_id = message.chat.id
    data = get_db('my_users')
    for id_ in data:
        if id_['chat_id'] == user_id:
            return id_


def get_user():
    with open(f'JSON/my_users.json', 'rb') as file:
        return file.read()