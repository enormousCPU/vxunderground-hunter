# vxunderground-hunter

vxunderground-hunter is a tool that enables you to search for a certian malware or a query on the vx-underground website.
it can be used to download multiple malwares with the ability to select or download all binaries for a given malware.

 

## instellation
```sh
git clone https://github.com/enormousCPU/vxunderground-hunter.git
cd vxunderground-hunter
pip install -r requirements.txt
```
and simply run `python vxug-py --help`:

      usage: vxug.py [-h] [-m MALWARE] [-dm] [-dn] [-dp DOWNLOADPATH]

      options:
        -h, --help            show this help message and exit
        -m MALWARE, --malware MALWARE
                              malware name/query to search for
        -dm, --downlAllMals   download all matching malwares
        -dn, --downlAllbins   download all binaries for a given malware
        -dp DOWNLOADPATH, --downloadPath DOWNLOADPATH
                              download path


## note: this is a Quick N' Dirty code ~~

