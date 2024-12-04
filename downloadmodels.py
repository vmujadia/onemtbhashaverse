import sys
import os
import requests

from oneconfig import URL_SPM_MODEL, URL_ONEMT_MODEL, URL_SDIC, URL_TDIC

urls = [URL_SPM_MODEL, URL_ONEMT_MODEL, URL_SDIC, URL_TDIC]
filenames = ["models/onemtv3b_spm.model","models/onemtv3b.pt","models/dict.SRC.txt","models/dict.TGT.txt"]

for url, filename in zip(urls, filenames):
    r = requests.get(url, stream=True)
    with open(filename, 'wb') as fd:
        for chunk in r.iter_content(chunk_size=256):
            fd.write(chunk)
    print(f"file {filename} downloaded succesfully")
