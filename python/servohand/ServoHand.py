from ServoFinger import ServoFinger


class ServoHand(object):

    def __init__(self, name):

        self._fingers = [ServoFinger(index=i) for i in xrange(5)]

    def getFinger(self, index):
        return self._fingers[index]

    def move(self, a=None, b=None, c=None, d=None, e=None):
        positions = [a,b,c,d,e]
        self.setFingerPositions(*positions)
        for i in xrange(5):
            self._fingers[i].move()
#
    #def binaryMove(self, configuration):
    #    assert type(configuration) is int, "configuration has to be an integer (5 bit)"
    #    # FIXME

    def setFingerPositions(self, a=None, b=None, c=None, d=None, e=None):
        positions = [a,b,c,d,e]
        for i, pos in enumerate(positions):
            if pos is not None:
                self._fingers[i].setPosition(pos)
        return self.getFingerPositions()

    def getFingerPositions(self):
        positions = [finger.getPosition() for finger in self._fingers]
        return positions