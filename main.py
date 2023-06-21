import os


i:int = 0
for f in os.listdir(os.getcwd()):
    if os.path.isfile(f) and f != "main.py":
        name, extension = os.path.splitext(f)
        os.rename(f, "nuevo" + str(i) + extension)
        i += 1
