from servohand.ServoControlBoard import ServoControlBoard
import pyb


class MicroPythonBoard(ServoControlBoard):

    def __init__(self):
        super(MicroPythonBoard, self).__init__()


    def move(self, channel, position):
        pass

    def _addServoConnection(self, channel):
        assert channel in [0,1,2,3], "Invalid Servo Channel: {0}".format(channel)
        if not self._servos.has_key(channel):
            self._servos[channel] = pyb.Servo(channel+1)
