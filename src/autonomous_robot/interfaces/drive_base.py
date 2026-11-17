from abc import ABC, abstractmethod

class DriveBase(ABC):
    """Abstract interface for controlling the robot's drive system."""

    @abstractmethod
    def set_wheel_speeds(self, left_speed: float, right_speed: float) -> None:
        pass

    @abstractmethod
    def stop(self) -> None:
        pass