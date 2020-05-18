import string
import random
import datetime

class PalmTrees:
    def __init__(self, leftb, rightb, palmtree):

        # The following is an uneducated attempt of a slow multilevel encoding
        # The following encoding is layered.
        # 'maps' stand for code-symbol reference dictionaries at each level
        # Levels are numbered in ascending order starting with the 1st primary level.

        self.leftb = leftb
        self.rightb = rightb
        self.palmtree = palmtree

        self.symbols = string.printable

        self.primary_codes = self.spawn_codes(self.symbols)
        print(self.primary_codes)

        self.map_lvl1 = self.encodelvl1(self.primary_codes, self.symbols)
        print(self.map_lvl1)


        self.map_lvl2 = self.encodelvl2(self.map_lvl1, self.palmtree)
        print(self.map_lvl2)

        self.timecode = str(datetime.datetime.now()).strip(' ').replace(':', '_')

        key = open('out/key_%s' % self.timecode, 'a+')

        for i, j in self.map_lvl2.items():
            key.write(f'{i}:{j}\n')

        key.close()

    def spawn_codes(self, lib: str):
        codes = []
        while len(codes) < len(self.symbols):
            code = str(random.randint(self.leftb, self.rightb))
            if code not in codes:
                codes.append(code)

        check = True
        for i in codes:
            if codes.count(i) > 1:
                check = False
                print(i)

        if check:
            print("Codes generated. No copies!")
        else:
            print("Bad result. There are copies!")

        return codes

    def encodelvl1(self, code_map: list, lib: str):
        map = {i: j for i, j in zip(code_map, self.symbols)}
        print("First lvl of encoding complete. Code map generated!")
        return map

    def encodelvl2(self, map_lvl1, palmtree):
        dc_string = palmtree
        transfer_map = {str(idx): lttr for idx, lttr in enumerate(dc_string)}
        print(transfer_map)
        main_map = {}
        for code, symb in map_lvl1.items():
            temp = []
            for i in code:
                for num, let in transfer_map.items():
                    if i == num:
                        temp.append(let)
            main_map[''.join(temp)] = symb

        if main_map != {}:
            print("Success! Second level generated.")
        else:
            print("Operation failed. Dictionary is empty.")

        return main_map

    def translate(self, text_input):

        message = open('out/message_%s' % self.timecode, 'a+')

        line = ''

        for i in text_input:
            for code, symb in self.map_lvl2.items():
                if len(line) > 40:
                    message.write(f'\r{line}')
                    line = ''
                if i == symb:
                    line += code

        message.write(f'{line}')
        message.close()

        print('Message encoded!')

