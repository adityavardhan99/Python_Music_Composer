#		python code
#		script_name: my_music_compose
#
#		author: Aditya Vardhan Thakur
#		description: Composition Practice
#       Set up

from earsketch import * # tells DAW to get ready to make music

init() # this function means initialize or begun the DAW
setTempo(120) # The set tempo() function allows you to choose how fast or slow you want your song to be played.
# Music
chord = RD_UK_HOUSE__5THCHORD_2
secondaryBeat = HIPHOP_BASSSUB_001
mainBeat = HOUSE_MAIN_BEAT_003

fitMedia(chord, 1, 1, 16)
# Add effect between measures 1 and 16 moving from -60db to 5db and back down
setEffect(1, VOLUME, GAIN, -60, 1, 5, 12)
setEffect(1, VOLUME, GAIN, 5, 12, -60, 16)

fitMedia(secondaryBeat, 2, 1, 12)
# Add effect
setEffect(2, DELAY, DELAY_TIME, 500)
fitMedia(mainBeat, 3, 1, 8)

# Add effcet
setEffect(3, REVERB, REVERB_TIME, 200)

# Finish


finish()
