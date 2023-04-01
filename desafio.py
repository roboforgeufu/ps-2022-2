#!/usr/bin/env pybricks-micropython
from pybricks.ev3devices import (
    ColorSensor,
    GyroSensor,
    InfraredSensor,
    Motor,
    TouchSensor,
    UltrasonicSensor,
)
from pybricks.hubs import EV3Brick
from pybricks.media.ev3dev import ImageFile, SoundFile
from pybricks.parameters import Button, Color, Direction, Port, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import DataLog, StopWatch, wait

# This program requires LEGO EV3 MicroPython v2.0 or higher.
# Click "Open user guide" on the EV3 extension tab for more information.

ev3 = EV3Brick()
ev3.speaker.beep()


def input_objetivo(ev3_brick):
    # Segura a execução do programa enquanto não houver cliques nos botões, conferindo sem parar
    objetivo = None
    while True:
        buttons = ev3.buttons.pressed()
        # Guarda o objetivo de acordo com o botão apertado
        if Button.UP in buttons or objetivo == None:
            objetivo = Color.GREEN
            ev3_brick.speaker.beep(100)
        elif Button.RIGHT in buttons:
            objetivo = Color.YELLOW
            ev3_brick.speaker.beep(200)
        elif Button.DOWN in buttons:
            objetivo = Color.RED
            ev3_brick.speaker.beep(300)
        elif Button.LEFT in buttons:
            objetivo = Color.BLUE
            ev3_brick.speaker.beep(400)

        ev3_brick.light.on(objetivo)

        # Ao apertar o botão do meio, sai do laço de repetição
        if Button.CENTER in buttons:
            break

    # Sinaliza a decisão
    ev3_brick.speaker.say(str(objetivo)[6:])
    return objetivo


# Escreva seu código aqui
objetivo = input_objetivo(ev3)
ev3.screen.print(objetivo)
