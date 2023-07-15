import os
import re

def dup_remover(dir):

    for root, dirs, files in os.walk(dir):

        flist = {}

        for fname in files:

            path = os.path.join(root, fname)

            matching = re.search(r'^(.*?)\((\d+)\)(\.[^.]*)?$', fname)

            if matching:

                name = matching.group(1)

                num = int(matching.group(2))

                ext = matching.group(3) or ""

                if name not in flist:

                    flist[name] = [(num, path, ext)]

                else:

                    flist[name].append((num, path, ext))

        for name in flist:

            files = flist[name]

            files.sort(key = lambda x: x[0])

            print(files)

            newest = files[-1][1]

            ext = files[-1][2]

            for num, fpath, _ in files[:-1]:

                print(f"Deleting duplicate file: {fpath}")

                os.remove(fpath)

            os.rename(newest, os.path.join(root, f"{name}{ext}"))

            print(f"Renamed {newest} to {name}{ext}")

dup_remover(os.path.expanduser("C:\Test"))
