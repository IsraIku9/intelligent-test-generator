# 🧪 Intelligent Test Generator
AI‑Powered Automated Test Case Generation for Python Projects

This project is an LLM‑assisted test generation system developed as part of the **SEN0414 – Advanced Programming** course at **Istanbul Kültür University**.  
It analyzes Python source code, extracts function signatures, and automatically generates **pytest‑compatible test cases** using a Large Language Model (LLM).

---

## 🚀 Features

- **Static Code Analysis**  
  Extracts function names, arguments, docstrings, and source code using Python's `ast` module.

- **LLM‑Powered Test Generation**  
  Builds a structured prompt and uses an LLM to generate meaningful test cases.

- **Automatic Test File Writer**  
  Saves generated tests into organized `tests/` directory.

- **Command‑Line Interface (CLI)**  
  Simple usage:
  ```bash
  python generate_tests.py <path_to_python_file>
  ```

- **High Test Coverage**  
  The system is fully validated with **98% automated test coverage**.

---

## 📂 Project Structure

```
intelligent-test-generator/
│
├── generator/
│   ├── code_analysis.py
│   ├── llm_generation.py
│   └── test_file_writer.py
│
├── tests/
│   ├── test_cli.py
│   ├── test_code_analysis.py
│   ├── test_llm_generation.py
│   └── test_test_file_writer.py
│
├── generate_tests.py
└── README.md
```

---

## 🛠️ Installation

Clone the repository:

```bash
git clone https://github.com/IsraIku9/intelligent-test-generator.git
cd intelligent-test-generator
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## ▶️ Usage

Generate tests for any Python file:

```bash
python generate_tests.py path/to/your_file.py
```

Generated tests will appear in:

```
tests/generated/
```

---

## 🧪 Running the Test Suite

This project includes a full automated test suite with **98% coverage**.

Run all tests:

```bash
pytest --cov=generator --cov-report=term-missing
```

---

## 📊 Test Coverage Summary

| Module               | Coverage |
|----------------------|----------|
| code_analysis.py     | 100%     |
| test_file_writer.py  | 100%     |
| llm_generation.py    | 95%      |
| **Total Coverage**   | **98%**  |

---

## 📘 Course Information

This project was developed for:

**SEN0414 – Advanced Programming**  
**Istanbul Kültür University**

---


