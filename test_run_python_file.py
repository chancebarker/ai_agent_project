from calculator.functions.run_python_file import run_python_file


def test_run_python_file():
    result1 = run_python_file("calculator", "main.py")
    print(f"Test 1 (usage instructions):\n{result1}\n")

    result2 = run_python_file("calculator", "main.py", ["3 + 5"])
    print(f"Test 2 (run calculator):\n{result2}\n")

    result3 = run_python_file("calculator", "tests.py")
    print(f"Test 3 (run tests):\n{result3}\n")

    result4 = run_python_file("calculator", "../main.py")
    print(f"Test 4 (outside working dir):\n{result4}\n")

    result5 = run_python_file("calculator", "nonexistent.py")
    print(f"Test 5 (nonexistent file):\n{result5}\n")

    result6 = run_python_file("calculator", "lorem.txt")
    print(f"Test 6 (not a Python file):\n{result6}\n")


if __name__ == "__main__":
    test_run_python_file()