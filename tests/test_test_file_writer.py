from pathlib import Path
from generator.test_file_writer import write_test_file


def test_write_test_file(tmp_path: Path, monkeypatch):
    monkeypatch.chdir(tmp_path)

    write_test_file(Path("module.py"), "def test_x(): pass")

    out = Path("tests_generated/test_generated_module.py")
    assert out.exists()
    assert "test_x" in out.read_text()
