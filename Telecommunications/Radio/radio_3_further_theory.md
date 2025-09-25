## My own Radio
Now that we understand the basics of transmitters and receivers, let's look at how I actually built my own small radio system
To keep it simple, in my system you can transmit morse code (a system of clicking noises in this case). 

To send Morse code wirelessly, I needed three things:  
- A source of radio waves (the oscillator / function generator)  
- A way to switch those waves on and off (the button for dots and dashes)  
- An antenna to send the waves into the air to my receiver

## Antennas
There are many different types of antenna. The two common ones are:
- **Monopole antenna (straight wire):** A simple metal rod or wire sticking up from the transmitter. It reaches peak efficiency when its size is that of a quarter of the carrier wave length. At 1 MHz, the wavelength is about 300 meters, so a quarter would be 75 meters (using the $c=\lambda f$ formula). Obviously I do not have the possibility to build a 75 meter high antenna.
- **Loop (or coil) antenna:** A wire bent into a loop, often with many turns. Instead of mainly radiating electric fields like a monopole, the loop produces strong magnetic fields nearby (called near-field). This works great over very short distances.
  
Because I wanted to build a radio system to just demonstrate all of this on one table, a loop antenna is the perfect option here.

## Coil Antenna