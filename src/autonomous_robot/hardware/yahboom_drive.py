from autonomous_robot.interfaces.drive_base import DriveBase


CONTROLLER_ADDRESS = 0x16
MOTOR_MOVE_COMMAND = 0x01
MOTOR_STOP_COMMAND = 0x02


def _convert_speed(speed: float) -> tuple[int, int]:

    if speed < -1.0 or speed > 1.0:
        raise ValueError("Speed must be between -1.0 and 1.0")

    hardware_speed = round(abs(speed)*100)
    if speed < 0:
        return (0, hardware_speed)
    elif speed > 0:
        return (1, hardware_speed)
    else:
        return (1, 0)


class YahboomDrive(DriveBase):
    """Implementation of the DriveBase interface for the Yahboom robot."""

    def __init__(self, bus):
        self.bus = bus

    def set_wheel_speeds(self, left_speed: float, right_speed: float) -> None:
        left_direction, left_hardware_speed = _convert_speed(left_speed)
        right_direction, right_hardware_speed = _convert_speed(right_speed)

        data = [
            left_direction, 
            left_hardware_speed,
            right_direction,
            right_hardware_speed
        ]

        self.bus.write_i2c_block_data(CONTROLLER_ADDRESS, MOTOR_MOVE_COMMAND, data)

    def stop(self) -> None:
        self.bus.write_byte_data(CONTROLLER_ADDRESS, MOTOR_STOP_COMMAND, 0x00)