from ServoControlBoard import ServoControlBoard

class ServoFinger(object):

    def __init__(self, index):
        self._index = index
        self._position = 0.5
        self._servo_control_board = ServoControlBoard()

    def move(self, position=None):
        if position is None:
            self.setPosition(position)
        self._servo_control_board.move(position=self._servoPosition(), channel=self._index)

    def setPosition(self, pos):
        if pos is not None:
            assert 0. <= pos <= 1., "position has to be between 0 and 1."
            self._position = pos

    def getPosition(self):
        return self._position

    def _servoPosition(self):
        return self._position # FIXME umrechnung und min max hier