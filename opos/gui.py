import Tkinter as tk
import sys
import threading
import time
import tkMessageBox

from operations import Process


class GUI(tk.Frame):
    master = tk.Tk()
    process_name = None

    def on_closing(self):
        if tkMessageBox.askokcancel("Quit", "Do you want to quit?"):
            sys.exit(0)

    def __init__(self, master=None, size='800x600'):
        self.master.protocol("WM_DELETE_WINDOW", self.on_closing)
        tk.Frame.__init__(self, master)
        width = size.split('x')[0]
        height = size.split('x')[1]
        self.master.geometry(size)
        self.master.title('Process monitor')
        self.info = tk.StringVar()
        self.info.set('Hello')
        self.program_name = tk.StringVar()
        self.program_name.set('Enter File Name [.exe] or Window Caption: ')
        self.ask_label = tk.Label(self.master, textvariable=self.program_name,
                                  height=int(height) * 2 / 700,
                                  font=('Times New Roman', '10'))

        self.ask_entry = tk.Entry(self.master, width=50)
        self.main_thread = threading.Thread(target=self.master.mainloop)
        self.second_thread = threading.Thread(target=self.start_monitor)
        self.second_thread.daemon = True
        self.ask_button = tk.Button(self.master, text='Monitor',
                                    command=self.second_thread.start)
        self.ask_label.grid(row=0, column=0)
        self.ask_entry.grid(row=1, column=0)
        self.ask_button.grid(row=2, column=0)

        self.main_thread.start()

    def start_monitor(self):
        filename = self.ask_entry.get()
        print('yoeryer')
        if filename != '':
            self.program_name.set('Status of "%s" process: ' % filename)
            self.ask_entry.grid_remove()
            self.ask_button.grid_remove()
            self.list_label = tk.Label(self.master, textvariable=self.info, width=100, height=50)
            self.list_label.grid(row=0, column=0)
            # threading.Thread(target=process, args={'filename': filename}).start()
            while True:
                proc = Process(filename=filename)
                time.sleep(2)
                if proc.current_state != self.info.get():
                    self.info.set(self.info.get() + '\n' + proc.current_state)
                print(proc.current_state)

if __name__ == '__main__':
    GUI()
