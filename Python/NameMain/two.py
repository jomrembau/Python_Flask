import one

print("Top level in two.py")

one.func()

if __name__ == "__main__":
    print("Two.py ran directly")
else:
    print("Two.ps imported")