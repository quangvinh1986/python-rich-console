from rich.console import Console
from rich.table import Table

table = Table(title="Danh sách các bài viết của Quangvinh1986 tháng 12/2020")

table.add_column("Số thứ tự", justify="right", style="cyan", no_wrap=True)
table.add_column("Tên bài viết", style="magenta")
table.add_column("Thời gian xuất bản", justify="right", style="green")

table.add_row("1", "Python-pdfkit Chuyển Đổi Mọi Nội Dung Sang PDF", "2020-12-06 09:46:19 GMT+0700")
table.add_row("2", "Làm Quen Với UnitTest Trong Python", "2020-12-10 09:48:38 GMT+0700")
table.add_row("3", "rich-content-on-terminal(draft)", "unknown")

console = Console()
console.print(table)
