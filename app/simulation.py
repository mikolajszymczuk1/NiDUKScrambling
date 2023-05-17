from simpy.core import Environment
from elements.TransmitterElement.Transmitter import Transmitter

SIGNAL = [1, 1, 1, 0, 0, 1, 0, 1, 1, 1, 0, 0, 0, 0, 0, 1]

env = Environment()
transmitter = Transmitter(env, SIGNAL)
print('### Start simulation ###\n')
env.process(transmitter.run_process())
env.run(until=10)
print('\n### End simulation ###')
