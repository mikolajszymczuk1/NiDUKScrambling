from simpy.events import Process
from typing import Generator
from ..PipelineBlockElement.PipelineBlock import PipelineBlock
from ..SignalJammerElement.SignalJammer import SignalJammer
from conf.scrambler_key_conf import SCRAMBLER_KEY
from conf.toggle_modules_conf import SCRAMBLER_MODULE

class Scrambler(PipelineBlock):
    # Run env process
    def run_process(self) -> Generator[Process, None, None]:
        scrambled_data = self.scramble_sum_channel() if SCRAMBLER_MODULE else self.data
        print(f'Scramble data:\n - {self.data} --> {scrambled_data}')
        signal_jammer = SignalJammer(self.env, scrambled_data)
        yield self.env.process(signal_jammer.run_process())

    def scramble_sum_channel(self) -> list[int]:
        """ Scramble data with sum method algorithm """

        scrambled_data = []
        key_length = len(SCRAMBLER_KEY)
        for i, bit in enumerate(self.data):
            scrambled_bit = bit ^ SCRAMBLER_KEY[i % key_length]
            scrambled_data.append(scrambled_bit)

        return scrambled_data
