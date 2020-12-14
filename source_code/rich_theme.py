from rich.console import Console
from rich.theme import Theme

my_theme = Theme({
    "issue_color" : "white underline",
    "warning_color": "cyan",
    "major_color": "yellow",
    "cirtical_color": "magenta",
    "fatal_color": "red",
    "highlight_background": "on blue",
    "highlight_number_background": "on green"
})

console = Console(theme=my_theme)

console.print("This is information", style="issue_color")
console.print("[warning_color]warning_count: [highlight_number_background] 100 [/highlight_number_background] issues[/warning_color]")
console.print("[highlight_background][fatal_color]fatal_count: [highlight_number_background] 100 [/highlight_number_background] issues[/fatal_color][highlight_background]")
