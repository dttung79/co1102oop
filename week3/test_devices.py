from devices import Light, Heating, MusicPlayer

celling_light = Light() # call the constructor of class Light to create an object

# access object's attributes
print(f'Name of the light: {celling_light.name}')
print(f'Status of the light: {celling_light.status}')
print(f'Settings of the light: {celling_light.settings}')
print(f'Setting type of the light: {celling_light.setting_type}')

# tell the object todo something based on its behaviours
celling_light.turn_on()
celling_light.increase()
celling_light.decrease()
celling_light.turn_off()

# create object of MusicPlayer
ipod = MusicPlayer()
ipod.play()
ipod.pause()
ipod.change_next()
ipod.change_next()
ipod.turn_off()