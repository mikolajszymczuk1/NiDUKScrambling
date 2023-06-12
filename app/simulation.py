import os
from simpy.core import Environment
from elements.TransmitterElement.Transmitter import Transmitter
from conf.output_conf import OUTPUT_DIR, OUTPUT_FILE

def main():
    # Input signal
    SIGNAL = [0, 1, 1, 1, 0, 1, 0, 1, 1, 1, 0, 0, 0, 0, 0, 1]

    # Clear output file before start simulation
    if os.path.exists(OUTPUT_DIR):
        with open(OUTPUT_FILE, 'w') as file:
            file.truncate()

    # Prepare simulation
    env = Environment()
    transmitter = Transmitter(env, SIGNAL, 4)

    # Run simulation
    print('### Start simulation ###\n')
    env.process(transmitter.run_process())
    env.run()
    print('\n### End simulation ###')


if __name__ == '__main__':
    main()
