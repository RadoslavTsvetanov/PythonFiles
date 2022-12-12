def func(name, arr):
    with open(name, 'a') as NewFile:
        for i in arr:
            NewFile.write(i)
            NewFile.write("\n")


def main():
    name = 'newnewnew.txt'
    arr = ["wd", "wd", "wd", "wd", "wd", "wd", "wd"]
    func(name, arr)


main()
