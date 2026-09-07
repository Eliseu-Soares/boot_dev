import os

schema_write_file = {
    "type": "function",
    "function": {
        "name": "write_file",
        "description": "This function write in file, if success return Successfully wrote to...Otherwise prefix Error:error_detail ",
        "parameters": {
            "type": "object",
            "properties": {
                "file_path": {
                    "type": "string",
                    "description": "This is a path for the argument file_path",
                },
                "content": {
                    "type": "string",
                    "description": "This is the argument for de file",
                },
            },
        },
    },
}

def write_file(working_directory: str, file_path: str, content: str) -> str:
    try:
        path =  os.path.abspath(working_directory)
        target_dir = os.path.normpath(os.path.join(path, file_path))
        if os.path.commonpath([path, target_dir]) == path:
            if os.path.isdir(target_dir):
                return f'Error: Cannot write to "{file_path}" as it is a directory'
            os.makedirs(os.path.dirname(target_dir), exist_ok=True)
            with open(target_dir, "w", encoding="utf-8") as file:
                file.write(content)
            return  f'Successfully wrote to "{file_path}" ({len(content)} characters written)'
        else:
            return f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory'
    except Exception as e:
        return f"Error: {e}"
