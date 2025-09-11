#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
A simple Hello World program in Python.
"""

def greet(name: str = "World") -> str:
    """
    Generate a greeting message.
    
    Args:
        name (str): The name to greet. Defaults to "World".
        
    Returns:
        str: The greeting message.
    """
    return f"Hello, {name}!"

def main() -> None:
    """Main function to run the program."""
    message = greet()
    print(message)
    
    # Greet a specific person
    personalized_message = greet("Alice")
    print(personalized_message)

if __name__ == "__main__":
    main()
