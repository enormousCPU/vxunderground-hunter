import requests, lxml, argparse, re, os
from bs4 import BeautifulSoup

from modules.table import *

HEADERS ={
            "User-Agent" : "Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4881.87 Safari/537.36"
        }


def banner():
    import pyfiglet
    print(pyfiglet.figlet_format("INFECTED"))

def get_soup(url):
    resp = requests.get(url, headers=HEADERS).text
    soup = BeautifulSoup(resp, 'lxml')

    return soup

class crawler():
    def __init__(self, url):
        self.url = url

    def search_query(self, q):
        soup = get_soup(self.url)
        tds = soup.find_all("td", class_='link')

        results = {}
        counter = 1
        for td in tds:
            if re.search(q.lower(), td.a.get_text().lower()):
                results[counter] = td.a['href']
                counter += 1
        
        return results

class vxinf():
    def __init__(self, downlAll, malware, downloadPath="."):
        self.links = {}
        self.downlAll = downlAll
        self.malware = malware
        self.downloadPath = downloadPath
        self.base_name = self.malware.split('/')[-2]
        self.malware_directory = os.path.join(self.downloadPath, self.base_name)
        self.bianries_counter = 1

    def get_malwareLinks(self, url):

        soup = get_soup(url)
        tbody = soup.find('tbody')
        for tr in tbody.find_all('tr'):
            link = tr.find('td', class_="link").a['href']
            name = tr.find('td', class_='link').text
            size = tr.find('td', class_='size').text

            if link == "../":
                continue
            if size == "0":
                self.get_malwareLinks(link)
            elif name.split('/')[-1].split('.')[-1] == "7z":
                self.links[self.bianries_counter] = link
                self.bianries_counter += 1

    def download_malware(self, url):
        
        resp = requests.get(url)
        file_name = url.split('/')[-1]
        
        malware_directory = os.path.join(self.downloadPath, os.path.join(self.base_name, url.replace(self.malware, "").replace(file_name, "")))

        try:
            if malware_directory not in os.listdir(self.malware_directory):
                os.makedirs(malware_directory)
        except:
            pass


        path = os.path.join(malware_directory, (file_name))
        with open(path, 'wb') as w:
            w.write(resp.content)

    def main(self):

        self.get_malwareLinks(self.malware)
        
        print(f"[{self.base_name}] Found {len(self.links)} binaries for {self.base_name}\n")

        if not self.downlAll:
            to_download = table(self.links, isHash=True, malwareName=self.base_name).main()
        else:
            to_download = self.links
        
        if not to_download:
            return
            
        
        try:
            os.mkdir(self.malware_directory)
        except FileNotFoundError:
            print("[!] Directory Not Found!")
            return
        except FileExistsError:
            pass
    
        print(f"\n[{self.base_name}] Downloading {len(to_download)} total of binaries")
        for malware_index in to_download:
            try:
                self.links[malware_index]
            except:
                continue
            self.download_malware(self.links[malware_index])
        
        
if __name__ == "__main__":
    try:
        banner()
    except:
        pass

    parser = argparse.ArgumentParser()
    parser.add_argument('-m', '--malware', help="malware name/query to search for")
    parser.add_argument('-dm', '--downlAllMals', help="download all matching malwares", action="store_true")
    parser.add_argument('-dn', '--downlAllbins', help="download all binaries for a given malware", action="store_true")
    parser.add_argument('-dp', '--downloadPath', help="download path", default=".")
    args = parser.parse_args()

    if not args.malware:
        print("[!] malware name/query must be supplied!\nQUITTING!")
        exit()
    
    FAMILIES_URL = "https://samples.vx-underground.org/samples/Families/"

    res = crawler(FAMILIES_URL).search_query(args.malware)

    if not args.downlAllMals:
        to_download = table(res, isHash=False).main()
    else:
        to_download = res.keys()
    
    if not to_download:
        print("QUITTING!")
        exit()

    
    for malware_index in to_download:
        try:
            res[malware_index]
        except:
            continue

        vxinf(args.downlAllbins, res[malware_index], args.downloadPath).main()
        print()
    

    print("Donwload Malwares!")
    print("QUITTING!")