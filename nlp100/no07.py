#!/usr/bin/env python3
"""
07. テンプレートによる文生成
引数x, y, zを受け取り「x時のyはz」という文字列を返す関数を実装せよ．
さらに，x=12, y="気温", z=22.4として，実行結果を確認せよ．
"""
template = "{}時の{}は{}"
x = 12
y = "気温"
z = 22.4
print(template.format(x, y, z))
