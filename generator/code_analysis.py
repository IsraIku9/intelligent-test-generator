import ast
from dataclasses import dataclass
from pathlib import Path
from typing import List, Optional


@dataclass
class FunctionInfo:
    name: str
    args: List[str]
    docstring: Optional[str]
    source: str


def analyze_code(file_path: Path) -> List[FunctionInfo]:
    text = file_path.read_text()
    tree = ast.parse(text)

    functions = []

    for node in ast.walk(tree):
        if isinstance(node, ast.FunctionDef):
            args = [arg.arg for arg in node.args.args]
            doc = ast.get_docstring(node)
            source = ast.get_source_segment(text, node)
            functions.append(FunctionInfo(node.name, args, doc, source))

    return functions
