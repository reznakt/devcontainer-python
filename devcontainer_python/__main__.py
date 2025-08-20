#!/usr/bin/env python3

from rich.console import Console
from rich.panel import Panel
from rich.text import Text

from . import PACKAGE_NAME, PACKAGE_VERSION


def main() -> None:
    console = Console()

    welcome_message = Text.from_markup(
        f":tada: Hello from [bold cyan]{PACKAGE_NAME}[/bold cyan] version"
        f" [green]{PACKAGE_VERSION}[/green]! :sparkles:",
        justify="center",
    )

    console.print(
        Panel(
            welcome_message,
            title="[bold]Welcome[/bold]",
            border_style="blue",
            padding=(1, 2),
        )
    )

    console.print()

    warning_message = (
        ":bell: [bold]Don't forget to customize this template![/bold] :bell:"
        "\n\n"
        "Make sure to update project details and other metadata in the "
        "project configuration files (e.g., [bold]pyproject.toml[/bold])."
    )

    console.print(
        Panel(
            Text.from_markup(warning_message, justify="center"),
            title="[bold yellow]Important Reminder[/bold yellow]",
            border_style="yellow",
            padding=(1, 2),
        )
    )


if __name__ == "__main__":
    main()
