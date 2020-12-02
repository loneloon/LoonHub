import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import datetime, time, json
import os


class Sol():

    def __init__(self):

        self.activities = {0: 'Sleep', 1:'Meals', 2:'Hygiene', 3:'Exercise', 4:'Work', 5:'Study', 6:'Creative',
                           7:'Shopping',
                           8:'Leisure', 9:'Cleaning'}

        self.colors = {'Sleep': 'gray', 'Meals': 'mediumseagreen', 'Hygiene':'turquoise', 'Exercise':'orange',
                       'Work':'indianred', 'Study':'cornflowerblue', 'Creative':'pink',
                           'Shopping':'rosybrown',
                           'Leisure':'lightgrey', 'Cleaning':'cyan'}

        self.current_task = 0

        self.current_record = []

        print('Welcome to Sol-protocol!\n')



    def cur_time(self):
        return datetime.datetime.now().strftime('%H:%M:%S')


    def punch_in(self, act_code, login):

        act_code = int(act_code)

        self.sync(login)

        if not self.current_record:
            self.current_record.append([self.cur_time(), self.activities[self.current_task]])
            self.current_task = act_code
            self.save(login)
            return f"Good morning!\nHave a nice day!\nYou started {self.activities[act_code]}"
        else:

            comp_str = ''

            self.current_record.append([self.cur_time(), self.activities[self.current_task]])
            comp_str += f"You finished {self.activities[self.current_task]}\n"
            self.current_task = act_code
            comp_str += f"You started {self.activities[act_code]}"
            self.save(login)
            return comp_str




    def stop(self):
        self.current_record.append([self.cur_time(), self.current_task])
        return f"You finished {self.activities[self.current_task]}\n\nRecording ended!"


    def sync(self, login):
        if not os.path.exists(r"cache"):
            os.mkdir("cache")

        if not os.path.exists(f"cache/{login}"):
            with open(f"cache/{login}", "w+") as cw:
                dummy_dict = {}
                dummy_dict["autosave"] = self.current_task
                json.dump(dummy_dict,cw, indent=2, ensure_ascii=True)

        try:
            if "autosave" in json.load(open(f"cache/{login}", 'r', encoding="utf-8")).keys():
                self.current_task = json.load(open(f"cache/{login}", 'r', encoding="utf-8"))["autosave"]

            if str(datetime.datetime.now())[0:10] in json.load(open(f"cache/{login}", 'r', encoding="utf-8")).keys():
                self.current_record = json.load(open(f"cache/{login}", 'r', encoding="utf-8"))
                self.current_record = self.current_record[str(datetime.datetime.now())[0:10]]
            else:
                temp = json.load(open(f"cache/{login}", 'r', encoding="utf-8"))
                with open(f"cache/{login}", 'w+', encoding="utf-8") as jf:
                    self.current_task = 0
                    temp[str(datetime.datetime.now())[0:10]] = []
                    temp["autosave"] = self.current_task
                    json.dump(temp, jf, indent=2, ensure_ascii=True)
                    jf.close()

        except Exception as e:
            print(e, 'sync problem')


    def save(self, login):

        temp = json.load(open(f"cache/{login}", 'r', encoding="utf-8"))

        with open(f"cache/{login}", 'w+', encoding="utf-8") as jf:
            temp[str(datetime.datetime.now())[0:10]] = self.current_record
            temp["autosave"] = self.current_task
            json.dump(temp, jf, indent=2, ensure_ascii=True)
            jf.close()

    def generate_graph(self, login):

        random_data = []

        ranged_data = []

        color_list = []

        with open(f"cache/{login}", 'r', encoding="utf-8") as jf:
            act_input = json.load(jf)
            jf.close()

        for i in act_input[str(datetime.datetime.now())[0:10]]:
            time_d = i[0].split(':')
            color_list.append(self.colors[i[1]])

            seconds = int(time_d[2]) + int(time_d[1]) * 60 + int(time_d[0]) * 3600

            if not random_data:
                random_data.append(seconds)
            else:
                random_data.append(seconds - sum(random_data))

        color_list = tuple(i for i in color_list)

        for idx, i in enumerate(random_data):
            if idx == 0:
                ranged_data.append((idx, i))
            else:
                ranged_data.append((sum(random_data[0: idx]), i))

        fig, ax = plt.subplots()
        ax.broken_barh(ranged_data, (0, 4),
                       facecolors=color_list)
        ax.set_xlim(0, sum(random_data))
        ax.set_xlabel('seconds since start')
        ax.grid(False)
        plt.axis('off')

        handls = []

        for act, col in self.colors.items():
            handls.append(mpatches.Patch(color=col, label=act))

        plt.legend(handles=handls)

        plt.savefig(f"{login}_report.png")

    def count_stats(self, login):

        time_list = []

        with open(f"cache/{login}", 'r', encoding="utf-8") as jf:
            act_input = json.load(jf)
            jf.close()

        prev_frame = 0

        for i in act_input[str(datetime.datetime.now())[0:10]]:
            time_d = i[0].split(':')

            seconds = int(time_d[2]) + int(time_d[1]) * 60 + int(time_d[0]) * 3600
            t_delta = seconds - prev_frame

            prev_frame = seconds

            time_list.append([t_delta, i[1]])


        summary = {}

        total_all = 0


        for activity in self.colors.keys():

            total_one = 0
            for entry in time_list:
                if entry[1] == activity:
                    total_one += int(entry[0])

            total_all += total_one
            summary[activity] = total_one

        for key, val in summary.items():
            summary[key] = val/total_all*100

        return summary

    def view_task(self, login):

        self.sync(login)

        return self.activities[self.current_task]


