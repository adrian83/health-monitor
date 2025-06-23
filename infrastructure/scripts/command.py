import subprocess


def execute(command: str, dir: str='.'):
    try:
        subprocess.run(
            command.split(" "),
            cwd=dir,
            check=True)
    except subprocess.CalledProcessError as e:
        print(f"Cannot run command: '{command}', error: {e}")