from servohand.ServoControlBoard import ServoControlBoard


class ServoFinger(object):

    def __init__(self, id_, name, servo_control_board=None):
        assert type(id_) is int, "id of ServoFinger has to be of type int."
        self._id = id_
        self.name = str(name)
        self._position = 0.5
        self._servo_control_board = servo_control_board

    def setServoControlBoard(self, board):
        assert isinstance(board, ServoControlBoard), "board has to be a ServoControlBoard object."
        self._servo_control_board = board

    def getID(self):
        return self._id

    def move(self, position=None):
        if self._servo_control_board is None:
            raise RuntimeError("No Servo Control Board connected. Add Servo Control Board using 'setServoControlBoard' method.")
        if position is not None:
            self.setPosition(position)
        print "move() in ServoFinger ", self._id, " to position: ", position
        self._servo_control_board.move(position=self._servoPosition(), channel=self._id)

    def setPosition(self, pos):
        if pos is not None:
            assert 0. <= pos <= 1., "position has to be between 0 and 1."
            self._position = pos

    def getPosition(self):
        return self._position

    def _servoPosition(self):
        return self._position # FIXME umrechnung und min max hier

    def calibrate(self, min_ms, full_ms, max_ms):
        assert min_ms <= full_ms and full_ms <= max_ms
        self._servo_control_board.calibrateFinger(self._id, min_ms=min_ms, full_ms=full_ms, max_ms=max_ms)




