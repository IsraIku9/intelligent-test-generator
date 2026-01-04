import os
from pathlib import Path
from typing import List

from openai import OpenAI
from generator.code_analysis import FunctionInfo


def build_prompt(file_path: Path, functions: List[FunctionInfo]) -> str:
    prompt = "You are an expert Python developer. Generate pytest test cases.\n\n"

    for fn in functions:
        prompt += f"Function name: {fn.name}\n"
        prompt += f"Arguments: {fn.args}\n"
        prompt += f"Docstring: {fn.docstring}\n"
        prompt += f"Source code:\n{fn.source}\n\n"

    prompt += "Return ONLY pytest test code. No explanations."
    return prompt


def generate_tests_with_llm(file_path: Path, functions: List[FunctionInfo]) -> str:
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        return "# ERROR: Missing OPENAI_API_KEY\n"

    client = OpenAI(api_key=api_key)

    prompt = build_prompt(file_path, functions)

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.3,
    )

    return response.choices[0].message["content"]
