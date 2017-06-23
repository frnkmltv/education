import Tkinter as tk
import threading

import operations


class GUI(tk.Frame):
    master = tk.Tk()
    keys = dict.fromkeys(
        ["PID", "Mem Usage", "Status", "CPU Time",
         "Window Title"], None
    )

    def on_closing(self):
        import tkMessageBox, sys
        try:
            process_item_values = operations.Process(filename=self.filename).current_state
            if tkMessageBox.askokcancel("Quit",
                                        "Do you want to quit?\nMonitored process is %s state" % process_item_values[
                                            'Status'].split('\n')[0]):
                sys.exit(0)
        except AttributeError:
            if tkMessageBox.askokcancel("Quit",
                                        "Do you want to quit?"):
                sys.exit(0)

    def stop_monitor(self):
        self.running = False
        self.stop_button.configure(command=self.on_closing, text='Exit')
        self.stop_button.grid_configure(row=2, column=1)
        self.second_thread.join(timeout=1)

    def __init__(self, master=master, size='450x300', running=False):
        self.running = running
        tk.Frame.__init__(self, master)
        self.master.geometry(size)
        self.master.protocol("WM_DELETE_WINDOW", self.on_closing)
        self.width = self.master.winfo_width()
        self.height = self.master.winfo_height()
        self.master.title('Process monitor')
        self.program_name = tk.StringVar()
        self.program_name.set('Enter File Name [.exe] or Window Caption: ')
        self.ask_frame = tk.Frame(self.master,
                                  highlightbackground='black', relief='ridge', bd='5', bg='white', width=self.width)
        self.display_process_frame = tk.Frame(self.master,
                                              highlightbackground='black', bg='white', relief='ridge', bd='2',
                                              width=self.width)
        self.ask_label = tk.Label(self.ask_frame, textvariable=self.program_name,
                                  font=('Ubuntu', '12', 'bold'), bg='white')
        self.ask_entry = tk.Entry(self.ask_frame, width=61, font=('Ubuntu', '10', 'bold'), bd='5')
        self.main = threading.Thread(target=self.master.mainloop, name='main')
        self.ask_button = tk.Button(self.ask_frame, text='Monitor', width=10, pady=2,
                                    command=self.change_window, relief=tk.GROOVE, font=('Ubuntu', '8', 'bold'))
        self.stop_button = tk.Button(self.ask_frame, text='Stop', width=10, pady=2, relief=tk.GROOVE,
                                     font=('Ubuntu', '8', 'bold'))
        self.main.start()
        self.ask_frame.grid(row=0, column=0)
        self.ask_label.grid(row=0, column=0, columnspan=2)
        self.ask_entry.grid(row=1, column=0, columnspan=2)
        self.ask_button.grid(row=2, column=0)

    def change_window(self):
        self.running = True
        filename = self.ask_entry.get()
        if filename != '' and filename != 'None':
            self.filename = filename
            self.second_thread = threading.Thread(target=self.start_monitor, name='monitorthread')
            self.second_thread.daemon = True
            self.second_thread.start()
            self.stop_button.configure(command=self.stop_monitor, text='Stop')
            self.stop_button.grid_configure(row=2, column=1)
        else:
            self.program_name.set('Enter File Name [.exe] or Window Caption: ' + '\nEmpty field. Try again')

            self.ask_button.grid_configure(row=2, column=0)

    def start_monitor(self):
        self.display_process_frame.grid(row=1, column=0)
        self.program_name.set('Status of %s process: ' % self.filename.upper())
        co = 0
        for label in self.keys.keys():
            if not self.keys[label]:
                self.keys[label] = tk.StringVar()
                self.list_label = tk.Label(self.display_process_frame, text=label, width=len(str(label)) + 3, anchor=tk.W,
                                           fg='black',
                                           font=('Times New Roman', '10', 'bold'))
            self.values_label = tk.Message(self.display_process_frame, textvariable=self.keys[label], bg='white',
                                           fg='black',
                                           font=('Times New Roman', '10'))
            self.list_label.grid(row=0, column=co)
            self.values_label.grid(row=1, column=co)
            # threading.Thread(target=process, args={'filename': filename}).start()
            co += 1
        while self.running:
            process_item_values = operations.Process(filename=self.filename).current_state
            for key in self.keys.keys():
                self.keys[key].set(process_item_values[key])


if __name__ == '__main__':
    a = GUI()
