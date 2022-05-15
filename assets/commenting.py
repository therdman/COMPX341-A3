from pathlib import Path
import os

files = []
for path in Path(os.getcwd()).rglob("*.ts"):
    files.append(path)

for file in files:
    i = Path(file)
    with i.open('r') as old:     
        data = old.read()
    with i.open('w') as new:
        new.write("//Name: Taylor Herdman \t ID: 1539767\n" + data)
        
