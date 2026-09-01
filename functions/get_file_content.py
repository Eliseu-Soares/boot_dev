import os
from config import MAX_CHARS

def get_file_content(working_directory: str, file_path: str) -> str:
    try:
        
        path =  os.path.abspath(working_directory)
        target_dir = os.path.normpath(os.path.join(path, file_path))
        if os.path.commonpath([path, target_dir]) == path:
            if not os.path.isfile(target_dir):
                return f'Error: File not found or is not a regular file: "{file_path}"'
            with open(target_dir, "r", encoding="utf") as file:
                content = file.read(MAX_CHARS)
                if file.read(1):
                    content += f'[...File "{file_path}" truncated at {MAX_CHARS} characters]'
            return content
        else:
            return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'
    except Exception as e:
        return f"Error: {e}"
