from calculator.functions.write_file import write_file


def test_write_file():
    result1 = write_file("calculator", "lorem.txt", "wait, this isn't lorem ipsum")
    print(f"Test 1 (write new file): {result1}")

    result2 = write_file("calculator", "pkg/morelorem.txt", "lorem ipsum dolor sit amet")
    print(f"Test 2 (write with nested dirs): {result2}")

    result3 = write_file("calculator", "/tmp/temp.txt", "this should not be allowed")
    print(f"Test 3 (outside working dir): {result3}")


if __name__ == "__main__":
    test_write_file()