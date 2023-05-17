from simpy.events import Process
from typing import Generator
from ..PipelineBlockElement.PipelineBlock import PipelineBlock
from ..DescramblerElement.Descrambler import Descrambler

class SignalJammer(PipelineBlock):
    # Run env process
    def run_process(self) -> Generator[Process, None, None]:
        print(f'Passing the signal through the interfering channel:\n - {self.data}')
        descrambler = Descrambler(self.env, self.data)
        yield self.env.process(descrambler.run_process())

    def jamming_channel(self) -> None:
        pass
