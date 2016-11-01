from servohand.ServoHand import ServoHand


class Test_ServoHand:

    def test_init(self):
        servohand = ServoHand("my_right_hand")
        assert False