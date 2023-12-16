import subprocess
import argparse
import re
import time

# Define command-line arguments
parser = argparse.ArgumentParser(description="Run Chia wallet send command multiple times.")
parser.add_argument("--tick", type=str, required=True, help="Value to replace 'tick' in the command.")
parser.add_argument("--iter", type=int, required=True, help="Number of times to run the command.")
parser.add_argument("--fee", type=float, required=True, help="Fee value to use in the command.")

# Parse the command-line arguments
args = parser.parse_args()

# Chia wallet send command template
chia_send_command_template = [
    "chia",
    "wallet",
    "send",
    "-t",
    "xchxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
    "-i",
    "3",
    "-a",
    "0.000000000001",
    "-m",
    "0.00000000001",
    "-e",
    "{{'p':'xchs','op':'mint','tick':'{}','amt':'1000'}}".format(args.tick),
    "--override",
    "--fee",
    str(args.fee),
]

# Function to run Chia send command and get block height and tx ID
def run_chia_send_command():
    try:
        print("Running Chia send command...")
        send_output = subprocess.check_output(chia_send_command_template, text=True)
        print(f"Command Output: {send_output}")
        match = re.search(r"-f (\d+) -tx (0x[a-fA-F0-9]+)", send_output)
        if match:
            block_height = match.group(1)
            tx_id = match.group(2)
            print(f"Block Height: {block_height}")
            print(f"Transaction ID: {tx_id}")
            return block_height, tx_id
        else:
            print("Block Height and Transaction ID not found in output.")
            return None, None
    except subprocess.CalledProcessError as e:
        print(f"Error running Chia send command: {e}")
        return None, None

# Function to check transaction status and wait for confirmation
def check_transaction_status(block_height, tx_id):
    while True:
        # Run chia wallet get_transaction command to get status
        get_transaction_command = ["chia", "wallet", "get_transaction", "-f", block_height, "-tx", tx_id]
        try:
            print(f"Checking transaction status for Block Height: {block_height}, TXID: {tx_id}...")
            transaction_output = subprocess.check_output(get_transaction_command, text=True)
            print(f"Transaction Output: {transaction_output}")
            status_match = re.search(r"Status: (\w+)", transaction_output)
            if status_match:
                status = status_match.group(1)
                print(f"Transaction Status: {status}")
                if status == "Confirmed":
                    print("Transaction is Confirmed. Proceeding to the next iteration.")
                    break  # Exit the loop when confirmed
                else:
                    print("Transaction is not Confirmed. Waiting for confirmation...")
            else:
                print("Transaction status not found in output.")
        except subprocess.CalledProcessError as e:
            print(f"Error running Chia get_transaction command: {e}")
        
        time.sleep(5)  # Wait for 5 seconds before checking again

# Loop to run the command
for i in range(args.iter):
    block_height, tx_id = run_chia_send_command()
    if block_height and tx_id:
        check_transaction_status(block_height, tx_id)
    
    if i < args.iter - 1:
        print("Waiting for the last one to complete before starting the next one...")

print("All commands have completed.")
