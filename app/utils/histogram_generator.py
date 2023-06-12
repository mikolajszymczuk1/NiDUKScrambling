import matplotlib
import matplotlib.pyplot as plt
import seaborn as sns
matplotlib.use('TkAgg')

def create_histogram(data: list[int], title: str, output_image_location: str) -> None:
    """ Generate histogram that shows strings of bits """

    # Setup variables
    current_bit = data[0]
    current_count = 1
    counts = []

    # Iterate through signal
    for bit in data[1:]:
        if bit == current_bit:
            current_count += 1
        else:
            counts.append((current_bit, current_count))
            current_bit = bit
            current_count = 1

    counts.append((current_bit, current_count))

    # Prepare histogram data
    x = range(len(counts))
    y = [count[1] for count in counts]
    labels = [f"{count[0]}" for count in counts]

    # Set theme on histogram
    sns.set_theme(style="darkgrid")

    # Setup histogrm
    plt.bar(x, y)
    plt.title(title)
    plt.xlabel('String index')
    plt.ylabel('String length')
    plt.xticks(x, labels)
    plt.yticks(range(min(y), max(y) + 1))
    plt.savefig(output_image_location)
