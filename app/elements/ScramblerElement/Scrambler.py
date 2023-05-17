from simpy.events import Process
from typing import Generator
from ..PipelineBlockElement.PipelineBlock import PipelineBlock
from ..SignalJammerElement.SignalJammer import SignalJammer

class Scrambler(PipelineBlock):
    # Run env process
    def run_process(self) -> Generator[Process, None, None]:
        print(f'Scramble data:\n - {self.data}')
        signal_jammer = SignalJammer(self.env, self.data)
        yield self.env.process(signal_jammer.run_process())
