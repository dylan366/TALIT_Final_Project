import sys
print(sys.executable)
import matplotlib.pyplot as plt
import schemdraw
import schemdraw.elements as elm

# Create the schematic
with schemdraw.Drawing() as d:
    d.config(unit=3)

    # Battery (Power Source)
    battery = d.add(elm.BatteryCell().label('Battery 9V'))

    # Morse Key (Switch)
    switch = d.add(elm.Switch().label('Morse Key'), xy=battery.end, to='right')

    # Line Wire
    line = d.add(elm.Line().length(2))

    # Receiver Side: Electromagnet (Coil)
    coil = d.add(elm.Inductor().label('Electromagnet').theta(-90), xy=line.end, to='down')

    # Parallel Buzzer (Optional)
    d.add(elm.Dot())
    buzzer = d.add(elm.Speaker().label('Buzzer (Optional)').theta(0), xy=coil.end, to='right')

    # Parallel Light Bulb (Optional)
    bulb = d.add(elm.Lamp().label('Bulb (Optional)').theta(0), xy=coil.end, to='left')

    # Ground Connection
    d.add(elm.Ground(), xy=coil.end, to='down')

    # Title
    d.add(elm.Label().label('Basic Telegraph Circuit', loc='top'))

    # Show the diagram
    plt.show()