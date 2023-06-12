from simpy.events import Timeout
from typing import Generator
from ..PipelineBlockElement.PipelineBlock import PipelineBlock
from conf.output_conf import OUTPUT_FILE

class Receiver(PipelineBlock):
    PROP_DELAY = 10

    # Run env process
    def run_process(self) -> Generator[Timeout, None, None]:
        print(f'Receive data:\n - {self.data} --> Save bits to file\n')

        with open(OUTPUT_FILE, 'a') as file:
            for bit in self.data:
                file.write(str(bit))

        yield self.env.timeout(self.PROP_DELAY)
