# Scrambling simulation for univeristy project

## Project modules

---

In project there are several modules that are single pipeline blocks, each one represents single functionality.

| Module | Functionality |
|--------|---------------|
| Transmitter | Load singal and send fragments to next block |
| Scrambler | Use special alghoritm to mix code (scramble code)|
| Signal Jammer | Crash code based on string of bits lengts |
| Descrambler | descramble mixed code from scramble process |
| Receiver | Merge all fragments and save output signal in file |

## Scrambling process

---

We concentrate on SUM method when we additonally use special key scramble signal

```py
def scramble_sum_channel(self) -> list[int]:
    """ Scramble data with sum method algorithm """

    scrambled_data: list[int] = []
    key_length: int = len(SCRAMBLER_KEY)
    for i, bit in enumerate(self.data):
        scrambled_bit: int = bit ^ SCRAMBLER_KEY[i % key_length]
        scrambled_data.append(scrambled_bit)

    return scrambled_data
```

Here is a formula that we use:

```py
scrambled_data[i] = data[i] XOR scrambler_key[i mod m]
```

Here is example and step by step how algorithm works:

```py
data = [0, 1, 1, 0, 0, 1, 0]
scrambler_key = [1, 0, 1, 0, 1]
m = len(scrambler_key) = 5

scrambled_data[0] = data[0] XOR scrambler_key[0 mod 5] = 0 XOR 1 = 1
scrambled_data[1] = data[1] XOR scrambler_key[1 mod 5] = 1 XOR 0 = 1
scrambled_data[2] = data[2] XOR scrambler_key[2 mod 5] = 1 XOR 1 = 0
scrambled_data[3] = data[3] XOR scrambler_key[3 mod 5] = 0 XOR 0 = 0
scrambled_data[4] = data[4] XOR scrambler_key[4 mod 5] = 0 XOR 1 = 1
scrambled_data[5] = data[5] XOR scrambler_key[5 mod 5] = 1 XOR 1 = 0
scrambled_data[6] = data[6] XOR scrambler_key[6 mod 5] = 0 XOR 1 = 1

scrambled_data = [1, 1, 0, 0, 1, 0, 1]
```

## Project setup

---

1) Clone project

2) Create virtual environment in project directory and activate it

```sh
python3 -m venv ./env
source ./env/bin/activate
```

3) Install dependencies from requirements.txt file:

```sh
pip install -r requirements.txt
```

4) Run simulation to generate output files

```sh
python app/simulation.py
```

## Tests

---

You can also run tests with command:

```sh
pytest
```

## Input / Output

---

In input directory in ```in_signal.txt``` you can paste any signal you whould like to use in simulation

In Output directory you can check output histograms and output text files where ```out_scrambler.txt``` is a file with scrambled signal code and ```out_signal.txt``` with simulation output signal code.
