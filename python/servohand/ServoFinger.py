from ServoControlBoard import ServoControlBoard


class ServoFinger(object):

    def __init__(self, id_, name):
        assert type(id_) is int, "id of ServoFinger has to be of type int."
        self._id = id_
        self.name = str(name)
        self._position = 0.5
        self._servo_control_board = ServoControlBoard()

    def getID(self):
        return self._id

    def move(self, position=None):
        if position is None:
            self.setPosition(position)
        self._servo_control_board.move(position=self._servoPosition(), channel=self._id)

    def setPosition(self, pos):
        if pos is not None:
            assert 0. <= pos <= 1., "position has to be between 0 and 1."
            self._position = pos

    def getPosition(self):
        return self._position

    def _servoPosition(self):
        return self._position # FIXME umrechnung und min max hier