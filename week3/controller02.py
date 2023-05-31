from devices import *

def chosen(device, command):
    if device in command or device.replace(" ", "") in command:
        return True
    else:
        return False

def init_devices():
    light = Light()
    heating = Heating()
    player = MusicPlayer()

    devices = [light, heating, player]

    for dev in devices:
        print(f"{dev.name} has been initialised")
    
    return devices

def get_name():
    name = input("What is your name? ")
    print(f"Hello {name}")

    return name

def control_device(device, command):
    if ' on ' in command:
        device.turn_on()
    elif ' off ' in command:
        device.turn_off()
    elif ' up ' in command:
        device.increase()
    elif ' down ' in command:
        device.decrease()
    elif ' play ' in command and device.name == 'music player':
        device.play()
    elif ' pause ' in command and device.name == 'music player':
        device.pause()
    elif ' next ' in command and device.name == 'music player':
        device.change_next()
    elif ' previous ' in command and device.name == 'music player':
        device.change_previous()
    else:
        print("Sorry I do not understand the command")

def main_program(name, devices):
    while True:
        print()
        command = input(f"What next, {name}? ")
        command = f" {command.lower()} "

        if "system off" in command:
            break
        found = False
        for device in devices:
            if chosen(device.name, command):
                control_device(device, command)
                found = True
                break
        if not found:
            print(f"Sorry {name}, I do not understand that")
    
    print(f"Bye bye, {name}")


#### Main Program ####
devices = init_devices()
name = get_name()
main_program(name, devices)