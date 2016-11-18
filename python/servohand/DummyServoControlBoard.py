from servohand.ServoInfo import ServoInfo
from servohand.ServoControlBoard import ServoControlBoard



class DummyServoControlBoard(ServoControlBoard):

    def __init__(self):
        super(DummyServoControlBoard, self).__init__()
        self._connections = {}

    def move(self, channel, position):
        self._verifyPosition(channel, position)
        self._servo_info[channel].setPosition(position)

    def _addServoConnection(self, channel):
        assert channel in [0,1,2,3,4], "Invalid Servo Channel: {0}".format(channel)
        if not self._servo_info.has_key(channel):
            self._servo_info[channel] = ServoInfo(channel, 0.5, 2.0, 1.5, pin=None)

    def _verifyPosition(self, channel, position):
        pass
        #if self._servos[channel].getMinPosition