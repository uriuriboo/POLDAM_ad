# POLDAM_ad


## poldamdot_to_easygraph.py

POLDAMのから出力されたグラフを

$$
N M
v_1 classname:methodname CFH CPH
.
.
v_n classname:methodname CFH CPH
V_i_1 V_j_1
.
.
V_i_m V_j_m
$$
に変換して他のプログラムから読み込みやすいようにする

## compare_same_version_hash.py

同型なマークル木に対してpoldamdot_to_easygraph.pyの出力結果を一つのファイルにまとめたものを準備する
それを読み込んでハッシュ値が変化したメソッドを出力する

## get_method.py

指定したメソッドのコードを取得
