from simpy.core import Environment
from elements.TransmitterElement.Transmitter import Transmitter

SIGNAL = [1, 1, 1, 0, 0, 1, 0, 1, 1, 1, 0, 0, 0, 0, 0, 1]

env = Environment()
transmitter = Transmitter(env, SIGNAL, 4)
print('### Start simulation ###\n')
env.process(transmitter.run_process())
env.run()
print('\n### End simulation ###')
