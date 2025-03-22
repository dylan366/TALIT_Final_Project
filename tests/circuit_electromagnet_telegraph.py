import sys
print(sys.executable)
import matplotlib.pyplot as plt
import schemdraw
import schemdraw.elements as elm

with schemdraw.Drawing() as d:
    d.config(unit=3)
    battery = d.add(elm.BatteryCell().label('Battery 9V'))
    switch = d.add(elm.Switch().label('Morse Key'), xy=battery.end, to='right')
    line = d.add(elm.Line().length(2))
    coil = d.add(elm.Inductor().label('Electromagnet').theta(-90), xy=line.end, to='down')
    d.add(elm.Dot())
    buzzer = d.add(elm.Speaker().label('Buzzer (Optional)').theta(0), xy=coil.end, to='right')
    bulb = d.add(elm.Lamp().label('Bulb (Optional)').theta(0), xy=coil.end, to='left')
    d.add(elm.Ground(), xy=coil.end, to='down')
    d.add(elm.Label().label('Basic Telegraph Circuit', loc='top'))
    plt.show()