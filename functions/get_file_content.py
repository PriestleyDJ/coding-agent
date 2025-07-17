import os
from config import MAX_CHARS
from google.genai import types


def get_file_content(working_directory, file_path):
    abs_working_dir = os.path.abspath(working_directory)
    target_dir = os.path.abspath(os.path.join(working_directory, file_path))

    if not target_dir.startswith(abs_working_dir):
        return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'
    if not os.path.isfile(target_dir):
        return f'Error: File not found or is not a regular file: "{file_path}"'

    try:
        with open(target_dir, "r") as f:
            content = f.read(MAX_CHARS)
            if os.path.getsize(target_dir) > MAX_CHARS:
                content += f'[...File "{file_path}" truncated at 10000 characters]'
            return content
    except Exception as e:
        return f'Error reading file "{file_path}": {e}'


schema_get_file_content = types.FunctionDeclaration(
    name="get_file_content",
    description="Read the contents of the file from the specified file path, constrained to the current working directory.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="The file path to the file that will be read, relative to the current working directory.",
            )
        },
    ),
)
