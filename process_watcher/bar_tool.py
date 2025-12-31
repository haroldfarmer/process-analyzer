from rich.live import Live
from rich.table import Table
import time
import psutil
import argparse

data = [
    ["Memory", "0"]
]

def get_process_memory(pid):
    process = psutil.Process(pid)
    memory_bytes = process.memory_info().rss
    memory_in_mib = memory_bytes / (1024 * 1024)
    return round(memory_in_mib, 2)

def make_table(data):
   
    table = Table(title="Live Table")
    table.add_column("Memory")
    table.add_column("Value MiB")

    for row in data:
        table.add_row(*row)

    return table

parser = argparse.ArgumentParser(description="A simple calculator script.")
parser.add_argument("--pid", type=int, help="The first number")
args = parser.parse_args()
print(args.pid)
with Live(make_table(data), refresh_per_second=4) as live:
    for i in range(5):
        memory = get_process_memory(int(args.pid))
        # Update one row's value
        data[0][1] = str(memory)  # update row "B"

        # Re-render the table
        live.update(make_table(data))
        time.sleep(1)
