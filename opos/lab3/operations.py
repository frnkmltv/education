import os
import time

class Process:
    def __init__(self, filename):
        self.filename = filename
        self.current_state = dict.fromkeys(
            ["PID", "Mem Usage", "Status", "CPU Time",
             "Window Title"], ''
        )
        if self.filename.endswith('.exe'):
            info = os.popen('tasklist /FI "IMAGENAME eq %s" /fo  csv /v  /nh' % self.filename).read()
        else:
            info = os.popen('tasklist /FI "WINDOWTITLE eq %s" /fo  csv /v  /nh' % self.filename).read()
        subtasks = [i for i in info.split('\n')]
        if not info.startswith('INFO: No tasks are running which match the specified criteria'):
            if len(subtasks) > 1:
                self.current_state["Window Title"] += subtasks[0].split(',')[-1][1:-1] + '\n'
                for i in range(len(subtasks) - 1):
                    self.current_state["CPU Time"] += subtasks[i].split(',')[-2][1:-1] + '\n'
                    self.current_state["Status"] += subtasks[i].split(',')[6][1:-1] + '\n'
                    self.current_state["Mem Usage"] += subtasks[i].split(',')[5][1:-1] + '\n'
                    self.current_state["PID"] += subtasks[i].split(',')[1][1:-1] + '\n'
            else:
                self.current_state["Window Title"] = subtasks[0].split(',')[0][1:-1]
                self.current_state["CPU Time"] = subtasks[0].split(',')[8][1:-1]
                self.current_state["Status"] = subtasks[0].split(',')[6][1:-1]
                self.current_state["Mem Usage"] = subtasks[0].split(',')[5][1:-1]
                self.current_state["PID"] = subtasks[0].split(',')[1][1:-1]
                # print(len(info.split('\n')) - 1)
                # print(info)
                # print(self.__dict__)

        else:
            self.current_state["Status"] = 'Not running'
            self.current_state["Window Title"] = '-----'
            self.current_state["PID"] = '-----'
            self.current_state["CPU Time"] = '-----'
            self.current_state["Mem Usage"] = '-----'

        time.sleep(2)
            # else:
            #     if self.current_state['PID'] == None:
            #         pass
            #     elif not self.current_state:
            #         self.current_state = 'Not running yet.'
            #     else:
            #         self.current_state = 'Task has stopped.'

            # def check(self):
            #     while self.run:
            #         # info = os.popen(
            #         #     'wmic process where "name="%s"" get ExecutablePath' % self.filename).read()
            #         # print(os.popen(self.filename).read())
            #


if __name__ == '__main__':
    process = Process('chrome.exe')
# proc = Process(filename='devenv.exe')
