import os

caminho = "C:\\Users\\felip\\AppData\\Local\\Programs\\Microsoft VS Code"

if os.path.exists(caminho):
    print("Essa localização existe")
    if os.path.isfile(caminho):
        print("Isso é um arquivo")
    elif os.path.isdir(caminho):
        ("Isso é uma pasta")
else:
    print("Essa localização não existe")