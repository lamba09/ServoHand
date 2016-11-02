import pytest
from servohand.ServoHand import ServoHand
from servohand.ServoFinger import ServoFinger


class Test_ServoHand:

    def setup_method(self, method):
        self.servohand = ServoHand()

    def teardown_method(self, method):
        del self.servohand

    def test_init(self):
        servohand = ServoHand("my_right_hand")

    def test_getFingers(self):
        finger = self.servohand.getFinger(0)
        assert isinstance(finger, ServoFinger)
        finger = self.servohand.getFinger(1)
        assert isinstance(finger, ServoFinger)
        finger = self.servohand.getFinger(2)
        assert isinstance(finger, ServoFinger)
        finger = self.servohand.getFinger(3)
        assert isinstance(finger, ServoFinger)
        finger = self.servohand.getFinger(4)
        assert isinstance(finger, ServoFinger)
        with pytest.raises(IndexError):
            self.servohand.getFinger(5)

    def test_setFingerPositions(self):
        positions = self.servohand.setFingerPositions()
        assert positions == [0.5,0.5,0.5,0.5,0.5]
        positions = self.servohand.setFingerPositions(0,0,0,0,0)
        assert positions == [0,0,0,0,0]
        positions = self.servohand.setFingerPositions(1,1,1,1,1)
        assert positions == [1,1,1,1,1]
        positions = self.servohand.setFingerPositions(None, 0, 0.5, None, None)
        assert positions == [1, 0, 0.5, 1, 1]
        with pytest.raises(AssertionError):
            self.servohand.setFingerPositions(1.5)

    def test_getFingerPositions(self):
        self.servohand.setFingerPositions(1,1,1,1,1)
        assert self.servohand.getFingerPositions() == [1,1,1,1,1]

    def test_move(self):
        self.servohand.move()
        self.servohand.move(0,0,0,0,0)
        assert self.servohand.getFingerPositions() == [0,0,0,0,0]
        self.servohand.move(1,1,1,1,1)
        assert self.servohand.getFingerPositions() == [1,1,1,1,1]
        self.servohand.move(0, None, 0, None, 0)
        assert self.servohand.getFingerPositions() == [0,1,0,1,0]
