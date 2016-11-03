import pytest
from servohand.ServoControlBoard import ServoControlBoard
from servohand.ServoFinger import ServoFinger


class Test_ServoControlBoard:

    def setup_method(self, method):
        self.controlboard = ServoControlBoard()

    def teardown_method(self, method):
        del self.controlboard

    def test_move(self):
        self.controlboard.move(0, 90)

    def test_connectFingers(self):
        fingers = [ServoFinger(42, "dummy_finger")]
        with pytest.raises(AssertionError):
            self.controlboard.connectFingers(fingers[0])
        self.controlboard.connectFingers(fingers)
