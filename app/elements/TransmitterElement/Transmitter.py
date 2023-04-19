from komm import BinarySymmetricChannel
from ..PipelineBlockElement.PipelineBlock import PipelineBlock
from ..ReceiverElement.Receiver import Receiver
from typing import List

class Transmitter(PipelineBlock):
    def __init__(self, env, data: List[int]):
        super().__init__(env, data)
        self.bsc = BinarySymmetricChannel(0.2)

    # Run env process
    def run_process(self):
        print(f'Prepare and send data: {self.data}')
        receiver = Receiver(self.env, self.bsc(self.data))
        yield self.env.process(receiver.run_process())
