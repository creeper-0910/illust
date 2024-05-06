import os

files = os.listdir("./inagi/")
files = [os.path.join("./inagi/", f) for f in files]
files.sort(key=os.path.getmtime, reverse=True)
result = [file[1:] for file in files]
with open('data.txt', 'w', encoding='utf-8') as f:
    f.write("\n".join(result))