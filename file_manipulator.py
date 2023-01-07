import sys
import os

def isInputpathValid(inputpath):
    if not os.path.isfile(inputpath):
        print("入力ファイルが存在しません")
        return False
    return True

def reverseFile(inputpath, outputpath):
    contents = ""
    with open(inputpath, "r") as f:
        contents = f.read()
    with open(outputpath, "w") as f:
        f.write(contents[::-1] + "\n")

def copyFile(inputpath, outputpath):
    contents = ""
    with open(inputpath, "r") as f:
        contents = f.read()
    with open(outputpath, "w") as f:
        f.write(contents)

def duplicateContentsFile(inputpath, repeatCount):
    contents = ""
    with open(inputpath, "r") as f:
        contents = f.read()
    with open(inputpath, "w") as f:
        f.write(contents * int(repeatCount))

def replaceStringFile(inputpath, needle, newString):
    contents = ""
    with open(inputpath, "r") as f:
        contents = f.read()
    with open(inputpath, "w") as f:
        f.write(contents.replace(needle, newString))

def main():
    argvLen = len(sys.argv)
    if argvLen < 2:
        print("入力が正しくありません")
        sys.exit(1)
    command = sys.argv[1]

    if command == "reverse":
        if argvLen != 4:
            print("入力が正しくありません")
            sys.exit(1)
        inputpath = sys.argv[2]
        outputpath = sys.argv[3]
        if not isInputpathValid(inputpath):
            sys.exit(1)
        reverseFile(inputpath, outputpath)
    elif command == "copy":
        if argvLen != 4:
            print("入力が正しくありません")
            sys.exit(1)
        inputpath = sys.argv[2]
        outputpath = sys.argv[3]
        if not isInputpathValid(inputpath):
            sys.exit(1)
        copyFile(inputpath, outputpath)
    elif command == "duplicate-contents":
        if argvLen != 4:
            print("入力が正しくありません")
            sys.exit(1)
        inputpath = sys.argv[2]
        repeatCount = sys.argv[3]
        if not isInputpathValid(inputpath):
            sys.exit(1)
        if not repeatCount.isdecimal():
            print("繰り返し回数は数字で入力してください")
            sys.exit(1)
        duplicateContentsFile(inputpath, repeatCount)
    elif command == "replace-string":
        if argvLen != 5:
            print("入力が正しくありません")
            sys.exit(1)
        inputpath = sys.argv[2]
        if not isInputpathValid(inputpath):
            return 1
        needle = sys.argv[3]
        newString = sys.argv[4]
        replaceStringFile(inputpath, needle, newString)
    else:
        print("無効なコマンドです")

if __name__ == "__main__":
    main()