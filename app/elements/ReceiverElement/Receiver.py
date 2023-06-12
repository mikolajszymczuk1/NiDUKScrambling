from simpy.events import Timeout
from typing import Generator
from ..PipelineBlockElement.PipelineBlock import PipelineBlock

class Receiver(PipelineBlock):
    PROP_DELAY = 10

    # Run env process
    def run_process(self) -> Generator[Timeout, None, None]:
        print(f'Receive data:\n - {self.data} --> Save bits to file\n')
        yield self.env.timeout(self.PROP_DELAY)
