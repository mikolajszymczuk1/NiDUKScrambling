from simpy.events import Process
from typing import Generator
from ..PipelineBlockElement.PipelineBlock import PipelineBlock
from ..SignalJammerElement.SignalJammer import SignalJammer

class Scrambler(PipelineBlock):
    # Run env process
    def run_process(self) -> Generator[Process, None, None]:
        scrambled_data = self.scramble_sum_channel()
        print(f'Scramble data:\n - {self.data} --> {scrambled_data}')
        signal_jammer = SignalJammer(self.env, scrambled_data)
        yield self.env.process(signal_jammer.run_process())

    def scramble_sum_channel(self) -> list[int]:
        """ Scramble data with specific algorithm """

        return self.data
