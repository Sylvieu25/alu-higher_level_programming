#!/usr/bin/python3
# 4-hidden_discovery.py
# A script that prints all names defined in the compiled module hidden_4.pyc,
# excluding names that start with "__".

if __name__ == "__main__":
    import hidden_4

    names = dir(hidden_4)
    for name in sorted(names):
        if not name.startswith("__"):
            print(name)
