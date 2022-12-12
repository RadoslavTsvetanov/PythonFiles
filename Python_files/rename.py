import os


def rename(old_name, new_name):
    os.rename(old_name, new_name)


def main():
    old_name = r"name.txt"
    new_name = r"hi.txt"
    rename(old_name, new_name)


main()
