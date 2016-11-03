import pytest
from servohand.ServoFinger import ServoFinger
from servohand.ServoControlBoard import ServoControlBoard


class Test_ServoFinger:

    def setup_method(self, method):
        self.servofinger = ServoFinger(0, "default")
        board = ServoControlBoard()
        self.servofinger.setServoControlBoard(board)

    def teardown_method(self, method):
        del self.servofinger

    def test_init(self):
        servofilger = ServoFinger(1, "my_right_hand")
        with pytest.raises(AssertionError):
            ServoFinger(1.1, "sADF")
        with pytest.raises(AssertionError):
            ServoFinger("finger1", "daumen")

    def test_getID(self):
        assert self.servofinger.getID() == 0
        assert ServoFinger(12, "new").getID() == 12

    def test_defaultPosition(self):
        assert self.servofinger.getPosition() == 0.5

    def test_setPosition(self):
        self.servofinger.setPosition(0.42)
        assert self.servofinger.getPosition() == 0.42
        self.servofinger.setPosition(None)
        assert self.servofinger.getPosition() == 0.42
        with pytest.raises(AssertionError):
            self.servofinger.setPosition(1.5)
        with pytest.raises(AssertionError):
            self.servofinger.setPosition(-0.5)

    def test_move(self):
        self.servofinger.setPosition(0.5)
        self.servofinger.move()
        assert self.servofinger.getPosition() == 0.5
        self.servofinger.move(1)
        assert self.servofinger.getPosition() == 1

