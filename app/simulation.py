import os
from simpy.core import Environment
from elements.TransmitterElement.Transmitter import Transmitter
from utils.histogram_generator import create_histogram, load_signal_from_file
from utils.signal_utils import error_bit_rate
from conf.input_conf import INPUT_FILE
from conf.output_conf import OUTPUT_DIR, OUTPUT_FILE, OUTPUT_SCRAMBLER_FILE, HISTOGRAM_INPUT_FILE, HISTOGRAM_SCRAMBLER_FILE, HISTOGRAM_OUTPUT_FILE
from conf.simulation_conf import BITS_IN_ONE_TIME

def main() -> None:
    # Input signal
    SIGNAL: list[int] = load_signal_from_file(INPUT_FILE)

    # Create output directory if does not exist
    if not os.path.exists(OUTPUT_DIR): os.makedirs(OUTPUT_DIR)

    # Clear output files before start simulation
    if os.path.exists(OUTPUT_DIR):
        with open(OUTPUT_FILE, 'w') as file: file.truncate()
        with open(OUTPUT_SCRAMBLER_FILE, 'w') as file: file.truncate()

    # Prepare simulation
    env = Environment()
    transmitter = Transmitter(env, SIGNAL, BITS_IN_ONE_TIME)

    # Run simulation
    print('### Start simulation ###\n')
    env.process(transmitter.run_process())
    env.run()
    print('\n### End simulation ###')

    # Generate histograms
    signal_out: list[int] = load_signal_from_file(OUTPUT_FILE)
    scrambler_out: list[int] = load_signal_from_file(OUTPUT_SCRAMBLER_FILE)
    create_histogram(SIGNAL, 'Histogram for input signal', HISTOGRAM_INPUT_FILE)
    create_histogram(scrambler_out, 'Histogram for scrambler output', HISTOGRAM_SCRAMBLER_FILE)
    create_histogram(signal_out, 'Histogram for output signal', HISTOGRAM_OUTPUT_FILE)
    print(f'\nEBR: {error_bit_rate(SIGNAL, signal_out)}%')


if __name__ == '__main__':
    main()
