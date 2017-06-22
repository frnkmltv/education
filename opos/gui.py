import Tkinter as tk
import sys
import threading
import time
import tkMessageBox

import operations


class GUI():
    master = tk.Tk()
    running = True

    def on_closing(self):
        if tkMessageBox.askokcancel("Quit", "Do you want to quit?"):
            sys.exit(0)

    def stop_monitor(self):
        self.runnning = False

    def __init__(self, master=None, size='800x600'):
        self.master.protocol("WM_DELETE_WINDOW", self.on_closing)
        self.width = size.split('x')[0]
        self.height = size.split('x')[1]
        self.master.geometry(size)
        self.master.title('Process monitor')
        self.info = tk.StringVar()
        self.info.set('Check if process active...')
        self.program_name = tk.StringVar()
        self.program_name.set('Enter File Name [.exe] or Window Caption: ')
        self.ask_label = tk.Label(self.master, textvariable=self.program_name,
                                  height=int(int(self.height) / 200),
                                  font=('Times New Roman', '10'), width=int(int(self.width) / 15))

        self.ask_entry = tk.Entry(self.master, width=int(int(self.width) / 15))
        self.main = threading.Thread(target=self.master.mainloop, name='main')
        self.window_thread = threading.Thread(target=self.change_window, name='windowthread')
        self.window_thread.daemon = True
        try:
            print(self.filename, 'est')
        except:
            print('netu')
        try:
            print(self.window_thread.is_alive())
        except:
            print('netu')

        self.ask_button = tk.Button(self.master, text='Monitor',
                                    command=self.window_thread.run)
        self.main.start()
        print(threading.current_thread(), 'current')
        if self.window_thread.is_alive():
            self.window_thread.join()
        self.ask_label.grid(row=0, column=0)
        self.ask_entry.grid(row=1, column=0)
        self.ask_button.grid(row=2, column=0)

    def change_window(self):
        self.filename = self.ask_entry.get()
        print(threading.enumerate())
        print(self.filename, 'here is filename')
        if self.filename != '' and self.filename != 'None':
            self.second_thread = threading.Thread(target=self.start_monitor, name='monitorthread')
            self.second_thread.daemon = True
            self.second_thread.start()
        else:
            self.program_name.set('Enter File Name [.exe] or Window Caption: ' + '\nEmpty field. Try again')
            if self.filename == '':
                self.main.run()
                self.ask_button.configure(command=self.window_thread.run)
                self.ask_button.grid_configure(row=2, column=0)

    def start_monitor(self):
        self.program_name.set('Status of "%s" process: ' % self.filename)
        self.list_label = tk.Label(self.master, textvariable=self.info, bg='white', width=int(int(self.width) / 15),
                                   fg='black', height=int(int(self.height) / 10))
        self.list_label.grid(row=0, column=1, rowspan=4)
        # threading.Thread(target=process, args={'filename': filename}).start()
        while True:
            task = self.info.get()
            time.sleep(1)
            proc = operations.Process(filename=self.filename)
            if proc.current_state != task:
                self.info.set(task + '\n' + proc.current_state)


if __name__ == '__main__':
    a = GUI()
