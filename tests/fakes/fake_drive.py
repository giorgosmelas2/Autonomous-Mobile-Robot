from autonomous_robot.interfaces.drive_base import DriveBase


class FakeDrive(DriveBase):
    """Fake implementation of the DriveBase interface for testing purposes."""

    def __init__(self):
        self.left_speed = 0.0
        self.right_speed = 0.0

    def set_wheel_speeds(self, left_speed: float, right_speed: float) -> None:
        self.left_speed = left_speed
        self.right_speed = right_speed
  
    def stop(self) -> None:
        self.left_speed = 0.0
        self.right_speed = 0.0