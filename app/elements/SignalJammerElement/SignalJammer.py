from simpy.events import Process
from typing import Generator
from ..PipelineBlockElement.PipelineBlock import PipelineBlock
from ..DescramblerElement.Descrambler import Descrambler
from enums.EnumBitState import EnumBitState

class SignalJammer(PipelineBlock):
    # Run env process
    def run_process(self) -> Generator[Process, None, None]:
        print(f'Passing the signal through the interfering channel:\n - {self.data}')
        descrambler = Descrambler(self.env, self.jamming_channel())
        yield self.env.process(descrambler.run_process())

    def jamming_channel(self) -> list[int]:
        """  """

        sets_of_bits = []
        for bit in self.data:
            if bit == EnumBitState.HIGH.value:
                pass

        return self.data
