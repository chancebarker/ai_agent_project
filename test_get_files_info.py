from calculator.functions.get_files_info import get_files_info

def run_tests():
    # Test 1: Valid current directory
    print("get_files_info('calculator', '.'):")
    print(f"Result for current directory:\n{get_files_info('calculator', '.')}\n")

    # Test 2: Valid subdirectory
    print("get_files_info('calculator', 'pkg'):")
    print(f"Result for 'pkg' directory:\n{get_files_info('calculator', 'pkg')}\n")

    # Test 3: Unauthorized absolute path
    print("get_files_info('calculator', '/bin'):")
    print(f"Result for '/bin' directory:\n    {get_files_info('calculator', '/bin')}\n")

    # Test 4: Unauthorized relative path traversal
    print("get_files_info('calculator', '../'):")
    print(f"Result for '../' directory:\n    {get_files_info('calculator', '../')}\n")

if __name__ == "__main__":
    run_tests()