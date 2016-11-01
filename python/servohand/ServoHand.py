from ServoFinger import ServoFinger


class ServoHand(object):

    def __init__(self, name):

        self._fingers = [ServoFinger(index=i) for i in xrange(5)]

    def getFinger(self, index):
        return self._fingers[index]

    def move(self, a=None, b=None, c=None, d=None, e=None):
        args = [a,b,c,d,e]
        for i in xrange(5):
            if args[i] is not None:
                self._fingers[i].move(args[i])

    def binaryMove(self, configuration):
        assert type(configuration) is int, "configuration has to be an integer (5 bit)"
        # FIXME

