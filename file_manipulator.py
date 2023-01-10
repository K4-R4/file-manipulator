import sys

# Reverse the contents
def reverseFile(inputpath, outputpath):
    contents = ""
    with open(inputpath, "r") as f:
        contents = f.read()
    with open(outputpath, "w") as f:
        f.write(contents[::-1] + "\n")

# Copy the contents
def copyFile(inputpath, outputpath):
    contents = ""
    with open(inputpath, "r") as f:
        contents = f.read()
    with open(outputpath, "w") as f:
        f.write(contents)

# Duplicate the contents
def duplicateContentsFile(inputpath, repeatCount):
    contents = ""
    with open(inputpath, "r") as f:
        contents = f.read().strip()
    with open(inputpath, "w") as f:
        f.write((contents + "\n") * int(repeatCount))

# Replace specific strings in the file
def replaceStringFile(inputpath, needle, newString):
    contents = ""
    with open(inputpath, "r") as f:
        contents = f.read()
    with open(inputpath, "w") as f:
        f.write(contents.replace(needle, newString))

def main():
    command = sys.argv[1]
    try:
        if command == "reverse":
            inputpath = sys.argv[2]
            outputpath = sys.argv[3]
            reverseFile(inputpath, outputpath)
        elif command == "copy":
            inputpath = sys.argv[2]
            outputpath = sys.argv[3]
            copyFile(inputpath, outputpath)
        elif command == "duplicate-contents":
            inputpath = sys.argv[2]
            repeatCount = sys.argv[3]
            duplicateContentsFile(inputpath, repeatCount)
        elif command == "replace-string":
            inputpath = sys.argv[2]
            needle = sys.argv[3]
            newString = sys.argv[4]
            replaceStringFile(inputpath, needle, newString)
        else:
            print("無効なコマンドです")
    except IndexError:
        print("引数の数が正しくありません")
    except FileNotFoundError:
        print("入力ファイルが存在しません")
    except ValueError:
        print("繰り返し回数は数字で入力してください")

if __name__ == "__main__":
    main()