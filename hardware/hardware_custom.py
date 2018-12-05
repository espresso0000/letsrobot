import mod_utils
import os

# Example for adding custom code to the controller
module = None

def setup(robot_config):
    global module
    # Your custom setup code goes here
    
 

    # This code calls the default setup function for your hardware.
    module = mod_utils.import_module('hardware', robot_config.get('robot', 'type'))
    module.setup(robot_config)
    
def move(args):
    # Your custom command interpreter code goes here
    direction = args['command']
    if direction == 'FIRE':
        os.sytem("aplay -D plughw:2 /home/pi/sounds/firehorn.wav")
    if direction == 'BEED':
        os.system("aplay -D plughw:2 /home/pi/sounds/beedoo_minions.wav")
    if direction == 'FART':
        os.system("aplay -D plughw:2 /home/pi/sounds/fart-1.wav")    
    
    
    # This code calls the default command interpreter function for your hardware.
    module.move(args)
