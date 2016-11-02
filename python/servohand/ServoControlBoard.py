#from ServoFinger import ServoFinger


class ServoControlBoard:

    def __init__(self):
        pass

    def move(self, channel, position):
        pass

    def connectFingers(self, finger_list):
       assert type(finger_list) is list
       for finger in finger_list:
           if isinstance(finger, ServoFinger):
               self._addServoConnection(finger.getID())
           else:
               raise TypeError("Invalid Finger List")

    def _addServoConnection(self, channel):
       pass