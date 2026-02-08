#!/usr/bin/env python3
"""
Test script to validate the Todo Console Application functionality
"""

from src.cli.todo_cli import TodoCLI


def test_application():
    """Test the complete functionality of the todo application."""
    print("=== Todo Console Application Test ===")

    # Create a single CLI instance to maintain state during the test
    cli = TodoCLI()

    print("\n1. Testing ADD command:")
    cli.handle_command("add", ["Buy groceries"])
    cli.handle_command("add", ["Call mom"])
    cli.handle_command("add", ["Write report"])
    cli.handle_command("add", ["Fix", "bug", "in", "production", "high"])
    cli.handle_command("add", ["Team", "meeting", "tomorrow", "medium", "2026-02-06"])

    print("\n2. Testing LIST command:")
    cli.handle_command("list", [])

    print("\n3. Testing SEARCH command:")
    cli.handle_command("search", ["meeting"])
    cli.handle_command("search", ["bug"])

    print("\n4. Testing FILTER command:")
    cli.handle_command("filter", ["high"])
    cli.handle_command("filter", ["medium"])

    print("\n5. Testing STATS command:")
    cli.handle_command("stats", [])

    print("\n6. Testing COMPLETE command:")
    cli.handle_command("complete", ["1"])

    print("\n7. Testing LIST command again (to see completed task):")
    cli.handle_command("list", [])

    print("\n8. Testing UPDATE command:")
    cli.handle_command("update", ["3", "Updated", "report", "with", "details"])

    print("\n9. Testing LIST command again (to see updated task):")
    cli.handle_command("list", [])

    print("\n10. Testing DELETE command:")
    cli.handle_command("delete", ["2"])

    print("\n11. Testing LIST command again (to see deleted task):")
    cli.handle_command("list", [])

    print("\n12. Testing STATS command again:")
    cli.handle_command("stats", [])

    print("\n13. Testing HELP command:")
    cli.handle_command("help", [])

    print("\n14. Testing error handling:")
    cli.handle_command("add", [])  # Should show error
    cli.handle_command("complete", ["999"])  # Should show error
    cli.handle_command("delete", ["abc"])  # Should show error
    cli.handle_command("update", ["999", "new", "description"])  # Should show error
    cli.handle_command("search", [])  # Should show error
    cli.handle_command("filter", ["invalid"])  # Should show error
    cli.handle_command("unknown", [])  # Should show error

    print("\n=== Test completed ===")


if __name__ == "__main__":
    test_application()