import yaml
from yaml.loader import SafeLoader
import subprocess

# Open the file and load the file
with open('fstab.yaml') as f:
    data = yaml.load(f, Loader=SafeLoader)
for i in data['fstab']:
    disk=i
    c=""
    for j in data['fstab'][i]:
        if (type(data['fstab'][i][j]) != str):
            for i in data['fstab'][i][j]:
                c=c+" "+i
        else:
            c=c+" "+(data['fstab'][i][j])
    out=disk+" "+c
cmd="out > /etc/fstab"
process = subprocess.Popen(cmd,stdout=subprocess.PIPE, shell=True)
run = process.communicate()[0].strip().decode('ASCII')
print(run)
