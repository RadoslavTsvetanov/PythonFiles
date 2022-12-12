

def func(name, n):
    br = 1
    with open("test.txt", "r") as content:
        with open(name, "w") as NewFile:
            for i in content:
                if(br % n == 0):
                    NewFile.write(i)
                br += 1


def main():
    func("newfile.txt", 3)


main()
