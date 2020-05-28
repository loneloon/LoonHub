

class PalmTrees:
    def __init__(self, text_input):
        import string
        import random
        import datetime
        # The following is an uneducated attempt of a slow multilevel encoding
        # The following encoding is layered.
        # 'maps' stand for code-symbol reference dictionaries at each level
        # Levels are numbered in ascending order starting with the 1st primary level.

        symbols = string.printable

        self.text_input = text_input

        def spawn_codes(lib: string):
            codes = []
            while len(codes) < len(symbols):
                code = str(random.randint(3789, 7891))
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

        primary_codes = spawn_codes(symbols)
        print(primary_codes)

        def encodelvl1(code_map: list, lib: string):
            map = {i: j for i, j in zip(code_map, symbols)}
            print("First lvl of encoding complete. Code map generated!")
            return map

        map_lvl1 = encodelvl1(primary_codes, symbols)
        print(map_lvl1)

        def encodelvl2(map_lvl1):
            dc_string = 'palm_tre3s'
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

        map_lvl2 = encodelvl2(map_lvl1)
        print(map_lvl2)

        timecode = str(datetime.datetime.now()).strip(' ').replace(':', '_')

        key = open('out/key_%s' % timecode, 'a+')

        for i, j in map_lvl2.items():
            key.write(f'{i}:{j}\n')

        key.close()

        message = open('out/message_%s' % timecode, 'a+')

        line = ''

        for i in text_input:
            for code, symb in map_lvl2.items():
                if len(line) > 40:
                    message.write(f'\r{line}')
                    line = ''
                if i == symb:
                    line += code

        message.write(f'{line}')
        message.close()


message = input("Enter the message for encryption: ")

encode = PalmTrees(message)