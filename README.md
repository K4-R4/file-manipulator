# File manipulator
## 説明
ファイルを操作するためのプログラムです。
## 使用方法
- ### reverse
入力ファイルの内容を逆にした出力ファイルを作成します。
```
python3 file-manipulator.py reverse inputpath outputpath
```
- ### copy
入力ファイルのコピーを作成して出力します。
```
python3 file-manipulator.py copy inputpath outputpath
```
- ### duplicate-contents
入力ファイルの内容を読み込み、その内容をn回入力ファイルに複製します。
```
python3 file-manipulator.py duplicate-contents inputpath n
```
- ### replace-string
入力ファイルにある文字列'needle'を検索し、'needle'のすべてを'newstring'に置き換えます。
```
python3 file-manipulator.py replace-string inputpath needle newstring
```
