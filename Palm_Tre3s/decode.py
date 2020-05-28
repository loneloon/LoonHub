
class PalmLeaves:
    def __init__(self):

        from tkinter import filedialog as fd
        import tkinter as tk

        root = tk.Tk()
        root.withdraw()

        self.text = ''

        def pathbutton():
            return fd.askopenfilename()

        m_path = pathbutton()

        message = open(m_path, 'r')
        for i in message.readlines():
            try:
                self.text += i
            except IndexError:
                pass

        #print(len(self.text))

        k_path = pathbutton()

        key = {}

        key_f = open(k_path, 'r')
        for i in key_f.readlines():
            try:
                if i[0:4] == 'mix=':
                    pass
                elif i[0:-1][-1] in key.values():
                    pass
                else:
                    key[i[0:4]] = i[0:-1][-1]
            except IndexError:
                pass

        #print(key)

        line = ''
        broken = []
        for i in self.text:
            if '\n' in line:
                line = line.strip('\n')
            if len(line) == 4:
                broken.append(line)
                line = ''
            line += i

        if '\n' in line:
            line = line.strip('\n')

        broken.append(line)
        line = ''

        print(broken)

        translate = ''

        for i in broken:
            for j, k in key.items():
                if i == j:
                    translate += k

        print(translate)


decode = PalmLeaves()
