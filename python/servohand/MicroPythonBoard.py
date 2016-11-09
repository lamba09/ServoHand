from servohand.ServoControlBoard import ServoControlBoard
import pyb


class MicroPythonBoard(ServoControlBoard):

    def __init__(self):
        super(MicroPythonBoard, self).__init__()

    def move(self, channel, position):
        pass

    def _addServoConnection(self, channel, calibration):
        assert channel in [0,1,2,3], "Invalid Servo Channel: {0}".format(channel)
        if not self._servo_info.has_key(channel):
            self._servo_info[channel] = pyb.Servo(channel+1, 0.5, 2.0, 1.5, pin=None)
