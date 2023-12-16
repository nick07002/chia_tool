# Chia Inscription Minting Tool

**Disclaimer: This tool is for minting Chia inscriptions and should be used at your own risk. Please exercise caution when using it.**

## Prerequisites

Before you can use this tool, make sure you have the following prerequisites installed on your system:

- **Python**: Ensure that Python is installed on your machine. You can download it from [python.org](https://www.python.org/downloads/).

- **Pip**: Pip is the package manager for Python. It should be included with your Python installation. You can check if Pip is installed by running `pip --version` in your terminal.

## Usage

1. Clone this repository to your local machine.

2. Open the `run.py` file in the project directory.

3. Replace the Chia address on **line 21** with your own Chia address.

4. Run the tool using the following command in your terminal:

   ```bash
   python3 run.py --tick <coin_name> --iter <number_of_iterations> --fee <transaction_fee>

   for example:

   python3 run.py --tick bram --iter 2 --fee 0.0001
