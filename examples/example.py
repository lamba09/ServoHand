from servohand.ServoHand import ServoHand
from servohand.RaspberryPiBoard import RaspberryPiBoard
import time

hand = ServoHand()
raspberry_pi = RaspberryPiBoard()
hand.setServoControlBoard(raspberry_pi)


def showNumber(number):
    assert 0 <= number <= 5
    bin(number)