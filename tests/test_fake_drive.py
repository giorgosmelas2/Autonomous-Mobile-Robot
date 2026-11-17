from fakes.fake_drive import FakeDrive


def test_initial_wheel_speeds():
    fake_driver = FakeDrive()
    assert fake_driver.left_speed == 0.0
    assert fake_driver.right_speed == 0.0


def test_set_wheel_speeds():
    fake_driver = FakeDrive()
    fake_driver.set_wheel_speeds(0.5, -0.3)
    assert fake_driver.left_speed == 0.5
    assert fake_driver.right_speed == -0.3


def test_stop():
    fake_driver = FakeDrive()
    fake_driver.set_wheel_speeds(0.5, -0.3)
    fake_driver.stop()
    assert fake_driver.left_speed == 0.0
    assert fake_driver.right_speed == 0.0