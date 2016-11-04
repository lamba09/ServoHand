import pytest
from servohand.DummyServoControlBoard import DummyServoControlBoard as ServoControlBoard
from servohand.ServoFinger import ServoFinger


class Test_ServoControlBoard:

    def setup_method(self, method):
        self.controlboard = ServoControlBoard()
        fingers = [ServoFinger(0, "dummy_finger")]
        self.controlboard.connectFingers(fingers)

    def teardown_method(self, method):
        del self.controlboard

    def test_move(self):
        self.controlboard.move(0, 1.5)
        #with pytest.raises(ValueError):
        #    self.controlboard.move(0, 0.75)

    def test_connectFingers(self):
        fingers = [ServoFinger(0, "dummy_finger")]
        with pytest.raises(AssertionError):
            self.controlboard.connectFingers(fingers[0])
        self.controlboard.connectFingers(fingers)

    def test_calibrateFinger(self):
        self.controlboard.calibrateFinger(0, 0.5, 1.5, 1.7)