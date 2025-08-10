## How it works
A radio only needs two things: A transmitter and a receiver. A transmittor creates radio waves and encodes them with the data we want to send, for example a song. The receiver catches these waves and decodes the information. The receiver is then connected to an output device which can then show us the message in the waves. Some output devices include loudspeakers, headphones or screens. This is of course worded very simply and we will go into more detail later.
To understand how a radio works, I will explain both the transmitter and receiver seperately in two seperate pages. Like that I will also combine the theory with the calculations behind it, as seperating these two would overcomplicate things. But first, I will give a quick introduction to radio waves.

A radio uses, as the name suggests, radio waves to communicate. Radio waves are waves within the electromagnetic spectrum, just like x-xray waves in medical devices, gamma waves in radiation, or visible light waves, which allow us to see the world. That's right, light, how we see it, is on the exact spectrum as the waves used during a phone call. Had our eyes evolved differently, we could see these radio waves too. But our eyes can only detect waves with the wavelength between 380 to 700 nanometres. Radiowaves have the wave length of many metres and reach much further, but therefore can't be detected by such a fragile organ like the human eye. 

These radio waves get manipulated, either by constantly changing the frequency or by constantly changing the amplitude of the wave, to send information. We will look at this system right now, but we will keep it at a basic level, as the radio I built could only send morse-code anyway, and could barely send louder things like my voice. 

## Radio transmission
The radio transmitter is the part of a radio system that does the following things:
- Create a stable, constant wave without any changes - just the wave nothing else
- Connect to an input device that gives the information that needs to be sent
- Takes the information and manipulates the stable wave with it, encoding the wave with data.

Creating a wave is easy. As the name suggests (electromagnetic wave), we need to somehow create changing electric fields and magnetic fields and in combination these two propagate a combined wave. The device to create an electromagnetic wave is called an oscillator. This name just means "back and forth" because that's what a wave, and the current in the circuit, do. This constant back-and-forth changing causes constant changes in electric and magnetic fields, hence creating a wave. The simplest oscillator is called an LC oscillator (L for inductance and C for capacitance) shown here:

Charging up the capacitor beforehand creates an electric field within. Upon closing the circuit, the current from the capacitor enters the inductor from one end, creating a magnetic field. This magnetic field in turn influences the electric field and therefore increases the electric field energy inside the capacitor. Now we're back at square one and this all (capacitor empties and electric field energy increases -> inductor fills up and magnetic field increases, electric field decreases -> electric field increases, magnet field decreases -> inductor empties, capacitor fills up), repeats until all energy is expended. This simple oscillator doesn't build up or anything, which means that due to resistance the waves get smaller and smaller after each turn and die out after some time. 

Using transistors we can rebuild the waves and have a true steady wave, though this requires additional power supply.

Now, using this created wave we can take some input wave (which is the information we want to send) and encode the carrier wave with the input wave. The wave created will be the wave that gets propagated through the air towards the receiver. 


