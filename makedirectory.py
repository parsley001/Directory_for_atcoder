import datetime
import os

t_delta = datetime.timedelta(hours=9)
JST = datetime.timezone(t_delta, 'JST')
now = datetime.datetime.now(JST)

# YYYYMMDDhhmmss形式に書式化
d = now.strftime('%Y%m%d')
print(d)


SAMPLE_DIR = str(d)

# 存在チェック
if os.path.isdir(SAMPLE_DIR):
    print("ディレクトリが既に存在しています")
else:
    os.makedirs(SAMPLE_DIR)
    filename = ["a","b","c","d","e","f","g","x"]
    for i in filename:
        path = "./" + SAMPLE_DIR + "/" + i + ".cpp"
        f = open(path, 'w') 
        f.write('')  # 何も書きこまずファイルを作成
        f.close()
    print("ディレクトリを作成しました")