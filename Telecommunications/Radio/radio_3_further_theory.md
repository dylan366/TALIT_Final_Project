## Further Theory for later
Now that we understand the basics of transmitters and receivers, let's look at how I actually built my own small radio system
To keep it simple, in my system you can transmit morse code (a system of clicking noises in this case). 

To send Morse code wirelessly, I needed three things:  
- A source of radio waves (the oscillator / function generator)  
- A way to switch those waves on and off (the button for dots and dashes)  
- An antenna to send the waves into the air to my receiver

## Antennas
There are many different types of antenna. The two common ones are:
- **Monopole antenna (straight wire):** A simple metal rod or wire sticking up from the transmitter. It reaches peak efficiency when its size is that of a quarter of the carrier wave length. At 1 MHz, the wavelength is about 300 meters, so a quarter would be 75 meters (using the $c=\lambda f$ formula). Clearly I do not have the possibility to build a 75-meter-high antenna.
- **Loop (or coil) antenna:** A wire bent into a loop, often with many turns. Instead of mainly radiating electric fields like a monopole, the loop produces strong magnetic fields nearby (called near-field). This works great over very short distances, but the antenna strength quickly becomes very weak over even just a few meters. Unlike a big antenna that can radiate far-field electromagnetic waves, my loop only produces strong magnetic fields in the near-field region. That’s why my demo works well across a table, but not across a city.
  
Because I wanted to build a radio system to demonstrate all of this on just one table, a loop antenna is the perfect option here.

## Loop (Coil) Antenna
- A wire carrying a current (current meaning a moving charge -> changing electric field) generates a magnetic field. 
- Turning this wire into a loop makes the magnetic field get stronger.
- If the current alternates (as with oscillating current), the magnetic field from the loop also goes back and forth.
- This alternating magnetic field creates current in another metal object (for example, a radio receiver antenna).

Since the magnetic field alternates anyway, the antenna doesn't have a "side". 
The radiation is strongest in the plane of the loop (to their sides, not facing the hole), while directly along the axis (through the hole) the signal is very weak. This is because the fields from different parts of the loop cancel in that direction. A loop antenna has a doughnut-shaped radiation pattern.

This means that the loop is acting like a **transformer without the iron core**.

The inductance of a coil antenna (inductance because all it really is, is a bigger inductor, since it also creates magnetic fields) can be calculated with this formula:
$L= N^2\mu_0D(\ln{\frac{8D}{r}}-2)$
where:
- $L$ is the inductance of the loop in Henries (H)
- $N$ is the number of turns
- $\mu_0$ is the permeability of free space $(=4\pi \cdot 10^{-7} H/m)$
- $D$ is the diameter of the coil
- $r$ is the radius of the wire

This formula is an approximation for a thin-wire, air-core loop. In practice, exact values are different, but it’s good enough to predict the resonance frequency with the LC formula from before.

The size of the loop and the number of turns determine how strong the magnetic field is in the near-field, and therefore how well the signal is picked up. Most importantly is, that $L$ and $C$ together set the resonant frequency $f$ from the LC formula.

Now that we know how loop antennas behave, let’s look at how I built my own coil and connected it to my function generator to send Morse code across a table.

## Special Modulation
Finally, we learned about AM and FM, but these are for transmitting actual data like voice input or other types of stuff. How would modulation work if we just wanted to use the radio like a telegraph?

### Amplitude Shift Keying (ASK)
If we want to just use a radio like a wireless telegraph (with a button), then the input won't be a really complicated wave as with voice input, but it will be an almost square wave. As an example, see (a) in the image below. When the button is pressed, current flows (equals 1), but if the button isn't pressed, then there is no current, so 0. The longer you press on a button, the longer the current signal. In a telegraph, this would equal to a longer beep or a longer break between two sounds. 
Modulating such a simple wave onto a carrier wave is an incredibly easy modulation technique. One possibility is to just entirely only let the carrier wave through when the button is pressed, and to cut it off from the transmitting antenna when the button isn't pressed. This is called On-Off-Keying, or OOK for short (see on image c). 
Simple:
- Button pressed -> Transmit the carrier wave without any changes to it
- Button not pressed -> cut the carrier wave off from the antenna, so nothing gets propagated.
<img src="images_script\tm355_bk1_pt2_f018.eps.jpg" width="300"> 
The (d) is known as binary amplitude-shift keying (BASK) and uses the exact same principle, just a 0 isn't no wave, but just a smaller wave. This means that the carrier wave never gets cut off from the antenna, but rather just lowers its amplitude until the next button press.
On a radio, when transmitting with OOK, since the wave doesn't actually carry any date, all we hear is static going on and off. Short static. Silence. Long static. That's it. 
In BASK, you only hear static, but its volume goes up with pressing a button. Static. Long loud static. Static. Short loud static. Simple as that.