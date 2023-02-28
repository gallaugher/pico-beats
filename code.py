# Idea based on original code by @todbot
# Modified (probably poorly) by Prof. John Gallaugher to include
# This version tested with CircuitPython v.8
import board, adafruit_mpr121, time, audiomixer, audiocore
from audiocore import WaveFile
from audiopwmio import PWMAudioOut as AudioOut


# Setup i2c on the Pico w/STEMMA_QT wired as shown in the diagram - GP4 (SDA/Blue), GP5 (SCL/Yellow, Power 3.3v(Out) Red
i2c = board.STEMMA_I2C() # Same for any board w/built-in STEMMA_QT port
touch_pad = adafruit_mpr121.MPR121(i2c)

# set up touchpads
touch_pad = adafruit_mpr121.MPR121(i2c)

# Coment out below if using the CircuitPlayground Bluefruit
# and be sure the board's pin is set to pin attached to tip of your audio plug.
audio = AudioOut(board.GP15) # I'm using GP15 for audio in. CHANGE if you use a different pin.

# Uncomment the 4 lines below of you're using a CircuitPlayground Bluefruit
# speaker = digitalio.DigitalInOut(board.SPEAKER_ENABLE)
# speaker.direction = digitalio.Direction.OUTPUT
# speaker.value = True
# audio = AudioOut(board.SPEAKER)

# Will be changed for microSD card lesson where we use larger files in a differently named folder/location
path = "slim_beats/" # This MUST be the name of the folder on CIRCUITPY, otherwise change as needed.

# MUST have 12 beats if using MPR121 touchpad breakout. Also make sure these 12 names match
# the files in your folder, named in the path, above. Otherwise modify the names.
beats = ["amen6.wav",
            "amenfull.wav",
            "ohohoh2.wav",
            "drum_loop.wav",
            "snappy_beats.wav",
            "hi_guitar.wav",
            "low_guitar.wav",
            "drum_cowbell.wav",
            "duck-scratch.wav",
            "freakie-freak.wav",
            "watch-this.wav",
            "yo.wav"]

# Should be 12 voices
num_voices = len(beats)

# create Mixer and attach to audio playback
# IMPORTANT: The "slim_beats" sounds were sampled at low-quality sample_rate=8000 so they could fit on the Pico.
# If you improve .wav quality, make sure you adjust the sample rate for any new sample rate.
# This will be changed when using version for microSD card in that lesson.
mixer = audiomixer.Mixer(voice_count=num_voices, sample_rate=8000, channel_count=1, bits_per_sample=16, samples_signed=True)
audio.play(mixer)

# read in all beats & simultaneously play them at audio sound .level = 0 (no volume)
for i in range(len(beats)):
    wave = audiocore.WaveFile(open(path+beats[i],"rb"))
    mixer.voice[i].play(wave, loop=True )
    mixer.voice[i].level = 0.0
time.sleep(1.0)  # let drums play a bit

while True:
    for i in range(len(beats)):
        if touch_pad[i].value:
            print(f"You touched pad # {i}!")
            mixer.voice[i].level = 1.0 # When touched, increase to full volume
        else:
            mixer.voice[i].level = 0.0 # No touch, then set volume back to zero
