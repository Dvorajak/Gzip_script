import gzip
import shutil
import os

cesta = "/var/log/"
soubory = os.listdir(cesta)



for i in soubory:
    if i.endswith(".log"):
        with open('/var/log/'+ i,"rt") as f_in:
            with gzip.open(cesta + i + '.gz','wt') as f_out:
                shutil.copyfileobj(f_in,f_out)
        os.remove(cesta + i)

