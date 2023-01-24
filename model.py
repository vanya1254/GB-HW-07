list_db = []


def get_db():
    global list_db
    return list_db
    

def set_db(data: dict):
    global list_db
    list_db.append(data)


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
            

def save_db(path: str):
    global list_db
    with open(path, 'w', encoding='UTF-8') as file:
        for i in range(len(list_db)):
            for v in list_db[i].values():
                if list_db[i]['comment'] != v:
                    temp = v + ';'
                    file.writelines(temp)
                else:
                    temp = v
                    file.writelines(temp)
            file.writelines('\n')