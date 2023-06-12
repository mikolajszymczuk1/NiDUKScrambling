from simpy.events import Process
from typing import Generator
from ..PipelineBlockElement.PipelineBlock import PipelineBlock
from ..ReceiverElement.Receiver import Receiver

class Descrambler(PipelineBlock):
    # Run env process
    def run_process(self) -> Generator[Process, None, None]:
        descrambled_data = self.descramble_sum_channel()
        print(f'Descrable data:\n - {self.data} --> {descrambled_data}')
        receiver = Receiver(self.env, descrambled_data)
        yield self.env.process(receiver.run_process())

    def descramble_sum_channel(self) -> list[int]:
        """ Descramble data with specific algorithm """

        return self.data
