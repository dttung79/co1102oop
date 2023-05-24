import database01 as db

names = db.get_names()
user_ids = db.get_user_ids()
infos = db.get_infos()

def print_user_details(names, user_ids, infos):
    for i in range(len(names)):
        name = names[i]
        user_id = user_ids[i]
        info = infos[i]
        print(f"name:      {name}")
        if user_id is not None:
            print(f"user id:   {user_id}")
        if info is not None:
            if info.startswith("BSc ") or info.startswith("MSc "):  # this is a student
                print(f"programme: {info}")
            else:  # this is a member of staff
                print(f"job title: {info}")
        print()

# def is_send(info, group):
#     send_message = False
#     if group == "all":
#         send_message = True
#     elif info is not None:
#         is_student = info.startswith("BSc ") or info.startswith("MSc ")
#         if group == "students" and is_student:
#             send_message = True
#         if group == "staff" and not is_student:
#             send_message = True
    
#     return send_message
def is_send(name):
    if name not in names:
        print(f'{name} not found!')
        return False
    if user_ids[names.index(name)] is None:
        print(f'{name} is guest! Message not sent')
        return False
    return True
def send_messages(names, infos):
    while True:
        name = input("Name? ")
        if is_send(name):
            message = input("Message? ")
            if message == 'exit':
                print('System exit')
                break
            elif message != "":
                print(f"Message sent to {name}")
            else:
                print("Empty message not sent")

## MAIN PROGRAMS
print_user_details(names, user_ids, infos)
send_messages(names, infos)