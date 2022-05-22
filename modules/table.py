
class table():
    def __init__(self, list_, isHash, malwareName=None):
        self.list_ = list_
        self.isHash = isHash
        self.malwareName = malwareName
    
    def malHash(self, c):
        return self.list_[c].split('/')[-1]
    
    def malName(self, c):
        return self.list_[c].split('/')[-2]

    def rangeCmdHandler(self, cmd):
        range_ = cmd.split('-')
        return [i for i in range(int(range_[0]), int(range_[1])+1)]
    
    def indCmdHandler(self, cmd):
        return [int(i) for i in cmd.split(',')]
    
    def multipleCmdHandler(self, cmd):
        results = []
        for command in cmd:
            if "-" in command:
                results += self.rangeCmdHandler(command)
            elif "," in command:
                results += self.indCmdHandler(command)
            else:
                results += [int(command)] if int(command) <= len(self.list_) else []
        
        return results
    
    def pTable(self):
        c = 1
        while c <= len(self.list_):
            for i in range(2):
                if c > len(self.list_):
                    break
                if self.isHash:
                    to_print = f"[{self.malwareName}][{c}] {self.malHash(c)}"
                else:
                    to_print = f"[{c}] {self.malName(c)}"
                
                print(f"{to_print}", end=" " * 16)
                c+= 1
            print("\n")
    
    def main(self):
        self.pTable()
        cmd = ""
        help = """
        exit - exit program
        n1-n2 - donwload all malwares/hashes from n1 to n2
        n1,n2,...,nk download individual malwares/hashes. must be seperated by ','
        n1,n2&n3-nk download malware/hash n1 and n2 and download all malwares/hashes from n3 to nk. compined commands must be seperated by "&"
        0 - download all
        
        """
        print("type help for supported commands")
        while cmd != "exit":
            cmd = input(f"cmd: ")    
            if cmd == "help":
                print(help)
            elif cmd == "0":
                return self.list_
            elif "&" in cmd:
                return self.multipleCmdHandler(cmd.split('&'))
            elif "-" in cmd:
                return self.rangeCmdHandler(cmd)
            elif "," in cmd:
                return self.indCmdHandler(cmd)
            elif cmd:
                try:
                    if int(cmd) <= len(self.list_):
                        return [int(cmd)]
                    else:
                        return []
                except:
                    pass
        return []

if __name__ == "__main__":
    exit()
