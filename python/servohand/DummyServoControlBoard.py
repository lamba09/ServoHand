from servohand.ServoInfo import ServoInfo
from servohand.ServoControlBoard import ServoControlBoard



class DummyServoControlBoard(ServoControlBoard):

    def __init__(self):
        super(DummyServoControlBoard, self).__init__()
        self._connections = {}

    def move(self, channel, position):
        self._verifyPosition(channel, position)
        self._servos[channel].setPosition(position)

    def _addServoConnection(self, channel):
        assert channel in [0,1,2,3,4], "Invalid Servo Channel: {0}".format(channel)
        if not self._servos.has_key(channel):
            self._servos[channel] = ServoInfo()

    def _verifyPosition(self, channel, position):
        pass
        #if self._servos[channel].getMinPosition