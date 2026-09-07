import os
import subprocess

schema_run_python_file = {
    "type": "function",
    "function": {
        "name": "run_python_file",
        "description": "This function run a python file, it have handle error",
        "parameters": {
            "type": "object",
            "properties": {
                "file_path": {
                    "type": "string",
                    "description": "This is a path for the argument file_path(python file)",
                },
                "args": {
                    "type": "list",
                    "description": "This is the arguments passed for the python file, this arguments can be empty(Is optional)",
                },
            },
        },
    },
}

def run_python_file(
    working_directory: str, file_path: str, args: list[str] | None = None
) -> str:
    try:
        path =  os.path.abspath(working_directory)
        target_dir = os.path.normpath(os.path.join(path, file_path))
        if os.path.commonpath([path, target_dir]) == path:
            if not os.path.isfile(target_dir):
                return f'Error: "{file_path}" does not exist or is not a regular file'
            if not file_path.endswith(".py"):
                return f'Error: "{file_path}" is not a Python file'
            command = ["python", target_dir]
            if args:
                command.extend(args)
            result = subprocess.run(
                command,
                text=True,
                timeout=30,
                capture_output=True,
                cwd=working_directory
                
            )
            output_return: str = ""
            if result.returncode != 0:
               output_return += f"Process exited with code {result.returncode}"
            if not result.stdout and not result.stderr:
                output_return += f"No output produced"
            output_return += f'STDOUT: {result.stdout} STDERR: {result.stderr}'
            return  output_return
        else:
            return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'
    except Exception as e:
        return f"Error: {e}"
    