#!/usr/bin/env python3
"""
Todo Console Application
A simple command-line todo list manager with add, list, complete, and delete functionality.
"""

import sys
from src.cli.todo_cli import TodoCLI


def main():
    """Main entry point for the application."""
    if len(sys.argv) < 2:
        print("Error: Please provide a command (add, list, complete, delete, help)")
        print("Usage: python main.py [command] [arguments]")
        print("Run 'python main.py help' for available commands")
        sys.exit(1)

    command = sys.argv[1]
    args = sys.argv[2:]

    cli = TodoCLI(data_file="tasks.json")
    cli.handle_command(command, args)


if __name__ == "__main__":
    main()