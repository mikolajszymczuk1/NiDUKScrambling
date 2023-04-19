import simpy
from elements.TransmitterElement.Transmitter import Transmitter

SIGNAL = [1, 1, 1, 0, 0, 1, 0, 1, 1, 1, 0, 0, 0, 0, 0, 1]

env = simpy.Environment()
transmitter = Transmitter(env, SIGNAL)
env.process(transmitter.run_process())
env.run(until=10)
