import string
import datetime
import os

class KeyGen:

    def __init__(self, path):
        self.now = str(datetime.datetime.now())[0:19].replace(' ', '_').replace(':', '')
        self.path = path
        self.filename = 'processing'
        self._openpath = open(f"{self.path}/{self.filename}", "a+")

    def keygen(self, length, lib, path):
        stock = ['0' * length]
        for pos in stock:
            if len(stock) == (len(lib)) ** length:
                break
            temp = list(pos)
            temp2 = list(pos)
            for idx, symb in enumerate(temp):
                for d in lib:
                    if temp[idx] == d:
                        pass
                    else:
                        print(''.join(temp2))
                        temp2[idx] = d
                        if (''.join(temp2)) in stock:
                            pass
                        else:
                            stock.append(''.join(temp2))
                            self._openpath.write(f"{''.join(temp2)}\r\n")
                        temp2 = temp
        self._openpath.close()
        os.chdir(self.path)
        os.rename(self.filename, self.now)
        return sorted(stock)


