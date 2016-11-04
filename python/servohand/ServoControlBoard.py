from abc import abstractmethod, ABCMeta


class ServoControlBoard(object):

    __metaclass__ = ABCMeta

    def __init__(self):
        self._channels = {}
        self._servos = {}

    @abstractmethod
    def move(self, channel, position):
        pass

    def connectFingers(self, finger_list):
        assert type(finger_list) is list
        for finger in finger_list:
            self._addServoConnection(finger.getID())
            finger.setServoControlBoard(self)

    @abstractmethod
    def _addServoConnection(self, channel):
       pass

    def calibrateFinger(self, channel, min_ms, full_ms, max_ms):
        self._servos[channel].setCalibration(min_ms, full_ms, max_ms)