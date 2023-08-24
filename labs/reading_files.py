example1 = "Example1.txt"

example2 = "Example2.txt"

lines = ["This is line A\n", "This is line B\n", "This is lince C\n"]


with open(example2, "+a") as testwritefile:
    print(f"Initial location: {testwritefile.tell()}")

    data = testwritefile.read()
    if not data:
        print("Read nothing")
    else:
        print(testwritefile.read())

    testwritefile.seek(0, 0)

    print(f"\nNew Location: {testwritefile.tell()}")
    data = testwritefile.read()
    if not data:
        print("Read nothing")
    else:
        print(data)

    print(f"Location after read: {testwritefile.tell()}")


with open(example2, "r") as readfile:
    with open("Example3.txt", "w") as writefile:
        for line in readfile:
            writefile.write(line)

with open("Example3.txt", "r") as testwritefile:
    print(testwritefile.read())
