# Declare the class Light
class Light:
    # Define a constructor to initialize objects of this class
    # Inside the constructor, initialize the attributes name, status, settings, and setting_type
    def __init__(self):
        self.name = 'ceiling light'
        self.status = False
        self.settings = 350
        self.setting_type = 'brightness'
    
    def turn_on(self):
        self.status = True
        print(f'{self.name} is on')

    def turn_off(self):
        self.status = False
        print(f'{self.name} is off')
    
    def increase(self):
        self.settings += 1
        print(f'{self.name} {self.setting_type} is set to {self.settings}')
    
    def decrease(self):
        self.settings -= 1
        print(f'{self.name} {self.setting_type} is set to {self.settings}')

class Heating:
    def __init__(self):
        self.name = 'heating'
        self.status = False
        self.settings = 350
        self.setting_type = 'temperature'
    
    def turn_on(self):
        self.status = True
        print(f'{self.name} is on')

    def turn_off(self):
        self.status = False
        print(f'{self.name} is off')
    
    def increase(self):
        self.settings += 1
        print(f'{self.name} {self.setting_type} is set to {self.settings}')
    
    def decrease(self):
        self.settings -= 1
        print(f'{self.name} {self.setting_type} is set to {self.settings}')

class MusicPlayer:
    def __init__(self):
        self.name = 'music player'
        self.status = False
        self.settings = 350
        self.setting_type = 'volume'
        self.songs = ['Change', 'Wake of Magellan', 'The Hourglass', 'King of Metal', 'Desert Rose', 'The Final Countdown']
        self.current_song = 0
    
    def play(self):
        print(f'{self.name} is playing {self.songs[self.current_song]}')
    
    def pause(self):
        print(f'{self.name} is paused')
    
    def change_next(self):
        self.current_song += 1
        if self.current_song >= len(self.songs):
            self.current_song = 0
        print(f'{self.name} is playing {self.songs[self.current_song]}')
    
    def change_previous(self):
        self.current_song = (self.current_song - 1) % len(self.songs)
        print(f'{self.name} is playing {self.songs[self.current_song]}')
    
    def turn_on(self):
        self.status = True
        print(f'{self.name} is on')

    def turn_off(self):
        self.status = False
        print(f'{self.name} is off')
    
    def increase(self):
        self.settings += 1
        print(f'{self.name} {self.setting_type} is set to {self.settings}')
    
    def decrease(self):
        self.settings -= 1
        print(f'{self.name} {self.setting_type} is set to {self.settings}')