
class KeyGen:
    def __init__(self, path):
        self.path = str(path)


    def keygen(self, pass_len, passw, path):
        import string
        import random

        idx = []
        data = []
        for i in string.digits:
            data.append(str(i))
        for i in string.ascii_uppercase:
            data.append(str(i))
        for i in string.ascii_lowercase:
            data.append(str(i))

        counter = 0

        # counter = len(data)**len(data)

        passw_logs = open(r"path","a+")

        print('We have', len(data) ** len(passw), 'possible combinations.')
        print('Proceed with keygen?')
        if input('Y/N = ') in ['N', 'n']:
            print('Wise decision!')
            pass
        else:
            match = False
            attempt_counter = 0
            while match != True:
                while len(idx) < len(passw):
                    idx.append(str(data[random.randrange(len(data))]))
                if ''.join(idx) == passw:
                    if ''.join(idx) not in passw_logs:
                        passw_logs.write(''.join(idx) + ',')
                    else:
                        pass
                    attempt_counter += 1
                    match = True
                    print('pass_unlocked!', 'password =', ''.join(idx))
                    print(attempt_counter, 'combinations were attempted.')
                else:
                    if ''.join(idx) not in passw_logs:
                        passw_logs.write(''.join(idx) + ',')
                    else:
                        pass
                    print(''.join(idx))
                    idx = []
                    attempt_counter += 1
                    continue

        passw_logs.close()
        print('')
        print('passw_logs written successfully!')
