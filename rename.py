import os
import os.path
import re
folders = [folder for folder in os.listdir() if os.path.isdir(folder)]
for folder in folders:
    if re.fullmatch(r'^Day\d$', folder):
        os.rename(folder, folder[:-1] + '0' + folder[-1:])