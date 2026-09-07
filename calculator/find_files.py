import os
for root, dirs, files in os.walk('.'):
    for f in files:
        path = os.path.join(root, f)
        if not path.startswith('./.'):  # skip hidden dirs
            print(path)
