#!/usr/bin/env pybricks-micropython
import math

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

ev3 = EV3Brick()

motorB = Motor(Port.B)
motorC = Motor(Port.C)
sensorC1 = ColorSensor(Port.S1)

DIAMETRO_RODA = 6.0
DIST_ENTRE_RODAS = 13.5


def anda_reto(dist):
    motorB.reset_angle(0)
    motorC.reset_angle(0)
    media_motor = 0
    graus_motor = (dist * 360) / (DIAMETRO_RODA * math.pi)
    while media_motor < graus_motor:
        motorB.run(200)
        motorC.run(200)
        media_motor = (motorB.angle() + motorC.angle()) / 2
    motorB.hold()
    motorC.hold()


def curva(graus_reais):
    motorB.reset_angle(0)
    motorC.reset_angle(0)
    media_motor = 0
    graus_motor = graus_reais * (DIST_ENTRE_RODAS / DIAMETRO_RODA)
    while media_motor < graus_motor:
        motorB.run(200)
        motorC.run(-200)
        media_motor = (motorB.angle() - motorC.angle()) / 2
        print(media_motor)
    motorB.hold()
    motorC.hold()


while sensorC1.color() != Color.GREEN:
    anda_reto(20)
    curva(90)
