## My own Radio
Now that we have learned quite a bit of the basics, we have enough theory to be able to build our very own radio transmitter. In this chapter, we will look at how I built my own functioning radio system, including a very simple tutorial for you to follow.

As we learned, for this project a loop antenna is ideal, since I just want to send morse code (on-off switching) across a table. 

But first things first, in all radio transmitters, we need a carrier wave. I could have made a stable oscillator myself, but there are a few reasons why I didn't:
- expensive (transistors and many other parts)
- too big (would have taken much more space)
- no guarantee that it would be stable

For that reason, I decided to buy a wave generator kit off AliExpress for less than a Franc. The Kit was a self-build kit, coming with all the parts, instructions, and a schematic circuit of both the kit and the integrated circuit. The finished product used a maximum of 12 Volts DC, and you could select the frequency range between 1 Hz and 1 MHz. Within those ranges, you had 3 knobs to tune the wave finely or coarsely, and also to change the amplitude.  

## Parts list for the whole transmitter
- Function generator Kit with XR2206
- 2x 1 meter of cable
- tools such as small cross screwdrivers, soldering station, 
- 9V to max 12V stable power source (I used a 9V battery and it worked fine)
  
- about 4.5meters of 1mm thick insulated copper wire
- a breadboard
- 4 pins (see image)
- 4 pin holders (see image)
- a button
- an LED
- a switch
- 2x 220 Ohm resistors
- some smaller cables
- a radio that has AM (I bought the Panasonic RF-2400D and it worked perfectly)
- sticky tape
<img src="images_tutorial\battery_image.jpg" width="200">

## Instructions:
#### Carrier wave generator:
1. Build the function generator kit according to the instructions it comes with. I have uploaded the same instructions here in case it didn't come with one.
<img src="images_tutorial\function_generator_schematic.jpg" width="300">
<img src="images_tutorial\function_generator_finished.jpg" width="200">

1. Take the two long cables. Open up the screws of the GND output (Top one on the blue box) and the SIN output (bottom one) on the generator. The middle output is for square waves, but we don't need that.
2. Trim the two cables and solder each end for better connection.
3. Put on cable on the SIN output, and the other cable in the GND output. Close the screws tightly and make sure the cables won't fall out.
<img src="images_tutorial\function_generator_cables.jpg" width="200">

1. On the other ends of the two cables, solder a pin on each.
<img src="images_tutorial\function_generator_pins.jpg" width="200">

1. Now you should be left with the generator and a long cable with a pin at the end coming out of the SIN output and another long cable coming out of the GND (also with a pin at the other end).
<img src="images_tutorial\function_generator_complete.jpg" width="200">

#### Coil antenna
<img src="images_tutorial\loop_antenna_finished.jpg" width="200">

1. Take the other very long wire (1mm thick)
2. Wound it up into a circle with a diameter of about 14cm (mine had 10 turns)
<img src="images_tutorial\loop_antenna_size.jpg" width="200">

3. Make sure the two ends are about just 1 or 2 cm apart and stable
4. Stabilize the whole antenna by putting tape onto it
5. Hold the two ends in place also using tape
<img src="images_tutorial\loop_antenna_tape.jpg" width="200">

6. Solder a pin onto each end so that the antenna can be taken away
7. NOTE: The antenna has no direction since we are using alternating current. Therefore it doesn't matter which way you connect the loop to the rest of the transmitter
#### Button breadboard
1. Solder the pin inputs on the positive line, the negative line, and then two pin inputs on one side oppposite eachother (this is where the antenna will go, so check that the distance is about right)
If unclear, I used pins and pin inputs so that the entire thing is detachable and not permanent. This makes for easier transport and storage.
2. Solder the button to the breadboard. One side is connected with a cable to the positive line. The other side diagonal to the first on is connected to one of the pins where the loop coil will go.
3. Connect the other pin where the loop coil goes to the ground of the breadboard.
<img src="images_tutorial\breadboard_top.jpg" width="200">
<img src="images_tutorial\breadboard_side.jpg" 
width="200">
<img src="images_tutorial\breadboard_size.jpg" width="200">

##### Optional
I added a switch with an LED to it as a help to see if the function generator is even on. Note that this LED will not work if the coil is connected, as the current will rather go through the coil than through the LED (less resistance). This LED part is more just a debug but nontheless quite useful.

1. Connect the unused side of the button next to the one going to the coil with the left pin of the switch. 
2. From the middle pin, connect two resistors in series (after each other).
3. Connect the LED. Look out for the polarity.
4. Connect the GND pin of the LED to the ground of the breadboard.
5. The right pin of the switch isn't connected to anything. This means that the switch is off when it is on that side.
6. ATTENTION: Make sure that nothing overlaps with anything. On breadboard, vertical lines of holes are all connected to eachother (in groups of five basically) so if you solder anything with the LED's onto a line where for example a button is soldered, it will connect! 

#### Finished
Now we've built all components needed for a radio transmitter: The carrier wave generator, the antenna, and a way to On-Off-Key. Let's get all of this together and make it work!

## Completing the Radio Transmitter
1. Take all the assembled parts (power supply, function generator, antenna, breadboard)
<img src="images_tutorial\all_built_pieces.jpg" width="200">

2. Connect the SIN output cable pin into the pin input on the positive line of the breadboard. (red line)
<img src="images_tutorial\red_connected.jpg" width="200">

3. Connect the GND output cable pin into the pin on the negative line of the breadboard. (blue line)
<img src="images_tutorial\black_connected.jpg" width="200">

4. Make sure the switch is off (on the right)
<img src="images_tutorial\switch_off_right.jpg" width="200">

5. Connect the antenna into both pin holders
<img src="images_tutorial\antenna_connected.jpg" width="200">

6. Set the green connector on the generator to the range 65K-1MHZ (the top one)
<img src="images_tutorial\green_pins_settings.jpg" width="200">

7. Connect the other green connector across the Sin description (see previous image)

8. Turn the Fine and Coarse knobs to their maximums (clockwise until it stops)
<img src="images_tutorial\knob_settings.jpg" width="200">

9.  Turn the knob for the Amplitude all the way down (anti-clockwise until stops) (previous image)

10. Power the function generator with your battery or other power source. Again, check that the voltage is maximum 12V. From this point on, your setup will start radiating.
<img src="images_tutorial\power_setup.jpg" width="200">

## Connecting with your Radio Receiver
1. Turn on your radio.
2. Turn the radio to AM
3. Go a few meters away from electronics such as your laptop, phone, TV, lights and LED lights, light switches, etc... These will otherwise interfere.
4. Have your antenna maybe 20 or 30 centimetres away from the radio.
5. Press down on the button without taking your finger off and slowly tune the radio in the range 1MHz to 1.3MHz until the static suddenly gets really loud. Now you have found your signal.
6. Take your finger off the button and press on it a few times to really make sure you've found your frequency. To confirm, you should be hearing the button clicks on the radio, or the static becoming louder with every press.
7. If this is the case, take your antenna and kit away from the radio - constantly clicking on the button - until you can't hear the changes on the radio any more. This can be the case anywhere between a few centimetres to 3 or 4 meters.
8. Great job! You have created your own radio system and can now send morse code wirelessly across a short distance!
   
On my GitHub, you can find a video demonstrating how it could sound. 