list_db = []

def read_db(path: str) -> list:
    global list_db
    with open(path, 'r', encoding='UTF-8') as file:
        my_list = file.readlines()
        for line in my_list:
            dict_id = dict()
            line = line.strip().split(';')
            dict_id['lastname'] = line[0]
            dict_id['firstname'] = line[1]
            dict_id['phone'] = line[2]
            dict_id['comment'] = line[3]
            list_db.append(dict_id)