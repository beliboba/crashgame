import os
import random
import sys
import time
import keyboard
from rich import print
from rich.console import Console
from rich.panel import Panel

console = Console

print(Panel.fit("Введи свою ставку и нажми [green]ENTER[/green]"))

bet = int(input())
print(Panel.fit("[yellow]Ставка сделана. Нажми X когда захочешь забрать деньги[/yellow]"))
time.sleep(5)


def crash(amount: int):
	x = 1.00
	crashat = random.uniform(1.01, 19.99)
	while x < crashat:
		x += 0.1
		print(Panel.fit(f"[red]{round(x, 3)}x[/red]"))
		time.sleep(0.1)
		os.system('cls' if os.name == 'nt' else 'clear')
		if keyboard.is_pressed("x"):
			print(Panel.fit(f"[green] Ты выиграл {round(amount*x, 3)}$! [/green]"))
			sys.exit()
	print(Panel.fit(f"[{round(x, 3)}x] [red]Crash![/red]"))


crash(bet)
