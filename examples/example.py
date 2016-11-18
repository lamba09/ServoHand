from servohand.ServoHand import ServoHand
from servohand.RaspberryPiBoard import RaspberryPiBoard

hand = ServoHand()
raspberry_pi = RaspberryPiBoard()
hand.setServoControlBoard(raspberry_pi)

finger0 = hand.getFinger(0)
finger0.move(1)

