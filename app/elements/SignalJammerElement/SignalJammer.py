import random
from simpy.events import Process
from typing import Generator
from ..PipelineBlockElement.PipelineBlock import PipelineBlock
from ..DescramblerElement.Descrambler import Descrambler
from enums.EnumBitState import EnumBitState
from conf.toggle_modules_conf import JAMMER_MODULE

class SignalJammer(PipelineBlock):
    # Run env process
    def run_process(self) -> Generator[Process, None, None]:
        data_after_jamming: list[int] = self.jamming_channel() if JAMMER_MODULE else self.data
        print(f'Passing the signal through the interfering channel:\n - {self.data} --> {data_after_jamming}')
        descrambler = Descrambler(self.env, data_after_jamming)
        yield self.env.process(descrambler.run_process())

    def find_sequence(self) -> tuple[bool, int, int]:
        """
        Try to find sequence of 1 or 0, return tuple with data
        Tuple --> True/False | start index | end index
        """

        start_index: int = 0
        end_index: int = -1
        current_sequence: int = 0
        current_state: int = self.data[0]
        for i in range(len(self.data)):
            if self.data[i] == current_state:
                current_sequence += 1
                end_index += 1
            else:
                start_index = i
                end_index = i
                current_sequence = 1

                if current_state == EnumBitState.LOW.value:
                    current_state = EnumBitState.HIGH.value
                else:
                    current_state = EnumBitState.LOW.value

            if current_sequence >= int(len(self.data) / 2) + 1:
                return (True, start_index, end_index)

        return (False, start_index, end_index)

    def jamming_channel(self) -> list[int]:
        """ Signal interference based on a sequence of the same bits """

        found_sequence: bool
        start_index: int
        end_index: int
        data: list[int] = self.data[:]
        found_sequence, start_index, end_index = self.find_sequence()

        if found_sequence:
            bit_index_to_change: int = random.randint(start_index, end_index)
            if data[bit_index_to_change] == EnumBitState.HIGH.value:
                data[bit_index_to_change] = EnumBitState.LOW.value
            else:
                data[bit_index_to_change] = EnumBitState.HIGH.value

        return data
