import matplotlib
import matplotlib.pyplot as plt
import seaborn as sns
matplotlib.use('TkAgg')

def create_histogram(data: list[int], title: str, output_image_location: str) -> None:
    """ Generate histogram that shows strings of bits """

    # Set theme on histogram
    sns.set_theme(style="darkgrid")

    # Create new figure and axis
    fig, ax = plt.subplots(figsize=(16, 9))

    # Setup variables
    current_bit: int = data[0]
    current_count: int = 1
    counts: dict[int, int] = {}

    # Iterate through signal
    for bit in data[1:]:
        if bit == current_bit:
            current_count += 1
        else:
            if current_count in counts:
                counts[current_count] += 1
            else:
                counts[current_count] = 1
            current_bit = bit
            current_count = 1

    if current_count in counts:
        counts[current_count] += 1
    else:
        counts[current_count] = 1

    # Prepare histogram data
    x: range = range(1, max(counts.keys()) + 1)
    y: list[int] = [counts[i] if i in counts else 0 for i in x]
    labels: list[str] = [str(i) for i in x]

    # Setup histogram
    ax.bar(x, y)
    ax.set_title(title)
    ax.set_xlabel('String length')
    ax.set_ylabel('String count')
    ax.set_xticks(x)
    ax.set_xticklabels(labels)
    ax.set_yticks(range(0, max(y) + 1, 5))
    plt.savefig(output_image_location)
    plt.close(fig)


def load_signal_from_file(file_location: str) -> list[int]:
    """ Load string signal from file and convert it to list of bits """

    with open(file_location, 'r') as file:
        signal_string: str = file.readline()
        signal_converted: list[int] = [int(bit) for bit in signal_string]
        return signal_converted
