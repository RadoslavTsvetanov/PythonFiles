def func(name):
    with open("test.txt", "r") as contents:
        data = [[]]
        for i in contents:
            data.append(i)
        for i in data:
            print(i)
            print("h")
        reversed = data[::-1]
        for i in reversed:
            print(i)
        with open(name, "w") as NewFile:
            for i in reversed:
                NewFile.write(i)


def main():
    func("NewNew.txt")


main()
