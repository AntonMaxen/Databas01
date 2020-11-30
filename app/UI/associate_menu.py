from app.UI.menus import menu
import app.BL.associates_controller as ac
import app.BL.contact_person_controller as cpc
from app.UI.ui_functions import f_input, print_amount_matches, divider, print_list_of_tablerows, print_tablerow


def show_all_associates():
    associates = ac.show_all_associates()
    print_list_of_tablerows(associates)
    print_amount_matches(associates)


def show_associate_by_id():
    print("Enter an Associate Id")
    a_id = f_input()
    associate = ac.show_associate_by_id(a_id)

    if associate:
        print_tablerow(associate)
        cp_id = associate.contact_person_id
        print(f'Do you want to show >{associate.name}s< contact person?\n'
              '1: Yes\n'
              '2: No')
        if int(f_input()) == 1:
            contact_person = cpc.show_cp_by_id(cp_id)
            print_tablerow(contact_person)

        else:
            return


def search_associates_menu():
    ass_column = ac.get_columns()

    def inner(column):
        return lambda: show_associate_by_columnvalue(column)

    menu({str(i+1): {"info": a, "func": inner(a)} for i, a in enumerate(ass_column[0:-1])})


def show_associate_by_columnvalue(column_name):
    print(f"enter searchvalue for {column_name}")
    name = f_input()
    associate = ac.get_associate_by_columnvalue(column_name, name)
    print_list_of_tablerows(associate)
    print_amount_matches(associate)


def update_associate():
    print("enter an Associate id: ")
    a_id = f_input()
    associate = ac.show_associate_by_id(a_id)
    ass_column = ac.get_columns()

    def inner(column, associate):

        return lambda: update_associate_column(column, associate)

    menu({str(i + 1): {"info": a, "func": inner(a, associate)} for i, a in enumerate(ass_column[0:-1])})


def update_associate_column(column, associate):
    print("Enter new value: ")
    value = f_input()
    ac.update_associate_column(associate, column, value)
    print_tablerow(associate)


def add_associate():
    insert_dict = {}
    for column in ac.get_columns():
        if column != "id":
            insert_dict[column] = input(f'{column}: ')
            if column == 'contact_person_id':
                contact_person = create_contact_person()
                insert_dict[column] = contact_person.id

    divider()
    associate = ac.add_associate(insert_dict)
    if associate:
        print_tablerow(associate)


def drop_associate_by_id():
    print("Enter an Associate id to delete Associate")
    a_id = int(f_input())
    associate = ac.show_associate_by_id(a_id)
    cp_id = associate.contact_person_id
    print('Do you want to delete contact person as well?\n'
          '1: Yes\n'
          '2: No')
    if int(f_input()) == 1:
        ac.drop_associate(a_id)
        cpc.drop_cp(cp_id)
        print(f'Successfully deleted {associate.name} & contact person')
        print('========================================================')
    elif int(f_input()) == 2:
        ac.drop_associate(a_id)
        print(f'Successfully deleted {associate.name}')
    else:
        return


def create_contact_person():
    print('Add contact persons information')
    print('===============================')
    insert_dict = {}
    for column in cpc.get_columns():
        if column != "id":
            insert_dict[column] = input(f'{column}: ')

    contact_person = cpc.add_cp(insert_dict)
    if contact_person:
        print_tablerow(contact_person)

    return contact_person


def update_contact_person():
    print("enter an Associate id: ")
    a_id = f_input()
    associate = ac.show_associate_by_id(a_id)
    cp_id = associate.contact_person_id
    contact_person = cpc.show_cp_by_id(cp_id)

    def inner(column, contact_person):
        return lambda: update_contact_person_column(column, contact_person)

    menu({str(i + 1): {"info": cp, "func": inner(cp, contact_person)} for i, cp in enumerate(cpc.get_columns())})


def update_contact_person_column(column, contact_person):
    print("Enter new value: ")
    value = f_input()
    cpc.update_cp_column(contact_person, column, value)
    print_tablerow(contact_person)


def drop_contact_person():
    print("Enter an Contact Persons id to delete that Contact Person")
    cp_id = int(f_input())
    cpc.drop_cp(cp_id)


def update_menu():
    menu({
        "1": {
            "info": "update associate",
            "func": update_associate,
        },
        "2": {
            "info": "update contact person",
            "func": update_contact_person,
        }
    })



def associate_menu():
    menu({
        "1": {
            "info": "show all associates",
            "func": show_all_associates
        },
        "2": {
            "info": "show associate by id",
            "func": show_associate_by_id

        },
        "3": {
            "info": "search associate",
            "func": search_associates_menu
        },
        "4": {
            "info": "update an associate or contact person by id and column",
            "func": update_menu
        },
        "5": {
            "info": "add an associate",
            "func": add_associate
        },
        "6": {
            "info": "delete associate by id",
            "func": drop_associate_by_id
        }
    })


if __name__ == '__main__':
    associate_menu()
