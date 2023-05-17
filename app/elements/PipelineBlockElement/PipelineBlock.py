from simpy import Environment

class PipelineBlock:
    def __init__(self, env: Environment, data: list[int]) -> None:
        self.env = env
        self.data = data
