# rich_live.py
import time
import random
from datetime import datetime

from rich.live import Live
from rich.table import Table

table = Table()
table.add_column("Row ID")
table.add_column("Description")
table.add_column("Level")

levels = ["[red]FATAL", "[magenta]CRITICAL", "[yellow]MAJOR", "[cyan]warning"]

with Live(table, refresh_per_second=4):  # update 4 times a second to feel fluid
    for row in range(12):
        time.sleep(0.4)  # arbitrary delay
        # update the renderable internally
        table.add_row(str(row), "issue at {}".format(datetime.now()), random.choice(levels))
