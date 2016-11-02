import pytest
from servohand.ServoControlBoard import ServoControlBoard


class Test_ServoControlBoard:

    def setup_method(self, method):
        self.controlboard = ServoControlBoard()

    def teardown_method(self, method):
        del self.controlboard

    def test_move(self):
        self.controlboard.move(0, 90)

