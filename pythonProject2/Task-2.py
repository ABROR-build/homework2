import os

rootdir = "C:/Users/abror/OneDrive/Desktop/Новая папка"
for file in os.listdir(rootdir):
    d = os.path.join(rootdir, file)
    if os.path.isdir(d):
        print(d)