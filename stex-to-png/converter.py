"""
stex to png converter
place and run this script in folder with stex files
"""

from os import getcwd, listdir, path
import re

cwd = getcwd()

for file in listdir(cwd):
    if file.endswith(".stex"):
        in_file = path.join(cwd, file)
        out_file = f"{re.sub(r'(?<=\.).*', '', in_file)}png"
        with open(in_file, 'rb') as in_img:
            with open(out_file, 'wb') as out_img:
                in_img.seek(32)

                while True:
                    char = in_img.read(1)
                    out_img.write(char)

                    if not char:
                        break
