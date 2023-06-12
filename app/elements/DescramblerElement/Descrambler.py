from simpy.events import Process
from typing import Generator
from ..PipelineBlockElement.PipelineBlock import PipelineBlock
from ..ReceiverElement.Receiver import Receiver
from conf.scrambler_key_conf import SCRAMBLER_KEY
from conf.toggle_modules_conf import DESCRAMBLER_MODULE

class Descrambler(PipelineBlock):
    # Run env process
    def run_process(self) -> Generator[Process, None, None]:
        descrambled_data = self.descramble_sum_channel() if DESCRAMBLER_MODULE else self.data
        print(f'Descrable data:\n - {self.data} --> {descrambled_data}')
        receiver = Receiver(self.env, descrambled_data)
        yield self.env.process(receiver.run_process())

    def descramble_sum_channel(self) -> list[int]:
        """ Descramble data with sum method algorithm """

        descrambled_data = []
        key_length = len(SCRAMBLER_KEY)
        for i, bit in enumerate(self.data):
            descrambled_bit = bit ^ SCRAMBLER_KEY[i % key_length]
            descrambled_data.append(descrambled_bit)

        return descrambled_data
