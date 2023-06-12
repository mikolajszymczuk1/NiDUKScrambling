import os
from simpy.core import Environment
from elements.TransmitterElement.Transmitter import Transmitter
from utils.histogram_generator import create_histogram
from conf.output_conf import OUTPUT_DIR, OUTPUT_FILE, HISTOGRAM_INPUT_FILE, HISTOGRAM_OUTPUT_FILE

def main():
    # Input signal
    SIGNAL = [0, 0, 1, 1, 1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1]

    # Clear output file before start simulation
    if os.path.exists(OUTPUT_DIR):
        with open(OUTPUT_FILE, 'w') as file:
            file.truncate()

    # Prepare simulation
    env = Environment()
    transmitter = Transmitter(env, SIGNAL, 16)

    # Run simulation
    print('### Start simulation ###\n')
    env.process(transmitter.run_process())
    env.run()
    print('\n### End simulation ###')

    # Generate histograms
    out_file = open(OUTPUT_FILE, 'r')
    signal_string = out_file.readline()
    signal_converted = [int(bit)for bit in signal_string]
    out_file.close()

    create_histogram(SIGNAL, 'Histogram for input signal', HISTOGRAM_INPUT_FILE)
    create_histogram(signal_converted, 'Histogram for output signal', HISTOGRAM_OUTPUT_FILE)


if __name__ == '__main__':
    main()
