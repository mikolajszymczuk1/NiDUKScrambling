from simpy.events import Process
from typing import Generator
from ..PipelineBlockElement.PipelineBlock import PipelineBlock
from ..ReceiverElement.Receiver import Receiver

class Descrambler(PipelineBlock):
    # Run env process
    def run_process(self) -> Generator[Process, None, None]:
        print(f'Descrable data:\n - {self.data}')
        receiver = Receiver(self.env, self.data)
        yield self.env.process(receiver.run_process())
