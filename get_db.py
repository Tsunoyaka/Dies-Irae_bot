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


