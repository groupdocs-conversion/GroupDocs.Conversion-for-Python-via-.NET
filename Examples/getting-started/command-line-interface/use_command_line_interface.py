"""Drive the ``groupdocs-conversion`` command-line interface from Python.

Installing the ``groupdocs-conversion-net`` wheel puts a
``groupdocs-conversion`` console script on ``PATH``; it is also reachable
as ``python -m groupdocs.conversion``. This example shells out to it the
same way a CI step, Make rule, or shell pipeline would — convert a
document, inspect it, and list the target formats valid for an input.

See https://docs.groupdocs.com/conversion/python-net/getting-started/command-line-interface/
for the full command reference.
"""
import subprocess
import sys


def run_cli(*args):
    """Invoke the CLI via ``python -m groupdocs.conversion`` and echo it."""
    cmd = [sys.executable, "-m", "groupdocs.conversion", *args]
    print("$ groupdocs-conversion " + " ".join(args))
    result = subprocess.run(cmd, capture_output=True, text=True)
    if result.stdout:
        print(result.stdout.rstrip())
    if result.returncode != 0:
        print(result.stderr.rstrip())
        raise RuntimeError(f"CLI exited with code {result.returncode}")
    print()
    return result


def use_command_line_interface():
    # Convert — the target format is inferred from the output extension.
    run_cli("convert", "./business-plan.docx", "./business-plan.pdf")

    # Inspect a document — prints format, size, and page count.
    run_cli("info", "./business-plan.pdf")

    # List the target formats valid for a given input document.
    run_cli("list-formats", "./business-plan.docx")


if __name__ == "__main__":
    use_command_line_interface()
