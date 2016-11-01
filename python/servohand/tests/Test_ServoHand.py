from servohand.ServoHand import ServoHand


class Test_ServoHand:

    def setup_method(self, method):
        self.servohand = ServoHand("default")

    def teardown_method(self, method):
        del self.servohand

    def test_init(self):
        servohand = ServoHand("my_right_hand")