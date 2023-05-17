from simpy.events import Process
from typing import Generator
from ..PipelineBlockElement.PipelineBlock import PipelineBlock
from ..ScramblerElement.Scrambler import Scrambler

class Transmitter(PipelineBlock):
    # Run env process
    def run_process(self) -> Generator[Process, None, None]:
        print(f'Prepare and send data:\n - {self.data}')
        scrambler = Scrambler(self.env, self.data)
        yield self.env.process(scrambler.run_process())
