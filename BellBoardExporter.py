import tkinter as tk
from tkinter import ttk


class Text():
    """
    The Text class, a custom class that wraps around a new instance of a tkinter Entrtexty widget.
    """
    def __init__(self, frame, startingText=None, width=None, height=None,
                 background="grey",
                 padx=0, pady=0,
                 column=None, row=None, columnspan=1, rowspan=1, sticky="W"):
        from tkinter import ttk, DISABLED, NORMAL, END
        self.startingText = startingText
        self.width=width
        self.height=height
        self.background = background
        self.padx = padx
        self.pady = pady
        self.column = column
        self.row = row
        self.columnspan=columnspan
        self.rowspan=rowspan

        self.info_text = tk.Text(frame, bg=self.background, width=self.width, height=self.height)
        self.info_text.insert(END, self.startingText+"\n")
        self.info_text.config(state=DISABLED)
        self.info_text.grid(column=self.column, row=self.row, columnspan=self.columnspan, rowspan=self.rowspan, padx=self.padx, pady=self.pady)


class Label():
    """
    The Label class, a custom class that wraps around a new instance of a tkinter Label widget.
    """
    def __init__(self, frame, text=None, font=("Arial Bold", 14),
                 foreground="black", background="white",
                 width=None, height=None,
                 padx=0, pady=0,
                 column=None, row=None, columnspan=1, rowspan=1, sticky="W"):

        self.text = text
        self.font = font
        self.foreground = foreground
        self.background = background
        self.width = width
        self.height = height
        self.padx = padx
        self.pady = pady
        self.column = column
        self.row = row
        self.columnspan = columnspan
        self.rowspan = rowspan
        self.sticky = sticky

        self.label = tk.Label(frame, text=self.text, font=self.font, fg=self.foreground, bg=self.background, width=self.width, height=self.height)
        self.label.grid(padx=self.padx, pady=self.pady,
                        column=self.column, row=self.row, columnspan=self.columnspan, rowspan=self.rowspan,
                        sticky=self.sticky)

    def update(self, text):
        """
        Update the value of the Label to the specified value, text.
        """
        self.label.configure(text=text)

class LabelFrame():
    """
    The LabelFrame class, a custom class that wraps around a new instance of a tkinter LabelFrame widget.
    """
    def __init__(self, frame, text=None, font=("Arial Bold", 14),
                 foreground="black", background="white",
                 width=None, height=None,
                 padx=0, pady=0,
                 column=None, row=None, columnspan=1, rowspan=1, sticky="W"):

        self.text = text
        self.font = font
        self.foreground = foreground
        self.background = background
        self.width = width
        self.height = height
        self.padx = padx
        self.pady = pady
        self.column = column
        self.row = row
        self.columnspan = columnspan
        self.rowspan = rowspan
        self.sticky = sticky

        self.label = tk.LabelFrame(frame, text=self.text, font=self.font, fg=self.foreground, bg=self.background, width=self.width, height=self.height)
        self.label.grid(padx=self.padx, pady=self.pady,
                        column=self.column, row=self.row, columnspan=self.columnspan, rowspan=self.rowspan,
                        sticky=self.sticky)

    def update(self, text):
        """
        Update the value of the LabelFrame to the specified value, text.
        """
        self.label.configure(text=text)


class Entry():
    """
    The Entry class, a custom class that wraps around a new instance of a tkinter Entry widget.
    """
    def __init__(self, frame, textVariable="", sanatiseEntry=True, width=None, state="normal", foreground="black", background="white",##3E4149",
                 padx=0, pady=0,
                 column=None, row=None, columnspan=1, rowspan=1, sticky="W"):

        self.sanatiseEntry = sanatiseEntry
        self.width=width
        self.state=state,
        self.foreground=foreground,
        self.background=background,
        self.padx=padx,
        self.pady=pady
        self.column=column
        self.row=row
        self.columnspan=columnspan
        self.rowspan=rowspan
        self.sticky=sticky

        self.entryValue = textVariable
        self.unsanatisedEntryValue = textVariable

        self.entry = tk.Entry(frame, textvariable=self.entryValue, width=self.width, state=self.state, foreground=self.foreground, background=self.background,)
        self.entry.grid(padx=self.padx, pady=self.pady,
                        column=self.column, row=self.row, columnspan=self.columnspan, rowspan=self.rowspan,
                        sticky=self.sticky)

    def sanatise(self):
        """
        Sanatise the current Entry value to match what's used on BellBoard.
        """
        if self.sanatiseEntry == True:
            self.entryValue = self.entryValue.replace(" ", "+")
            self.entryValue = self.entryValue.replace("*", "%2A")
            self.entryValue = self.entryValue.replace("/", "%2F")

    def update(self):
        """
        Update the variable that holds the Entry value to the currently given value within the Entry
        and create both sanatised and unsanatised versions of it.
        """
        self.entryValue = self.entry.get()
        self.unsanatisedEntryValue = self.entryValue
        self.sanatise()

    def get(self, sanatise=True):
        """
        Update the variable that holds the Entry value to the currently given value within the Entry,
        sanatise it if specified to, and return the value.
        """
        self.update()
        if sanatise == True:
            return self.entryValue
        elif sanatise == False:
            return self.unsanatisedEntryValue
        else:
            print('Error: Entry.get() option "sanatise" needs to be either a bool value or type None')

    def set(self, textVariable):
        """
        Set the value of the Entry to the given value, textVariable.
        """
        self.entryValue = textVariable
        self.unsanatisedEntryValue = self.entryValue
        self.entry.insert(0, textVariable)
        #self.update()

    def print(self):
        """
        Print the current value of the Entry.
        """
        #self.update()
        print(self.entryValue)

class Checkbutton():
    """
    The Checkbutton class, a custom class that wraps around a new instance of a tkinter Checkbutton widget.
    """
    def __init__(self, frame, tag=None, text=None, checkState=False, foreground="black", background="white",
                 padx=10, pady=0,
                 column=None, row=None, columnspan=1, rowspan=1, sticky="W"):

        self.tag = tag
        self.text=text
        self.foreground=foreground
        self.background=background
        self.padx=padx
        self.pady=pady,
        self.column=column
        self.row=row
        self.columnspan=columnspan
        self.rowspan=rowspan
        self.sticky=sticky

        self.chk_state_var = tk.BooleanVar(value=checkState)
        self.checkbox = tk.Checkbutton(frame, text=self.text, variable=self.chk_state_var,
                                       onvalue=True, offvalue=False,
                                       foreground=self.foreground, background=self.background,
                                       command=self.cb)
        self.checkbox.grid(padx=self.padx, pady=self.pady,
                           column=self.column, row=self.row, columnspan=self.columnspan, rowspan=self.rowspan,
                           sticky=self.sticky)

    def cb(self):
        """
        Runs given function when the value of the Checkbutton is changed.
        """
        if self.tag is None:
            print("Check state variable is", self.chk_state_var.get())
        else:
            print("{} is {}".format(self.tag, self.chk_state_var.get()))

    def get(self):
        """
        Get the value of the Checkbutton.
        """
        return self.chk_state_var.get()

    def set(self, value):
        """
        Set the value of the Checkbutton.
        """
        self.chk_state_var.set(value)

class Button():
    """
    The Button class, a custom class that wraps around a new instance of a tkinter Button widget.
    """
    def __init__(self, frame, options, tag=None, text=None, foreground="black", background="white", command=None,
                 padx=10, pady=0,
                 column=None, row=None, columnspan=1, rowspan=1, sticky="W"):

        self.tag = tag
        self.options=options
        self.text=text
        self.command = command
        self.foreground=foreground
        self.background=background
        self.padx=padx
        self.pady=pady,
        self.column=column
        self.row=row
        self.columnspan=columnspan
        self.rowspan=rowspan
        self.sticky=sticky

        self.button = tk.Button(frame, text=self.text, highlightbackground=self.background, background=self.background, foreground=self.foreground,
                                command=self.clicked)
        self.button.grid(padx=self.padx, pady=self.pady,
                         column=self.column, row=self.row, columnspan=self.columnspan, rowspan=self.rowspan,
                         sticky=self.sticky)


    def clicked(self):
        """
        Run given function when Button is clicked.
        """
        if self.command is not None:
            self.command()


class Combobox():
    """
    The Combobox class, a custom class that wraps around a new instance of a tkinter Combobox widget.
    """
    def __init__(self, frame, tag=None, menuOptions=None, width=None, foreground="black", background="white",
                 padx=10, pady=0,
                 column=None, row=None, columnspan=1, rowspan=1, sticky="W"):

        self.tag=tag,
        self.menuOptions = menuOptions
        self.width = width
        self.foreground=foreground
        self.background=background
        self.padx=padx
        self.pady=pady
        self.column=column
        self.row=row
        self.columnspan=columnspan
        self.rowspan=rowspan
        self.sticky=sticky

        self.menuValue = tk.StringVar()
        self.menuValue.set(self.menuOptions[0]) # default value

        self.combobox = ttk.Combobox(frame, textvariable=self.menuValue, values=self.menuOptions, width=width, state='readonly')
        self.combobox.configure(background=self.background, foreground=self.foreground)

        self.combobox.bind("<<ComboboxSelected>>", self.dropdown_callback)

        self.combobox.grid(padx=self.padx, pady=self.pady,
                             column=self.column, row=self.row, columnspan=self.columnspan, rowspan=self.rowspan,
                             sticky=self.sticky)

    def get(self):
        """
        Returns the currently selected Combobox value.
        """
        return self.menuValue.get()

    def dropdown_callback(self, selected=None):
        """
        Print Combobox value when it is changed to a new value.
        """
        print("{} set to {}".format(self.tag[0], self.menuValue.get()))
        if len(self.tag) > 1:
            print("Warning: tag with unexpected length: {}".format(self.tag))


class BBOption():
    """
    The BBOption class (BellBoardOption). A class the holds all the tkinter widgets used within the given frame,
    for easy access to each one, and their values etc.
    """
    def __init__(self, frame, background):
        self.frame = frame
        self.backgroundColour = background
        del background
        self.label = {}
        self.entry = {}
        self.checkbox = {}
        self.button = {}
        self.combobox = {}

    def add_label(self, tag, text=None, font=("Arial Bold", 14),
                  width=None, height=None,
                  foreground="black", background=None, padx=0, pady=0,
                  column=None, row=None, columnspan=1, rowspan=1, sticky="W"):
        """
        Function to add a tkinter Label to the frame. Does this by creating an instance of the custom Label
        wrapper class.
        """
        if background is None:
            background = self.backgroundColour

        self.label[tag] = Label(self.frame, text=text, font=font,
                                width=width, height=height,
                                foreground=foreground, background=background,
                                padx=padx, pady=pady,
                                column=column, row=row, columnspan=columnspan, rowspan=rowspan, sticky=sticky)

    def add_labelFrame(self, tag, text=None, font=("Arial Bold", 14),
                  width=None, height=None,
                  foreground="black", background=None, padx=0, pady=0,
                  column=None, row=None, columnspan=1, rowspan=1, sticky="W"):
        """
        Function to add a tkinter LabelFrame to the frame. Does this by creating an instance of the custom LabelFrame
        wrapper class.
        """
        if background is None:
            background = self.backgroundColour

        self.label[tag] = LabelFrame(self.frame, text=text, font=font,
                                     width=width, height=height,
                                     foreground=foreground, background=background,
                                    padx=padx, pady=pady,
                                    column=column, row=row, columnspan=columnspan, rowspan=rowspan, sticky=sticky)

    def add_entry(self, tag, sanatiseEntry=True, width=None, state="normal",
                  foreground="black", background="white", padx=0, pady=0,
                  column=None, row=None, columnspan=1, rowspan=1, sticky="W"):
        """
        Function to add a tkinter Entry to the frame. Does this by creating an instance of the custom Entry
        wrapper class.
        """
        self.entry[tag] = Entry(self.frame, sanatiseEntry=sanatiseEntry, width=width, state=state, foreground=foreground, background=background,
                                padx=padx, pady=pady,
                                column=column, row=row, columnspan=columnspan, rowspan=rowspan, sticky=sticky)

    def add_checkbox(self, tag, text=None, checkState=False,
                     foreground="black", background=None, padx=10, pady=0,
                     column=None, row=None, columnspan=1, rowspan=1, sticky="W"):
        """
        Function to add a tkinter Checkbutton to the frame. Does this by creating an instance of the custom Checkbutton
        wrapper class.
        """
        if background is None:
            background = self.backgroundColour

        self.checkbox[tag] = Checkbutton(self.frame, tag=tag, text=text, checkState=checkState,
                                         foreground=foreground, background=background,
                                         padx=padx, pady=pady,
                                         column=column, row=row, columnspan=columnspan, rowspan=rowspan, sticky=sticky)

    def add_button(self, tag, options, text=None, command=None,
                   foreground="black", background=None, padx=10, pady=0,
                   column=None, row=None, columnspan=1, rowspan=1, sticky="W"):
        """
        Function to add a tkinter Button to the frame. Does this by creating an instance of the custom Button
        wrapper class.
        """
        if background is None:
            background = self.backgroundColour

        self.button[tag] = Button(self.frame, tag=tag, options=options, text=text, command=command,
                                  foreground=foreground, background=background, padx=padx, pady=pady,
                                  column=column, row=row, columnspan=columnspan, rowspan=rowspan, sticky=sticky)

    def add_combobox(self, tag, menuOptions=None, width=None,
                     foreground="black", background=None, padx=10, pady=0,
                     column=None, row=None, columnspan=1, rowspan=1, sticky="W"):
        """
        Function to add a tkinter Combobox to the frame. Does this by creating an instance of the custom Combobox
        wrapper class.
        """
        if background is None:
            background = self.backgroundColour

        self.combobox[tag] = Combobox(self.frame, tag=tag, menuOptions=menuOptions, width=width,
                                      foreground=foreground, background=background, padx=padx, pady=pady,
                                      column=column, row=row, columnspan=columnspan, rowspan=rowspan,
                                      sticky=sticky)


class Menu():
    """
    The Menu class.
    """
    def __init__(self, root):
        self.menu = tk.Menu(root)
        self.newMenuItem = tk.Menu(self.menu)
        self.newMenuItem.add_command(label="Exit", command=root.destroy)
        self.menu.add_cascade(label="File", menu=self.newMenuItem)
        root.configure(menu=self.menu)


class Buffer():
    """
    The Buffer class.
    """
    def __init__(self):
        self.buf = ""
    def read(self):
        """
        Read the buffer.
        """
        return self.buf

    def flush(self):
        """
        Flush the buffer.
        """
        pass#self.buf = ""

    def clear (self):
        """
        Clear the buffer.
        """
        self.buf = ""

    def write(self, value):
        """
        Write to the buffer.
        """
        if value != "\n":
            self.buf += "> " + value + "\n"


class BB(tk.Frame):
    """
    The BB (BellBoard) class.
    """
    def __init__(self, root):

        from platform import system
        import sys
        from threading import Thread

        self.programTitle = "Bell Board Exporter - v1.0.0"
        self.backgroundColour = "#474641"

        tk.Frame.__init__(self, root)
        root.configure(background=self.backgroundColour)
        root.geometry("")
        root.title(self.programTitle)

        root.columnconfigure(0, weight=1)
        root.rowconfigure(0, weight=1)

        menu = Menu(root)

        self.canvas = tk.Canvas(root, borderwidth=0, highlightthickness=0, background=self.backgroundColour)
        self.frame = tk.Frame(self.canvas, background=self.backgroundColour)

        #self.vsb = tk.Scrollbar(root, orient="vertical", command=self.canvas.yview)
        #self.canvas.configure(yscrollcommand=self.vsb.set)
        #self.hsb = tk.Scrollbar(root, orient="horizontal", command=self.canvas.xview)
        #self.canvas.configure(xscrollcommand=self.hsb.set)

        if system() == "Windows":
            self.canvas.bind_all("<MouseWheel>", self._onMousewheel_windows)

        elif system() == "Linux":
            self.canvas.bind_all("<MouseWheel>", self._onMousewheel_linux)

        elif system() == "Darwin":
            self.canvas.bind_all("<MouseWheel>", self._onMousewheel_mac)

        else:
            print("Warning: Could not determine OS platform, assuming Windows")
            self.canvas.bind_all("<MouseWheel>", self._on_mousewheel_windows)

        #self.vsb.pack(side="right", fill="y")
        #self.hsb.pack(side="bottom", fill="x")
        self.canvas.pack(side="left", fill="both", expand=True)
        self.canvas.create_window((0, 0), window=self.frame, anchor="nw", 
                                  tags="self.frame")

        self.canvas.bind("<Configure>", self._onResize)
        self.frame.bind("<Configure>", self._onResize)

        self.frame.bind("<Configure>", self._onFrameConfigure)
        self.frame.grid_propagate=1
        for i in range(5):
            self.frame.columnconfigure(i, weight=1)
        for i in range(27):
            self.frame.rowconfigure(i, weight=1)
        self.frame.pack(fill="both", expand=True)
        #self.frame.grid(row=0, column=0, sticky="EW")
        #self.frame.pack()

        self.populate()
        self.downloader = Downloader(self.frame, self.options, self.advancedOptions)#, self.download)
        self.populate_downloadOptions()
        self.downloader.update_Download(self.downloadOptions)

        def printing_thread(self, info_text):
            """
            Function to put the printing of information, errors, etc, onto a seperate thread to the main thread.
            """
            self.info_text = info_text
            # Create Buffer class object
            self.buf = Buffer()
            # Set stdout to output to buf
            # This allows us to display a virtual terminal
            # that intercepts print(info) statements from imported classes
            sys.stdout = self.buf
            # Check and refresh buf -- see function for details
            # Could add extra bit in buf class that on write also writes to a log file
            self.print_rate = 150
            self.print_rate_original = self.print_rate
            self.read_std_out()
        self.printing_thread = Thread(target=printing_thread, args=(self, self.info_text))
        self.printing_thread.start()

    def _onResize(self, event):
        """
        Resize the tkinter canvas and frame on the user changing the size of the window.
        """
        self.width = event.width
        self.height = event.height
        self.canvas.configure(width=self.width, height=self.height)
        self.frame.configure(width=self.width, height=self.height)

    def _onFrameConfigure(self, event):
        '''Reset the scroll region to encompass the inner frame'''
        self.canvas.configure(scrollregion=self.canvas.bbox("all"))

    def _onMousewheel_windows(self, event):
        '''Enable frame scrolling for Windows'''
        #self.canvas.xview_scroll(int(-1*(event.delta/120)), "units")
        self.canvas.yview_scroll(int(-1*(event.delta/120)), "units")
        
    def _onMousewheel_linux(self, event):
        '''Enable frame scrolling for Linux'''
        #self.canvas.xview_scroll(int(-1*(event.delta/120)), "units")
        self.canvas.yview_scroll(int(-1*(event.delta/120)), "units")

    def _onMousewheel_mac(self, event):
        '''Enable frame scrolling for Mac'''
        #self.canvas.xview_scroll(int(-1*(event.delta)), "units")
        self.canvas.yview_scroll(int(-1*(event.delta)), "units")

    def populate(self):
        """
        Populate the tkinter frame with the bellboard search options and advanced search options.
        """
        row_i = 0
        col_i = 0
        lbl_title = Label(self.frame, text=self.programTitle, font=("Arial Bold", 24), background=self.backgroundColour,
                          padx=5, column=col_i, row=row_i, columnspan=2)
        row_i += 1
        col_i = 0
        self.options = BBOption(self.frame, self.backgroundColour)
        self.options.add_label(tag="association", text="Association:", padx=5, column=col_i, row=row_i, columnspan=2)
        self.options.add_entry(tag="association", width=32, padx=10, column=col_i, row=row_i+1, columnspan=2)
        row_i += 1

        row_i += 1
        col_i = 0
        self.options.add_label(tag="dateRungFrom", text="From (dd/mm/yyyy):", padx=5, column=col_i, row=row_i)
        self.options.add_entry(tag="dateRungFrom", width=10, padx=10, column=col_i, row=row_i+1)
        self.options.add_label(tag="dateRungTo", text="To (dd/mm/yyyy):", padx=5, column=col_i+1, row=row_i)
        self.options.add_entry(tag="dateRungTo", width=10, padx=10, column=col_i+1, row=row_i+1)
        row_i += 1

        row_i += 1
        col_i = 0
        self.options.add_label(tag="place", text="Place:", padx=5, column=col_i, row=row_i)
        self.options.add_entry(tag="place", width=16, padx=10, column=col_i, row=row_i+1)

        col_i += 1
        self.options.add_label(tag="county", text="County (or Country):", padx=5, column=col_i, row=row_i)
        self.options.add_entry(tag="county", width=16, padx=10, column=col_i, row=row_i+1)

        col_i += 1
        self.options.add_label(tag="dedication", text="Dedication (or Address):", padx=5, column=col_i, row=row_i)
        self.options.add_entry(tag="dedication", width=16, padx=10, column=col_i, row=row_i+1)
        row_i += 1

        row_i += 1
        col_i = 0
        self.options.add_label(tag="ringingLength", text="Lengths:", padx=5, column=col_i, row=row_i)
        self.options.add_checkbox(tag="allRingingLengths", text="All Lengths", checkState=True, column=col_i, row=row_i+1)
        self.options.add_checkbox(tag="shortTouchesRingingLengths", text="Short Touches", column=col_i, row=row_i+2)
        self.options.add_checkbox(tag="quarterRingingLengths", text="Quarter Peals", column=col_i, row=row_i+3)
        self.options.add_checkbox(tag="quartersOrLongerRingingLengths", text="Qtrs or Longer", column=col_i, row=row_i+4)
        self.options.add_checkbox(tag="dateTouchesRingingLengths", text="Date Touches", column=col_i, row=row_i+6)
        self.options.add_checkbox(tag="halfPealRingingLengths", text="Half Peals", column=col_i, row=row_i+7)
        self.options.add_checkbox(tag="pealRingingLengths", text="Peals", column=col_i, row=row_i+8)
        self.options.add_checkbox(tag="longLengthsRingingLengths", text="Long Lengths", column=col_i, row=row_i+9)

        col_i += 1
        self.options.add_label(tag="ringingMethod", text="Method (or Performance Title):", padx=5, column=col_i, row=row_i)
        self.options.add_entry(tag="ringingMethod", width=24, padx=10, column=col_i, row=row_i+1)

        col_i += 1
        self.options.add_label(tag="bellType", text="Type (Tower or Hand):", padx=5, column=col_i, row=row_i)
        bellTypeOptions = ["Tower and Hand", "Handbells Only", "Tower Bells Only"]
        self.options.add_combobox(tag="bellType", menuOptions=bellTypeOptions, width=15, column=col_i, row=row_i+1)
        #self.options.add_checkbox(tag="towerAndHand", text="Tower and Hand", column=col_i, row=row_i+1)
        #self.options.add_checkbox(tag="handbellsOnly", text="Handbells Only", column=col_i, row=row_i+2)
        #self.options.add_checkbox(tag="towerBellsOnly", text="Tower Bells Only", column=col_i, row=row_i+3)
        row_i += 9

        row_i += 1
        col_i = 0
        self.options.add_label(tag="ringerName", text="Ringer:", padx=5, column=col_i, row=row_i)
        self.options.add_entry(tag="ringerName", width=16, padx=10, column=col_i, row=row_i+1)
        self.options.add_label(tag="conductorName", text="Conductor:", padx=5, column=col_i+1, row=row_i)
        self.options.add_entry(tag="conductorName", width=16, padx=10, column=col_i+1, row=row_i+1)
        self.options.add_label(tag="composerName", text="Composer:", padx=5, column=col_i+2, row=row_i)
        self.options.add_entry(tag="composerName", width=16, padx=10, column=col_i+2, row=row_i+1)
        row_i += 1

        row_i += 1
        col_i = 0

        self.advancedOptions = BBOption(self.frame, self.backgroundColour)
        self.advancedOptions.add_label(tag="bellRung", text="Bell Rung (e.g. 2 or n-1):", padx=5, column=col_i, row=row_i)
        self.advancedOptions.add_entry(tag="bellRung", width=16, padx=10, column=col_i, row=row_i+1)
        self.advancedOptions.add_label(tag="otherRinger", text="Other Ringer:", padx=5, column=col_i+1, row=row_i)
        self.advancedOptions.add_entry(tag="otherRinger", width=16, padx=10, column=col_i+1, row=row_i+1)
        self.advancedOptions.add_label(tag="otherRingersBell", text="Other Ringer's Bell:", padx=5, column=col_i+2, row=row_i)
        self.advancedOptions.add_entry(tag="otherRingersBell", width=16, padx=10, column=col_i+2, row=row_i+1)
        row_i += 1

        row_i += 1
        col_i = 0
        self.advancedOptions.add_label(tag="compDetails", text="Composition Details:", padx=5, column=col_i, row=row_i)
        self.advancedOptions.add_entry(tag="compDetails", width=16, padx=10, column=col_i, row=row_i+1)
        row_i += 1

        row_i += 1
        col_i = 0
        self.advancedOptions.add_label(tag="footnote", text="Footnote (Contains Word):", padx=5, column=col_i, row=row_i)
        self.advancedOptions.add_entry(tag="footnote", width=16, padx=10, column=col_i, row=row_i+1)

        row_i -= 3
        col_i = 1
        self.advancedOptions.add_checkbox(tag="withPhoto", text="With Photo", column=col_i, row=row_i+1)
        self.advancedOptions.add_checkbox(tag="withComposition", text="With Composition", column=col_i, row=row_i+2)
        self.advancedOptions.add_checkbox(tag="machineReadableComposition", text="Machine-Readable Composition", column=col_i, row=row_i+3)
        self.advancedOptions.add_checkbox(tag="excludedNonCompliantPerformances", text="Exclude Non-Compliant Performances", column=col_i, row=row_i+4)
        self.advancedOptions.add_checkbox(tag="ringerIsConductor", text="Ringer is Conductor", column=col_i, row=row_i+5)
        self.advancedOptions.add_checkbox(tag="ringerIsStrapper", text="Ringer is Strapper", column=col_i, row=row_i+6)
        row_i += 6

        row_i -= 1
        col_i = 0
        self.advancedOptions.add_label(tag="orderBy", text="Order By:", padx=5, column=col_i, row=row_i)
        menuOptions = ["Date Rung", "Date Submitted", "Place", "Length",
                       "Duration", "Peal Speed", "Method (or Title)",
                       "Score From Likes", "Number of Likes", "Performance Views"]
        self.advancedOptions.add_combobox(tag="orderByMenu", menuOptions=menuOptions, width=15, column=col_i, row=row_i+1)
        #self.advancedOptions.add_checkbox(tag="orderByDateRung", text="Date Rung", column=col_i+1, row=row_i+1)
        #self.advancedOptions.add_checkbox(tag="orderByDateSubmitted", text="Date Submitted", column=col_i, row=row_i+1)
        #self.advancedOptions.add_checkbox(tag="orderByPlace", text="Place", column=col_i+1, row=row_i+2)
        #self.advancedOptions.add_checkbox(tag="orderByLength", text="Length", column=col_i, row=row_i+2)
        #self.advancedOptions.add_checkbox(tag="orderByDuration", text="Duration", column=col_i+1, row=row_i+3)
        #self.advancedOptions.add_checkbox(tag="orderByPealSpeed", text="Peal Speed", column=col_i, row=row_i+3)
        #self.advancedOptions.add_checkbox(tag="orderByMethod(orTitle)", text="Method (or Title)", column=col_i+1, row=row_i+4)
        #self.advancedOptions.add_checkbox(tag="orderByScoreFromLikes", text="Score From Likes", column=col_i, row=row_i+4)
        #self.advancedOptions.add_checkbox(tag="orderByNumberOfLikes", text="Number of Likes", column=col_i+1, row=row_i+5)
        #self.advancedOptions.add_checkbox(tag="orderByPerformanceViews", text="Performance Views", column=col_i, row=row_i+5)
        row_i += 1#1

        self.advancedOptions.add_checkbox(tag="reverseResults", text="Reverse Order of Results", checkState=True, column=col_i, row=row_i+1)

    def populate_downloadOptions(self):
        """
        Populate the tkinter frame with the download options.
        """
        import os
        self.downloadOptions = BBOption(self.frame, self.backgroundColour)
        self.downloadOptions.add_label(tag="downloadOptions", text="Download Options:", font=("Arial Bold", 16), padx=0, column=4, row=0)

        self.downloadOptions.add_label(tag="savePath", text="Save Path:", padx=0, column=4, row=1, columnspan=1)
        self.downloadOptions.add_entry(tag="savePath", sanatiseEntry=False, width=56, padx=10, column=4, row=1+1, columnspan=1)
        self.downloadOptions.entry["savePath"].set(os.path.join(os.getcwd(), ""))

        self.downloadOptions.add_checkbox(tag="downloadPDF", text="Download as PDF", checkState=True, column=4, row=3)
        self.downloadOptions.add_checkbox(tag="downloadCSV", text="Download as CSV", checkState=True, column=4, row=4)
        self.downloadOptions.add_button(tag="downloadbutton", text="Download", options=self.options, command=self.downloader.download, column=4, row=5,
                                        columnspan=2)

        self.info_text = Text(self.frame, startingText=self.programTitle, column=4, row=6, width=82, height=38,
                              columnspan=1, rowspan=23, padx=10, pady=10, sticky="NESW")

    def read_std_out(self):
        """Put stdout messages into the info_box. Called once, auto-refreshes"""
        read = self.buf.read()
        if read:
            self.add_info(read)
        self.buf.clear()#flush()
        self.after(self.print_rate, self.read_std_out)  # Call this again soon

    def add_info(self, info):
        """Add informational message to info box. Use instead of print().
        arguments: (str) info
        effects: add line with info printed to screen in info box"""
        from tkinter import DISABLED, NORMAL, END

        # A basic bit of sanatising:
        info = info.rstrip()

        self.info_text.info_text.config(state=NORMAL)
        info = str(info) + "\n"
        self.info_text.info_text.insert(END, info)
        self.info_text.info_text.see(END)
        self.info_text.info_text.config(state=DISABLED)

    def reset_print_rate(self):
        """
        Reset the print rate to its original value.
        """
        self.print_rate = self.print_rate_original


class Downloader():
    """
    Downloader class.
    """
    def __init__(self, frame, options, advancedOptions, downloadOptions=None):
        self.frame = frame
        self.options = options
        self.advancedOptions = advancedOptions
        self.downloadOptions = downloadOptions

    def update_Download(self, downloadOptions):
        """
        Function to update the Downloader class object. Used to allow the class to be initialised without
        the download options being available, as they can be passed in with this function later.
        """
        self.downloadOptions = downloadOptions

    def download(self):
        """
        Function to download files. Goes through the download options and downloads files for those options, with a seperate
        file for each ringing length, and for PDF and CSV, depending on given options.
        """
        if self.options.entry["ringerName"].get() == "" and self.options.entry["conductorName"].get() == "" and self.options.entry["composerName"].get() == "":
            print('Error: Need at least one of Ringer, Conductor, or Composer to be filled in!')
        else:

            self.urlOptions = {"Association":self.options.entry["association"].get(sanatise=False),
                               "From":self.options.entry["dateRungFrom"].get(sanatise=False),
                               "To":self.options.entry["dateRungTo"].get(sanatise=False),
                               "Place":self.options.entry["place"].get(sanatise=False),
                               "County":self.options.entry["county"].get(sanatise=False),
                               "Dedication":self.options.entry["dedication"].get(sanatise=False),
                               "All Lengths":self.options.checkbox["allRingingLengths"].get(),
                               "Short Touches":self.options.checkbox["shortTouchesRingingLengths"].get(),
                               "Quarter Peals":self.options.checkbox["quarterRingingLengths"].get(),
                               "Qtrs or Longer":self.options.checkbox["quartersOrLongerRingingLengths"].get(),
                               "Date Touches":self.options.checkbox["dateTouchesRingingLengths"].get(),
                               "Half Peals":self.options.checkbox["halfPealRingingLengths"].get(),
                               "Peals":self.options.checkbox["pealRingingLengths"].get(),
                               "Long Lengths":self.options.checkbox["longLengthsRingingLengths"].get(),
                               "Method":self.options.entry["ringingMethod"].get(sanatise=False),
                               "Bell Type":self.options.combobox["bellType"].get(),
                               "Ringer Name":self.options.entry["ringerName"].get(sanatise=False),
                               "Conductor Name":self.options.entry["conductorName"].get(sanatise=False),
                               "Composer Name":self.options.entry["composerName"].get(sanatise=False),

                               "Bell Rung":self.advancedOptions.entry["bellRung"].get(sanatise=False),
                               "Other Ringer":self.advancedOptions.entry["otherRinger"].get(sanatise=False),
                               "Other Ringer's Bell":self.advancedOptions.entry["otherRingersBell"].get(sanatise=False),

                               #comp details
                               "Composition Details":self.advancedOptions.entry["compDetails"].get(sanatise=False),
                               #footnote
                               "Footnote":self.advancedOptions.entry["footnote"].get(),

                               "With Photo":self.advancedOptions.checkbox["withPhoto"].get(),
                               "With Composition":self.advancedOptions.checkbox["withComposition"].get(),
                               "Machine-Readable Composition":self.advancedOptions.checkbox["machineReadableComposition"].get(),
                               "Exclude Non-Compliant Performances":self.advancedOptions.checkbox["excludedNonCompliantPerformances"].get(),
                               "Ringer is Conductor":self.advancedOptions.checkbox["ringerIsConductor"].get(),
                               "Ringer is Strapper":self.advancedOptions.checkbox["ringerIsStrapper"].get(),

                               "Order By":self.advancedOptions.combobox["orderByMenu"].get(),

                               "Reverse Results":self.advancedOptions.checkbox["reverseResults"].get(),

                               "PDF":self.downloadOptions.checkbox["downloadPDF"].get(),
                               "CSV":self.downloadOptions.checkbox["downloadCSV"].get()}
            self.baseUrl = "https://bb.ringingworld.co.uk/export.php?"

            # Options
            url = self.baseUrl + "&association=" + self.options.entry["association"].get()
            url += "&from=" + self.options.entry["dateRungFrom"].get()
            url += "&to=" + self.options.entry["dateRungTo"].get()
            url += "&place=" + self.options.entry["place"].get()
            url += "&region=" + self.options.entry["county"].get()
            url += "&address=" + self.options.entry["dedication"].get()
            url += "&title=" + self.options.entry["ringingMethod"].get()
            if self.options.combobox["bellType"].get() == "Tower and Hand":
                pass
            elif self.options.combobox["bellType"].get() == "Handbells Only":
                url += "&bells_type=hand"
            elif self.options.combobox["bellType"].get() == "Tower Bells Only":
               url +=  "&bells_type=tower"
            url += "&ringer=" + self.options.entry["ringerName"].get()
            url += "&conductor=" + self.options.entry["conductorName"].get()
            url += "&composer=" + self.options.entry["composerName"].get()

            # Advanced Options
            url += "&ringer_bell=" + self.advancedOptions.entry["bellRung"].get()
            url += "&ringer2=" + self.advancedOptions.entry["otherRinger"].get()
            url += "&ringer2_bell=" + self.advancedOptions.entry["otherRingersBell"].get()
            url += "&details=" + self.advancedOptions.entry["compDetails"].get()
            url += "&footnote=" + self.advancedOptions.entry["footnote"].get()
            for advancedOptionsCheckbox in self.advancedOptions.checkbox:
                if self.advancedOptions.checkbox[advancedOptionsCheckbox].get() == True:
                    if advancedOptionsCheckbox == "withPhoto":
                        url += "&has_media"
                        print("Info: Currently can only download the performances but not their photos!")#cannot download performance photos, only the performances!")
                    if advancedOptionsCheckbox == "withComposition":
                        url += "&with_composition"
                    if advancedOptionsCheckbox == "machineReadableComposition":
                        url += "&machine_comp=1"
                    if advancedOptionsCheckbox == "excludedNonCompliantPerformances":
                        url += "&compliant"
                    if advancedOptionsCheckbox == "ringerIsConductor":
                        url += "&ringer_is_conductor"
                    if advancedOptionsCheckbox == "ringerIsStrapper":
                        url += "&ringer_is_strapper"
            if self.advancedOptions.combobox["orderByMenu"].get() == "Date Rung":
                url += "&order="
            elif self.advancedOptions.combobox["orderByMenu"].get() == "Date Submitted":
                url += "&order=newest"
            elif self.advancedOptions.combobox["orderByMenu"].get() == "Place":
                url += "&order=place"
            elif self.advancedOptions.combobox["orderByMenu"].get() == "Length":
                url += "&order=changes"
            elif self.advancedOptions.combobox["orderByMenu"].get() == "Duration":
                url += "&order=duration"
            elif self.advancedOptions.combobox["orderByMenu"].get() == "Peal Speed":
                url += "&order=peal_speed"
            elif self.advancedOptions.combobox["orderByMenu"].get() == "Method (or Title)":
                url += "&order=title"
            elif self.advancedOptions.combobox["orderByMenu"].get() == "Score From Likes":
                url += "&order=Score"
            elif self.advancedOptions.combobox["orderByMenu"].get() == "Number of Likes":
                url += "&order=likes"
            elif self.advancedOptions.combobox["orderByMenu"].get() == "Performance Views":
                url += "&order=views"
            if self.advancedOptions.checkbox["reverseResults"].get() is True:
                url += "+reverse"

            # Print options being used
            downloading_output_print = ""
            downloading_output_print += "Using Options:"
            for key in self.urlOptions:
                if self.urlOptions[key] == "" or self.urlOptions[key] == False:
                    pass
                else:
                    downloading_output_print += "\n     {}: {}".format(key, self.urlOptions[key])
            print(downloading_output_print)

            print("Files to Download:")
            self.urlBefore = "{}".format(url)
            for length in self.options.checkbox:
                if self.options.checkbox[length].get() == True:
                    url += "&length="
                    if length == "allRingingLengths":
                        self.download_url(url, saveName=self.downloadOptions.entry["savePath"].get()+"_"+length,
                                          downloadPDF=self.downloadOptions.checkbox["downloadPDF"].get(),
                                          downloadCSV=self.downloadOptions.checkbox["downloadCSV"].get())
                    elif length == "shortTouchesRingingLengths":
                        url += "short"
                        self.download_url(url, saveName=self.downloadOptions.entry["savePath"].get()+"_"+length,
                                          downloadPDF=self.downloadOptions.checkbox["downloadPDF"].get(),
                                          downloadCSV=self.downloadOptions.checkbox["downloadCSV"].get())
                    elif length == "quarterRingingLengths":
                        url += "quarter"
                        self.download_url(url, saveName=self.downloadOptions.entry["savePath"].get()+"_"+length,
                                          downloadPDF=self.downloadOptions.checkbox["downloadPDF"].get(),
                                          downloadCSV=self.downloadOptions.checkbox["downloadCSV"].get())
                    elif length == "quartersOrLongerRingingLengths":
                        url += "q-or-p"
                        self.download_url(url, saveName=self.downloadOptions.entry["savePath"].get()+"_"+length,
                                          downloadPDF=self.downloadOptions.checkbox["downloadPDF"].get(),
                                          downloadCSV=self.downloadOptions.checkbox["downloadCSV"].get())
                    elif length == "dateTouchesRingingLengths":
                        url += "date"
                        self.download_url(url, saveName=self.downloadOptions.entry["savePath"].get()+"_"+length,
                                          downloadPDF=self.downloadOptions.checkbox["downloadPDF"].get(),
                                          downloadCSV=self.downloadOptions.checkbox["downloadCSV"].get())
                    elif length == "halfPealRingingLengths":
                        url += "half"
                        self.download_url(url, saveName=self.downloadOptions.entry["savePath"].get()+"_"+length,
                                          downloadPDF=self.downloadOptions.checkbox["downloadPDF"].get(),
                                          downloadCSV=self.downloadOptions.checkbox["downloadCSV"].get())
                    elif length == "pealRingingLengths":
                        url += "peal"
                        self.download_url(url, saveName=self.downloadOptions.entry["savePath"].get()+"_"+length,
                                          downloadPDF=self.downloadOptions.checkbox["downloadPDF"].get(),
                                          downloadCSV=self.downloadOptions.checkbox["downloadCSV"].get())
                    elif length == "longLengthsRingingLengths":
                        url += "long"
                        self.download_url(url, saveName=self.downloadOptions.entry["savePath"].get()+"_"+length,
                                          downloadPDF=self.downloadOptions.checkbox["downloadPDF"].get(),
                                          downloadCSV=self.downloadOptions.checkbox["downloadCSV"].get())

                url = "{}".format(self.urlBefore)

    def download_url(self, url, saveName, downloadPDF=True, downloadCSV=True):
        """
        Function to download files, downloads as PDF and/or CSV depending on passed in argumet values.
        """
        import os
        from threading import Thread

        if downloadPDF == True:
            print("   {}".format(saveName+'.pdf'))
            downloadThread_pdf = Thread(target=self._dowloadFile, args=(url+"&fmt="+"pdf", saveName+".pdf"))
            downloadThread_pdf.start()

        if downloadCSV == True:
            print("   {}".format(saveName+'.csv'))
            downloadThread_csv = Thread(target=self._dowloadFile, args=(url+"&fmt="+"csv", saveName+".csv"))
            downloadThread_csv.start()

    def _dowloadFile(self, url, saveName):
        """
        Function to do the actual download. Kept seperate to allow for multithreading.
        """
        import requests
        downloadAttmptCount = 0
        maxDownloadAttmpts = 5
        while downloadAttmptCount < maxDownloadAttmpts:
            try:
                myfile = requests.get(url)
                downloadAttmptCount = maxDownloadAttmpts + 1
            except requests.exceptions.RequestException as err:
                print("Error in downloading file:\n   "+err+"\n   Trying download again...")
                downloadAttmptCount += 1
        if downloadAttmptCount == maxDownloadAttmpts:
            print("Error: Could not download file in allowed number of attempts, please try again")
        elif downloadAttmptCount == maxDownloadAttmpts + 1:
            open(saveName, 'wb').write(myfile.content)
            print("{} downloaded!".format(saveName))


if __name__ == "__main__":
    root=tk.Tk()
    BB(root).pack(side="top", fill="both", expand=True)
    root.mainloop()
