import os

schema_get_files_info = {
    "type": "function",
    "function": {
        "name": "get_files_info",
        "description": "Lists files in a specified directory relative to the working directory, providing file size and directory status",
        "parameters": {
            "type": "object",
            "properties": {
                "directory": {
                    "type": "string",
                    "description": "Directory path to list files from, relative to the working directory (default is the working directory itself)",
                },
            },
        },
    },
}


def get_files_info(working_directory: str, directory: str = ".") -> str:
    try:
        path =  os.path.abspath(working_directory)
        target_dir = os.path.normpath(os.path.join(path, directory))
        if os.path.commonpath([path, target_dir]) == path:
            if not os.path.isdir(target_dir):
                return f'Error: "{directory}" is not a directory'
            files:list[str] = os.listdir(target_dir)
            print(f"Result for '{directory}' directory:")
            for file in files:
                    file_path = os.path.join(target_dir, file)
                    print(f"- {file}: file_size={os.path.getsize(file_path)} bytes, is_dir={os.path.isdir(file_path)}")
            return  f'Success: "{directory}" is within the working directory'
        else:
            return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'
    except Exception as e:
        return f"Error: {e}"
