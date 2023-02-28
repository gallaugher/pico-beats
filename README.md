# pico-beats
Simulate a DJ Board with a Raspberry Pi Pico, MPR121 12-pad Capacitive Touch board, and CircuitPython

This also uses "slim_beats" folder that you can download at: https://bit.ly/circuitpython-school-files

Mix breakbeats with an Adafruit mpr121 12 key capacitive touch sensor. https://www.adafruit.com/product/4830

Original code & beats files provided by @todbot. Thx for sharing your code & helping me learn! Check out his repo for some slick code examples at: https://github.com/todbot/circuitpython-tricks/tree/main/larger-tricks

My example uses a Raspberry Pi Pico W (same wiring for plain Pico) wired as below:
<img width="980" alt="pico stemma audio diagram" src="https://user-images.githubusercontent.com/20801687/221918995-33564c58-bb4b-43dc-88bb-013e9897aa3a.png">

Assumption is that you're using a speaker that has separate power. I used a Hamburger-style speaker that you can get from Amazon, Walmart, or SparkFun.

If you are modifying the code and using different files, BE SURE
- that your path variable is set equal to the same folder name that holds audio files on your pico.
- that your 12 file names (including .wav extension) are properly named in the beats list in the code.
- that the mixer = audiomixer.Mixer line has the proper sample_rate

NOTE: To those who are using this example after viewing the lesson where we add a microSD card for more storage on the pic, you have differnet lines for all three examples above. These are mentioned in that lesson.
