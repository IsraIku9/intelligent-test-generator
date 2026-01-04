from pathlib import Path
from generator.code_analysis import analyze_code


def test_analyze_code_extracts_functions(tmp_path: Path):
    file = tmp_path / "demo.py"
    file.write_text("def add(a, b):\n    return a + b\n")

    functions = analyze_code(file)
    assert len(functions) == 1
    assert functions[0].name == "add"
    assert functions[0].args == ["a", "b"]
