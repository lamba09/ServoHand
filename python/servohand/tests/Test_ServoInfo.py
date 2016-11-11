import pytest
from servohand.ServoInfo import ServoInfo


class Test_ServoInfo:

    def setup_method(self, method):
        self.servo_info = ServoInfo(0, 1., 1.5, 2., 3)

    def teardown_method(self, method):
        del self.servo_info

    def test_init(self):
        assert self.servo_info._pin == 3

    def test_position(self):
        self.servo_info.setPosition(1.23)
        assert self.servo_info.getPosition() == 1.23

    def test_convertDegreeToMs(self):
        assert self.servo_info.convertDegreeToMs(90) == 1.5
        assert self.servo_info.convertDegreeToMs(45) == 1.
        assert self.servo_info.convertDegreeToMs(135) == 2.0

    def test_setPositionDegree(self):
        self.servo_info.setPositionDegree(45)
        assert self.servo_info.getPosition() == 1.0
        self.servo_info.setPositionDegree(135)
        assert self.servo_info.getPosition() == 2.0

    def test_convertPercentToMs(self):
        assert self.servo_info.convertPercentToMs(0) == 1.
        assert self.servo_info.convertPercentToMs(1) == 1.5
        assert self.servo_info.convertPercentToMs(0.5) == 1.25

    def test_setPositionPercent(self):
        self.servo_info.setPositionPercent(1)
        assert self.servo_info.getPosition() == 1.5
        self.servo_info.setPositionPercent(0)
        assert self.servo_info.getPosition() == 1.
        self.servo_info.setPositionPercent(0.1)
        assert self.servo_info.getPosition() == 1.05

