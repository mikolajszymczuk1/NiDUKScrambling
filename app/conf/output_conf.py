import os

OUTPUT_DIR: str = 'output'
OUTPUT_FILE: str = os.path.join(OUTPUT_DIR, 'out_signal.txt')
OUTPUT_SCRAMBLER_FILE: str = os.path.join(OUTPUT_DIR, 'out_scrambler.txt')
HISTOGRAM_INPUT_FILE: str = os.path.join(OUTPUT_DIR, 'histogram_input.png')
HISTOGRAM_SCRAMBLER_FILE: str = os.path.join(OUTPUT_DIR, 'histogram_scrambler.png')
HISTOGRAM_OUTPUT_FILE: str = os.path.join(OUTPUT_DIR, 'histogram_output.png')
