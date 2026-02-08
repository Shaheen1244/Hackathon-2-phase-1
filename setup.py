#!/usr/bin/env python3
"""
Setup script for the Todo Console Application.
This script helps set up the virtual environment for the project.
"""

import os
import sys
import subprocess
import venv


def create_virtual_environment():
    """Create a virtual environment for the project."""
    env_name = "todo-app-env"

    print(f"Creating virtual environment: {env_name}")
    venv.create(env_name, with_pip=True)
    print(f"Virtual environment '{env_name}' created successfully!")

    print("\nTo activate the virtual environment:")
    print("# On Windows:")
    print(f"  {env_name}\\Scripts\\activate")
    print("# On macOS/Linux:")
    print(f"  source {env_name}/bin/activate")

    print(f"\nAfter activation, you can run the Todo Console App with:")
    print("  python main.py [command] [arguments]")


def main():
    """Main function to run the setup."""
    print("Todo Console Application - Setup Script")
    print("=" * 45)

    # Check Python version
    if sys.version_info < (3, 8):
        print("Warning: This application requires Python 3.8 or higher.")
        print(f"Your current version is {sys.version}")
        return 1

    create_virtual_environment()

    print("\nSetup complete! The Todo Console App has no external dependencies,")
    print("so once you activate the virtual environment, you can run it directly.")
    return 0


if __name__ == "__main__":
    sys.exit(main())