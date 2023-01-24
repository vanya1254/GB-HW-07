from model import read_db, list_db
from view import main_menu, show_all, exit_program, db_success, create_contact


def input_handler(inp: int):
    match inp:
        case 1:
            show_all(list_db)
        case 2:
            read_db('database.txt')
            db_success(list_db)
        case 4:
            list_db.append(create_contact())
        case 7:
            exit_program()
            

def start():
    while True:
        user_choice = main_menu()
        input_handler(user_choice)