from servohand.ServoFinger import ServoFinger
from servohand.ServoControlBoard import ServoControlBoard


class ServoHand(object):

    def __init__(self, name="ServoHand"):
        self._name = name
        self._fingers = [ServoFinger(id_=i, name=name+"_finger"+str(id)) for i in xrange(5)]

    def setServoControlBoard(self, board):
        assert isinstance(board, ServoControlBoard), "board has to be a ServoControlBoard object."
        self._servo_control_board = board
        self._servo_control_board.connectFingers(self._fingers)

    def getFinger(self, index):
        return self._fingers[index]

    def move(self, a=None, b=None, c=None, d=None, e=None):
        positions = [a,b,c,d,e]
        print "move() in ServoHand to positions: ", positions
        self.setFingerPositions(*positions)
        for i in xrange(5):
            self._fingers[i].move()

    def setFingerPositions(self, a=None, b=None, c=None, d=None, e=None):
        positions = [a,b,c,d,e]
        for i, pos in enumerate(positions):
            if pos is not None:
                self._fingers[i].setPosition(pos)
        return self.getFingerPositions()

    def getFingerPositions(self):
        positions = [finger.getPosition() for finger in self._fingers]
        return positions

    def moveBinary(self, number):
        assert 0 <= number < 2**5 and type(number) is int
        self.move(*map(int, list("{0:05b}".format(number)[::-1])))