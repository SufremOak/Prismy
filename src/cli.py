import typer
import subprocess
from rich import print as cprint
from Core.repl import prismyRepl
from Core.web import StartWebApp

app = typer.Typer()
app_port = 3000


@app.command()
def repl():
    prismyRepl.new(__init__)

@app.command
def web():
    StartWebApp()

def main():
    # main function

if __name__ == "__main__":
    main()