from simpy.core import Environment
from simpy.events import Process
from typing import Generator
from ..PipelineBlockElement.PipelineBlock import PipelineBlock
from ..ScramblerElement.Scrambler import Scrambler

class Transmitter(PipelineBlock):
    def __init__(self, env: Environment, data: list[int], bits_to_read: int = 8) -> None:
        super().__init__(env, data)
        self.bits_to_read: int = bits_to_read

    # Run env process
    def run_process(self) -> Generator[Process, None, None]:
        print(f'Prepare and send data:\n - {self.data}\n')

        while len(self.data) > 0:
            bits: list[int] = self.data[:self.bits_to_read]
            self.data: list[int] = self.data[self.bits_to_read:]
            print(f'Send bits:\n - {bits}')
            scrambler = Scrambler(self.env, bits)
            yield self.env.process(scrambler.run_process())
