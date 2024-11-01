# クォーテーションが、ダブルではなく、シングルになっている場合
"""
hoge
"""

# Listの要素間のスペースが不ぞろいかつ、改行されてしまっている
# ⇒ 要素間のスペースをそろえて、改行を無くしてほしい
list_1 = [1, 2, 3, 4, 5]

# Listの要素のカンマが要素の前に置いているものと後に置いているものとが混在している
# ⇒ 要素間のカンマをそろえてほしい
list_2 = ["a", "b", "c", "d", "e"]

# 正しく記載している関数 ⇒ 書き換わらないことを期待
def func_1(vals: list) -> int:
    return sum(vals)


# 引数が小文字ではなく、大文字 ⇒ 小文字に書き換わってほしい
def func_2(VALS: list) -> int:
    return sum(VALS)


# 関数名が小文字ではなく、大文字 ⇒ 全て小文字に書き換わってほしい
def Func_3(vals: list) -> int:
    return sum(vals)


# 使っていないライブラリをimportする ⇒ 1行で複数importしていること、ioとtimeは使っていないから削除してほしい
def func_4(vals: list) -> int:
    import os
    import io, time

    return sum(vals), os.getcwd()


print(f"{list_1=}")
print(f"{list_2=}")


print(f"{func_1(list_1)=}")
print(f"{func_2(list_1)=}")
print(f"{Func_3(list_1)=}")
print(f"{func_4(list_1)=}")
