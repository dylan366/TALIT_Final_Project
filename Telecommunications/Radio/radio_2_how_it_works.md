## How It Works
A radio system only needs two essential parts: a transmitter and a receiver. 
- The transmitter creates radio waves and encodes them with the data we want to send — for example, spoken words or Morse code.
- The receiver captures those waves and decodes the information.
- The decoded signal is then sent to an output device such as a loudspeaker, headphones, or even a screen.
- 
This is a very simplified view — we’ll dive into the details later. For now, let’s start with the basics of radio waves themselves.

As the name suggests, radios use radio waves to communicate. Radio waves are part of the electromagnetic spectrum, the same family of waves that includes X-rays (used in medical imaging), gamma rays (from radioactive sources), infrared light (heat), and visible light (what our eyes can detect).
In fact, visible light is just another kind of electromagnetic wave, but with much shorter wavelengths - between about 380 and 700 nanometres. Radio waves have much longer wavelengths, sometimes many meters long. Because of that, they can travel much farther than visible light, but our eyes can’t detect them. If our vision were tuned differently, we might literally see radio broadcasts around us.

On their own, plain radio waves don’t carry useful information, they’re just a wave in the electromagnetic field. To send data, we have to modulate them, that is, change some property of the wave in a controlled way.
There are two main approaches:
- Amplitude Modulation (AM): The height (amplitude) of the wave is varied while the frequency stays constant.
- Frequency Modulation (FM): The frequency of the wave changes while the amplitude stays constant.

The names "AM radio" and "FM radio" come from these methods. In this project, we’ll focus on AM, because it’s simpler to build with basic components. My homemade radio could only transmit Morse code reliably, and only faintly transmit louder sounds like blowing into a microphone.

## Radio transmission
The radio transmitter is the part of a radio system that does the following things:
- Create a stable, constant wave without any changes - just the wave nothing else
- Connect to an input device that gives the information that needs to be sent
- Takes the information and manipulates the stable wave with it, encoding the wave with data.

Creating a wave is easy. As the name suggests (electromagnetic wave), we need to somehow create changing electric fields and magnetic fields and in combination these two propagate a combined wave. The device to create an electromagnetic wave is called an oscillator. This name just means "back and forth" because that's what a wave, and the current in the circuit, do. This constant back-and-forth changing causes constant changes in electric and magnetic fields, hence creating a wave. The simplest oscillator is called an LC oscillator (L for inductance and C for capacitance) shown here:

Charging up the capacitor beforehand creates an electric field within. Upon closing the circuit, the current from the capacitor enters the inductor from one end, creating a magnetic field. This magnetic field in turn influences the electric field and therefore increases the electric field energy inside the capacitor. Now we're back at square one and this all (capacitor empties and electric field energy increases -> inductor fills up and magnetic field increases, electric field decreases -> electric field increases, magnet field decreases -> inductor empties, capacitor fills up), repeats until all energy is expended. This simple oscillator doesn't build up or anything, which means that due to resistance the waves get smaller and smaller after each turn and die out after some time. 

Using transistors we can rebuild the waves and have a true steady wave, though this requires additional power supply.

Now, using this created wave we can take some input wave (which is the information we want to send) and encode the carrier wave with the input wave. The wave created will be the wave that gets propagated through the air towards the receiver. 


