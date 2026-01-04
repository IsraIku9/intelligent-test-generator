from pathlib import Path


def write_test_file(file_path: Path, test_code: str):
    out_dir = Path("tests_generated")
    out_dir.mkdir(exist_ok=True)

    out_file = out_dir / f"test_generated_{file_path.stem}.py"
    out_file.write_text(test_code)
