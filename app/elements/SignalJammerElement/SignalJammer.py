from simpy.events import Process
from typing import Generator
from ..PipelineBlockElement.PipelineBlock import PipelineBlock
from ..DescramblerElement.Descrambler import Descrambler
from enums.EnumBitState import EnumBitState

class SignalJammer(PipelineBlock):
    # Run env process
    def run_process(self) -> Generator[Process, None, None]:
        data_after_jamming = self.jamming_channel()
        print(f'Passing the signal through the interfering channel:\n - {self.data} --> {data_after_jamming}')
        descrambler = Descrambler(self.env, data_after_jamming)
        yield self.env.process(descrambler.run_process())

    def jamming_channel(self) -> list[int]:
        """ Signal interference based on a sequence of the same bits """

        sets_of_bits = []
        for bit in self.data:
            if bit == EnumBitState.HIGH.value:
                pass

        return self.data
