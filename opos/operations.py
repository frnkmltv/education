import time

import os


class Process:
    run = True
    current_state = 'kuku'

    def __init__(self, filename, ask_delay=5):
        self.ask_delay = ask_delay
        self.filename = filename
        self.current_state = 'Unknown'
        info = os.popen('tasklist /FI "IMAGENAME eq %s" /fo  csv /v /nh' % self.filename).read()
        if not info.startswith('INFO: No tasks are running which match the specified criteria.'):
            subtasks = [i for i in info.split('\n')]
            if len(subtasks) > 1:
                self.window_caption = subtasks[0].split(',')[-1]
                self.subtasks = subtasks[1:]
            self.state = info.split(',')[6]
            print(len(info.split('\n')) - 1)
            print(info)
            print(self.__dict__)
            self.current_state = info
        else:
            self.current_state = 'Not running yet.'
        time.sleep(self.ask_delay)

        # def check(self):
        #     while self.run:
        #         # info = os.popen(
        #         #     'wmic process where "name="%s"" get ExecutablePath' % self.filename).read()
        #         # print(os.popen(self.filename).read())
        #

if __name__ == '__main__':
    process = Process('chrome.exe')
# proc = Process(filename='devenv.exe')
