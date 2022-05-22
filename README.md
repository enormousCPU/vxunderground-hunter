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
## example

     `python vxug.py -m rat`:

     [1] 9002Rat                [2] Android.Brata                

     [3] AsyncRAT                [4] BitRAT                

     [5] BoratRAT                [6] CrateDepression                

     [7] Cronrat                [8] CuratorRansomware                

     [9] DCRat                [10] Darktrack Rat                

     [11] DiscordRAT                [12] HavexRat                

     [13] KimjongRat                [14] Limerat                

     [15] LodaRAT                [16] Molerats                

     [17] NerbianRAT                [18] NetWireRAT                

     [19] NjRat                [20] ParallaxRat                

     [21] PickandPlaceRAT                [22] QuasarRAT                

     [23] RatDispenser                [24] RokRAT                

     [25] STRRAT                [26] ShimRAT                

     [27] Trat                [28] Trochilus Rat                

     [29] UBoatRAT                [30] UDPRat                

     [31] XPertRat                [32] XRat                

     [33] XTremeRat                

     type help for supported commands
     cmd: help

             exit - exit programe
             n1-n2 - donwload all malwares/hashes from n1 to n2
             n1,n2,...,nk download individual malwares/hashes. must be seperated by ','
             n1,n2&n3-nk download malware/hash n1 and n2 and download all malwares/hashes from n3 to nk. compined commands must be seperated by "&"
             0 - download all


     cmd: 

## note: this is a Quick N' Dirty code ~~

