from calculator.functions.get_file_content import get_file_content

def run_tests():
    print("--- Starting Tests for get_file_content ---")

    # 1. Test Truncation with lorem.txt
    print("\nTesting: lorem.txt (Truncation Check)")
    content = get_file_content("calculator", "lorem.txt")
    
    # We check if the content is longer than the limit and contains the message
    print(f"Total length of returned string: {len(content)}")
    if "[...File" in content and "truncated" in content:
        print("Result: PASS (Truncation message found)")
    else:
        print("Result: FAIL (No truncation message found)")

    # 2. Test valid files
    print("\nTesting: Valid files")
    print(get_file_content("calculator", "main.py"))
    print(get_file_content("calculator", "pkg/calculator.py"))

    # 3. Test Security (Outside directory)
    print("\nTesting: Security (Accessing /bin/cat)")
    print(get_file_content("calculator", "/bin/cat"))

    # 4. Test Missing File
    print("\nTesting: Missing file")
    print(get_file_content("calculator", "pkg/does_not_exist.py"))

if __name__ == "__main__":
    run_tests()