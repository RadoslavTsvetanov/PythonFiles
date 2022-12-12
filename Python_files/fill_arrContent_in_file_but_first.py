def func(name, arr):
    with open("test.txt", "r") as contents:
        data = []
        for i in arr:
            data.append(i)
        for i in contents:
            data.append(i)
        for i in data:
            print(i)
        with open("test.txt", "w") as NewFile:
            for i in data:
                NewFile.write(i)
                NewFile.write("\n")


def main():
    arr = ["wd", "wd", "wd", "wd", "wd", "wd", "wd"]
    name = "test.txt"
    func(name, arr)


main()
