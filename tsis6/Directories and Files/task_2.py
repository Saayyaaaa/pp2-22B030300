import os
print('Exist:', os.access('../Directories and Files', os.F_OK))
print('Readable:', os.access('../Directories and Files', os.R_OK))
print('Writable:', os.access('../Directories and Files', os.W_OK))
print('Executable:', os.access('../Directories and Files', os.X_OK))