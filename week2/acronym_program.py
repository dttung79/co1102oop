# Write a program that asks user to enter an acronym and then prints out the words represented by the acronym then loops back and asks for another acronym
# The program will stop when the user enters "exit" (without quotes) instead of an acronym
# The program will print all the acronyms and their meanings if user enters "." (without quotes) instead of an acronym
# If an acronym is not existed, the program will ask if the user wants to add it to the dictionary and if user chooses yes, the program will ask for the meaning of the acronym and add it to the dictionary
# Output example:
# Enter an acronym: IP
# IP stands for Internet Protocol
# Enter an acronym: DNS
# DNS stands for Domain Name System
# Enter an acronym: .
# IP stands for Internet Protocol
# DNS stands for Domain Name System
# RAM stands for Random Access Memory
# Enter an acronym: ROM
# ROM is not in the dictionary. Do you want to add it? (y/n) y
# Enter the meaning of ROM: Read Only Memory
# Enter an acronym: ROM
# ROM stands for Read Only Memory
# Enter an acronym: exit
# Goodbye!

acronyms_dict = {'IP': 'Internet Protocol', 'RAM': 'Random Access Memory', 'CPU': 'Central Processing Unit', 'ROM': 'Read Only Memory', 'DNS': 'Domain Name System'}

running = True
while running:
    acronym = input('Enter an acronym: ').upper()
    if acronym == '.':
        for a in acronyms_dict:
            print(a, 'stands for', acronyms_dict[a])
    elif acronym.lower() == 'exit':
        print('Goodbye!')
        running = False
    elif acronym in acronyms_dict:
        print(acronym, 'stands for', acronyms_dict[acronym])
    else:
        print(acronym, 'is not in the dictionary.', end=' ')
        add = input('Do you want to add it? (y/n) ')
        if add.lower() == 'y':
            meaning = input(f'Enter the meaning of {acronym}: ')
            acronyms_dict[acronym] = meaning
            print(acronym, 'stands for', meaning)