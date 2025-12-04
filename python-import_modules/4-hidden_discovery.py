#!/usr/bin/python3
import importlib.util

if __name__ == "__main__":
    # Load the compiled module hidden_4.pyc
    spec = importlib.util.spec_from_file_location("hidden_4", "hidden_4.pyc")
    hidden_4 = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(hidden_4)

    # Get all names, filter out private names, and sort
    names = [name for name in dir(hidden_4) if not name.startswith("__")]

    # Print names
    for name in sorted(names):
        print(name)

