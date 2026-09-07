import os
from config import MAX_CHARS

schema_get_file_content = {
    "type": "function",
    "function": {
        "name": "get_file_content",
        "description": "This function get the content of a file, if the file has more than 20.000 Characters the function truncate the content and show a messagem to explain it",
        "parameters": {
            "type": "object",
            "properties": {
                "file_path": {
                    "type": "string",
                    "description": "This is a path for the argument file_path",
                },
            },
        },
    },
}

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
