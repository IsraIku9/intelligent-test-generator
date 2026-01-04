#!/usr/bin/env python3
import argparse
from pathlib import Path

from generator.code_analysis import analyze_code
from generator.llm_generation import generate_tests_with_llm
from generator.test_file_writer import write_test_file


def main():
    parser = argparse.ArgumentParser(
        description="Intelligent Test Generation System – AI-powered test case generation"
    )
    parser.add_argument("file", type=str, help="Python module to analyze")
    parser.add_argument("--print-only", action="store_true", help="Print tests instead of writing file")
    parser.add_argument("--no-llm", action="store_true", help="Disable LLM and generate placeholder tests")
    args = parser.parse_args()

    file_path = Path(args.file)
    if not file_path.exists():
        print("Error: File not found.")
        return 1

    print(f"Analyzing {file_path}...")

    functions = analyze_code(file_path)

    if args.no_llm:
        test_code = "# Placeholder tests\n"
        for fn in functions:
            test_code += f"def test_{fn.name}_placeholder():\n    assert True\n\n"
    else:
        test_code = generate_tests_with_llm(file_path, functions)

    if args.print_only:
        print(test_code)
    else:
        write_test_file(file_path, test_code)
        print("Generated tests written to tests_generated/")

    return 0


if __name__ == "__main__":
    main()