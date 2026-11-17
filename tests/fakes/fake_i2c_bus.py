class FakeI2CBus:
    """Fake I2C bus for testing purposes."""

    def write_i2c_block_data(self, address: int, command: int, data: list[int]) -> None:
        self.address = address
        self.command = command  
        self.data = data

    def write_byte_data(self, address: int, command: int, data: int) -> None:
        self.address = address
        self.command = command  
        self.data = data