from pathlib import Path
import subprocess
import sys


def test_cli_missing_file():
    result = subprocess.run(
        [sys.executable, "generate_tests.py", "missing.py"],
        capture_output=True,
        text=True,
    )
    assert "Error" in result.stdout
