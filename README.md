# pico-beats
Simulate a DJ Board with a Raspberry Pi Pico, MPR121 12-pad Capacitive Touch board, and CircuitPython

Mix breakbeats with an Adafruit mpr121 12 key capacitive touch sensor. https://www.adafruit.com/product/4830

Original code & beats files provided by @todbot. Thx for sharing your code & helping me learn! Check out his repo for some slick code examples at: https://github.com/todbot/circuitpython-tricks/tree/main/larger-tricks

My example uses a Raspberry Pi Pico W (same wiring for plain Pico) wired as below:


BUT I've had problems running on RP2040 processors (also tried on a QT Py RP2040). I found Mu regularly dropped the board & then the board couldn't connect as CIRCUITPY, so I had to do a complete re-install of CircuitPython to get things working again. Frustrating.

I had much mroe reliable success with a CircuitPlayground Bluefruit. See comments in code for minor changes. For wiring for the CPB, connect I2C of STEMMA-QT cabling as follows:

Black to GND
Red to 3.3v (not VOUT)
Blue to A5 (also labeled SDA)
Yellow to A4 (also labeled SCL)
Clip two alligator clips to the RCA jack as shown above.

Sleeve base of audio plug should connect to pad GND
Tip of audo plug should connect to AUDIO. Assumption is that you're using a speaker that has separate power. I used a Hamburger-style speaker that you can get from Amazon, Walmart, or SparkFun.
