def func(name):
    with open("test.txt", "r") as contents:
        with open(name, "w") as newFile:
            for i in contents:
                newFile.write(i)
                print(i)
                print("h")


def main():
    func("New.txt")


main()
