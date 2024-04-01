import os
import subprocess
from getpass import getpass
from tqdm import tqdm
from rich.console import Console
from rich.style import Style

def main():
    console = Console()
    api_token = getpass("Enter your PyPI API token: ")

    try:
        # Build the package
        console.print("Building the package...", style="bold green")
        with tqdm(total=100, desc="Building", unit="B", unit_scale=True, unit_divisor=1024) as progress:
            process = subprocess.Popen(["python", "setup.py", "sdist", "bdist_wheel"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            while True:
                output = process.stdout.readline()
                if output == b'' and process.poll() is not None:
                    break
                if output:
                    progress.update(len(output))
        rc = process.poll()
        if rc != 0:
            console.print(f"[bold red]Error building package. Return code: {rc}[/bold red]")
            return

        build_time = progress.format_interval(progress.format_dict["elapsed"])
        console.print(f"Package built in [bold green]{build_time}[/bold green]")

        # Publish the package to PyPI
        console.print("Publishing the package to PyPI...", style="bold green")
        with tqdm(total=100, desc="Uploading", unit="B", unit_scale=True, unit_divisor=1024) as progress:
            process = subprocess.Popen(["twine", "upload", "--skip-existing", "dist/*", "--username", "__token__", "--password", api_token], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            while True:
                output = process.stdout.readline()
                if output == b'' and process.poll() is not None:
                    break
                if output:
                    progress.update(len(output))
        rc = process.poll()
        if rc != 0:
            console.print(f"[bold red]Error publishing package. Return code: {rc}[/bold red]")
            return

        upload_time = progress.format_interval(progress.format_dict["elapsed"])
        console.print(f"Package published in [bold green]{upload_time}[/bold green]")
        console.print("Package published successfully! 🚀", style="bold green")

    except Exception as e:
        console.print(f"[bold red]Error: {e}[/bold red]")