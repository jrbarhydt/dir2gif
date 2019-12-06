import imageio
from os import listdir, rename
from os.path import isfile, join
mypath = os.getcwd()
myfiles = [mypath + f for f in listdir(mypath) if isfile(join(mypath, f))]
images=[]

for file in myfiles:
    images.append(imageio.imread(file))
imageio.mimsave(mypath + '\\movie.gif', images)

# TODO: add args to parse, input loc and output loc, maybe compression