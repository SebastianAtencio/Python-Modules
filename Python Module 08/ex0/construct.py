import sys
import os
import site


def check_matrix() -> None:
    is_venv = sys.prefix != sys.base_prefix
    current_python = sys.executable
    if not is_venv:
        print()
        print("MATRIX STATUS: You're still plugged in")
        print()
        print(f"Current Python: {current_python}")
        print("Virtual Environment: None detected")
        print()
        print("WARNING: You're in the global environment!")
        print("The machines can see everything you install.")
        print()
        print("To enter the construct, run:")
        print("python -m venv matrix_env")
        print("source matrix_env/bin/activate # On Unix")
        print("matrix_env\\Scripts\\activate # On Windows")
        print()
        print("Then run this program again.")
    else:
        venv_name = os.path.basename(sys.prefix)
        package_paths = site.getsitepackages()
        print()
        print("MATRIX STATUS: Welcome to the construct")
        print()
        print(f"Current Python: {current_python}")
        print(f"Virtual Environment: {venv_name}")
        print(f"Enviroment Path: {sys.prefix}")
        print()
        print("SUCCESS: You're in an isolated environment!")
        print("Safe to install packages without affecting")
        print("the global system.")
        print()
        print("Package installation path")
        print(f"{package_paths[0]}")


if __name__ == "__main__":
    check_matrix()
