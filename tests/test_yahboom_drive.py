import pytest
from autonomous_robot.hardware.yahboom_drive import _convert_speed, YahboomDrive
from fakes.fake_i2c_bus import FakeI2CBus


def test_speed_conversion():
    assert _convert_speed(0.6) == (1, 60)
    assert _convert_speed(-0.6) == (0, 60)
    assert _convert_speed(0.0) == (1, 0)
    assert _convert_speed(1.0) == (1, 100)
    assert _convert_speed(-1.0) == (0, 100)


def test_speed_conversion_rejects_out_of_range_values():
    with pytest.raises(ValueError):
        _convert_speed(1.5)
        
    with pytest.raises(ValueError):
        _convert_speed(-1.5)


def test_set_wheel_speeds():
    bus = FakeI2CBus()
    drive = YahboomDrive(bus)

    drive.set_wheel_speeds(0.5, -0.3)

    assert bus.address == 0x16
    assert bus.command == 0x01
    assert bus.data == [1, 50, 0, 30]


def test_stop():
    bus = FakeI2CBus()
    drive = YahboomDrive(bus)

    drive.stop()

    assert bus.address == 0x16
    assert bus.command == 0x02
    assert bus.data == 0x00


