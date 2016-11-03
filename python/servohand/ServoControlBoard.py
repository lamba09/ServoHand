from abc import abstractmethod


class ServoControlBoard(object):

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