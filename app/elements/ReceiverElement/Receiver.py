from ..PipelineBlockElement.PipelineBlock import PipelineBlock

class Receiver(PipelineBlock):
    PROP_DELAY = 10

    # Run env process
    def run_process(self):
        print(f'Receive data: {self.data}')
        yield self.env.timeout(self.PROP_DELAY)
