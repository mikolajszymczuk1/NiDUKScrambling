import pytest
from simpy.core import Environment
from simpy.events import Process
from elements.TransmitterElement.Transmitter import Transmitter

@pytest.fixture
def env() -> Environment:
    return Environment()

class TestTransmitter:
    def test_transmitter_sends_data(self, env: Environment) -> None:
        # GIVEN
        data: list[int] = [1, 0, 1, 1, 0, 0, 1, 1]
        bits_to_read: int = 4
        transmitter: Transmitter = Transmitter(env, data, bits_to_read)

        # WHEN
        env.process(transmitter.run_process())
        env.step()

        # THEN
        assert transmitter.data == [0, 0, 1, 1]

    def test_transmitter_sends_no_data_when_empty(self, env: Environment) -> None:
        # GIVEN
        data: list[int] = []
        bits_to_read: int = 4
        transmitter: Transmitter = Transmitter(env, data, bits_to_read)

        # WHEN
        env.process(transmitter.run_process())

        # THEN
        assert transmitter.data == []
