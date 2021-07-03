import os
import shutil

path = input('Please input the directory that you would like to organize: ')

files = os.listdir(path)

for i in files:
    name = os.path.splitext(i)

    title = name[0]
    extension = name[1]

    if os.path.exists(path+'/'+extension):
        shutil.move(path+i, path+'/'+extension)
    else:
        os.path.makedirs(path+'/'+extension)
        shutil.move(path+i, path+'/'+extension)

print('Your files have been succesfully organized.')