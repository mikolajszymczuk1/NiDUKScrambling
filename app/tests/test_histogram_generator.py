import os
from conf.output_conf import OUTPUT_DIR
from utils.histogram_generator import create_histogram, load_signal_from_file

class TestHistogramGenerator:
    @classmethod
    def setup_class() -> None:
        if not os.path.exists(OUTPUT_DIR):
            os.makedirs(OUTPUT_DIR)

    @classmethod
    def teardown_class() -> None:
        os.remove(os.path.join(OUTPUT_DIR, 'histogram_test.png'))
        os.remove(os.path.join(OUTPUT_DIR, 'out_test_signal.txt'))

    def test_create_histogram(self) -> None:
        # GIVEN
        test_data: list[int] = [1, 0, 1, 1]
        output_image: str = os.path.join(OUTPUT_DIR, 'histogram_test.png')

        # WHEN
        create_histogram(test_data, 'title', output_image)

        # THEN
        assert os.path.exists(output_image)

    def test_load_signal_from_file(self) -> None:
        # GIVEN
        test_signal: str = os.path.join(OUTPUT_DIR, 'out_test_signal.txt')
        with open(test_signal, 'w') as file:
            file.write('1001101')

        # WHEN
        signal: list[int] = load_signal_from_file(test_signal)

        # THEN
        assert signal == [1, 0, 0, 1, 1, 0, 1]
