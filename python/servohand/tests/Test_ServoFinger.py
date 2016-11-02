import pytest
from servohand.ServoFinger import ServoFinger


class Test_ServoFinger:

    def setup_method(self, method):
        self.servofinger = ServoFinger(0, "default")

    def teardown_method(self, method):
        del self.servofinger

    def test_init(self):
        servofilger = ServoFinger(1, "my_right_hand")