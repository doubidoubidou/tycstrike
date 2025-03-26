import os

root=r'E:\cs1.6\gitroot\cstrike\maps'

files=os.listdir(root)
files=[f.split('.')[0] for f in files if f.endswith('.bsp')]

with open('E:\cs1.6\gitroot\maps.txt','w') as f:
    f.write('\n'.join(files))