import pathlib
from google.genai import types


# Imagine this is imported from your config.py
MAX_CHARS = 10000 

def get_file_content(working_directory, file_path):
    try:
        # 1. Setup the paths
        base_dir = pathlib.Path(working_directory).resolve()
        full_path = (base_dir / file_path).resolve()

        # 2. Security Check: Is the file actually inside the folder?
        if not str(full_path).startswith(str(base_dir)):
            return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'

        # 3. Validation: Does the file exist and is it a regular file?
        if not full_path.is_file():
            return f'Error: File not found or is not a regular file: "{file_path}"'

        # 4. Reading and Truncation
        with open(full_path, 'r', encoding='utf-8') as f:
            content = f.read(MAX_CHARS)
            
            # Check if there is exactly 1 more character left
            if f.read(1):
                content += f'\n[...File "{file_path}" truncated at {MAX_CHARS} characters]'
                
        return content

    except Exception as e:
        # 5. Catch-all for unexpected errors (permissions, etc.)
        return f"Error: {str(e)}"

schema_get_file_content = types.FunctionDeclaration(
    name="get_file_content",
    description="Reads and returns the contents of a specified file relative to the working directory",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="Path to the file to read, relative to the working directory",
            ),
        },
        required=["file_path"],
    ),
)