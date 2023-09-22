import sqlite3
import os

# ===================================================
# 事前にdbが存在するか確認し、存在したら削除
db_path = r"C:\Users\nao23\Documents\Python_Projects\python_sqlite3_tutorial_311\tutorial.db"
if os.path.exists(db_path) == True:
    os.remove(db_path)
else: pass


# ===================================================
# DBを作成する（既に作成されていたらこのDBに接続する）
dbname = 'tutorial.db'
conn = sqlite3.connect(dbname)


# ===================================================
# SQLiteを操作するためのカーソルを作成
cur = conn.cursor()

# SQLでテーブルの作成
cur.execute(
    'CREATE TABLE items(id INTEGER PRIMARY KEY AUTOINCREMENT, name STRING, price INTEGER)'
    )

# SQLでデータ登録
cur.execute(
    'INSERT INTO items values(0, "りんご", 100)'
    )

# 一括登録するデータを設定
inserts = [
    (1, "みかん", 80),
    (2, "ぶどう", 150),
    (3, "バナナ", 60)
    ]

# SQLで一括データ登録
cur.executemany(
    'INSERT INTO items values(?, ?, ?)', inserts
    )


# ===================================================
# SQLでデータ検索
cur.execute(
    'SELECT * FROM items'
    )

print('\n')
print(cur)
print(type(cur))

# 取得したデータはカーソルの中に入る
print('\n')
for row in cur:
    print(row)
    print(type(row))


# ===================================================
# SQLでデータ更新
cur.execute(
    'UPDATE items SET price = 260 WHERE id = "3"'
    )

# SQLでデータ削除後に検索
cur.execute(
    'DELETE FROM items WHERE id = "2"'
    )

cur.execute(
    'SELECT * FROM items'
    )

print('\n')
for row in cur:
    print(row)


# ===================================================
# コミットしないと登録が反映されない
conn.commit()

# DBとの接続を閉じる(必須)
conn.close()
