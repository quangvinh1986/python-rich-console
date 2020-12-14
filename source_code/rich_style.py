from rich.console import Console
from rich.style import Style
console = Console()

base_style = Style.parse("red")
console.print("Hello World!", style = base_style)
console.print("Welcome to codelearn", style = base_style + Style(underline=True) + Style(link="https://codelearn.io/"))
