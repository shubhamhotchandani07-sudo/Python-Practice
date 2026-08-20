#Create the following classes:

# Camera
# Create a method take_photo() that prints:
# "Taking a photo..."
# MusicPlayer
# Create a method play_music() that prints:
# "Playing music..."
# SmartPhone
# Inherit from both Camera and MusicPlayer.
# Create an additional method make_call() that prints:
# "Making a call..."
# Create an object of SmartPhone and use it to:
# Take a photo
# Play music
# Make a call

class camera:

    def take_photo(self):
        print("Taking a photo...")


class musicplayer():

    def play_music(self):
        print("Playing music...")


class smartPhone(camera,musicplayer):

    def make_call(self):
        camera.take_photo(self)
        musicplayer.play_music(self)
        print("Making a call...")

a=smartPhone()
a.make_call()