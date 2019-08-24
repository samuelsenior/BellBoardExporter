import tkinter as tk
from tkinter import ttk


class Text():
    def __init__(self, frame, startingText=None, width=None, height=None,
                 padx=0, pady=0,
                 column=None, row=None, columnspan=1, rowspan=1, sticky="W"):
        from tkinter import ttk, DISABLED, NORMAL, END
        ...
        self.startingText = startingText
        self.width=height
        self.height=height
        self.padx = padx
        self.pady = pady
        self.column = column
        self.row = row
        self.columnspan=columnspan

        self.rowspan=rowspan
        self.info_text = tk.Text(frame, bg="grey", width=self.width, height=self.height)
        self.info_text.insert(
            END, self.startingText+"\n")
        self.info_text.config(state=DISABLED)
        self.info_text.grid(column=self.column, row=self.row, columnspan=self.columnspan, rowspan=self.rowspan, padx=self.padx, pady=self.pady)
        ...


class Label():
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
        self.label.configure(text=text)

class LabelFrame():
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
        self.label.configure(text=self.text+text)


class Entry():
    def __init__(self, frame, sanatiseEntry=True, width=None, state="normal", foreground="black", background="white",##3E4149",
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

        self.entryValue = ""

        self.entry = tk.Entry(frame, width=self.width, state=self.state, foreground=self.foreground, background=self.background,)
        self.entry.grid(padx=self.padx, pady=self.pady,
                        column=self.column, row=self.row, columnspan=self.columnspan, rowspan=self.rowspan,
                        sticky=self.sticky)

    def sanatise(self):
        if self.sanatiseEntry == True:
            self.entryValue = self.entryValue.replace(" ", "+")
            self.entryValue = self.entryValue.replace("*", "%2A")
            self.entryValue = self.entryValue.replace("/", "%2F")

    def update(self):
        self.entryValue = self.entry.get()
        self.sanatise()

    def get(self):
        self.update()
        return self.entryValue

    def print(self):
        #self.update()
        print(self.entryValue)

class Checkbutton():
    def __init__(self, frame, tag=None, text=None, checkState=False, foreground="black", background="white",
                 padx=10, pady=0,
                 column=None, row=None, columnspan=1, rowspan=1, sticky="W"):

        self.tag = tag
        self.text=text
        self.checkState=checkState
        self.foreground=foreground
        self.background=background
        self.padx=padx
        self.pady=pady,
        self.column=column
        self.row=row
        self.columnspan=columnspan
        self.rowspan=rowspan
        self.sticky=sticky

        self.chk_state_var = tk.BooleanVar(value=self.checkState)
        self.checkbox = tk.Checkbutton(frame, text=self.text, variable=self.chk_state_var,
                                       onvalue=True, offvalue=False,
                                       foreground=self.foreground, background=self.background,
                                       command=self.cb)
        self.checkbox.grid(padx=self.padx, pady=self.pady,
                           column=self.column, row=self.row, columnspan=self.columnspan, rowspan=self.rowspan,
                           sticky=self.sticky)

    def cb(self):
        if self.tag is None:
            print("Check state variable is", self.chk_state_var.get())
        else:
            print("{} is {}".format(self.tag, self.chk_state_var.get()))

    def get(self):
        return self.chk_state_var.get()

    def set(self, value):
        self.chk_state_var.set(value)

class Button():
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
        self.options.entry["ringerName"].update()

        #print(self.options.entry["ringerName"].get())

        if self.command is not None:
            self.command()


class Combobox():
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
        return self.menuValue.get()

    def dropdown_callback(self, selected=None):
        print("{} set to {}".format(self.tag[0], self.menuValue.get()))
        if len(self.tag) > 1:
            print("Warning: tag with unexpected length: {}".format(self.tag))


class BBOption():
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

        self.entry[tag] = Entry(self.frame, sanatiseEntry=sanatiseEntry, width=width, state=state, foreground=foreground, background=background,
                                padx=padx, pady=pady,
                                column=column, row=row, columnspan=columnspan, rowspan=rowspan, sticky=sticky)

    def add_checkbox(self, tag, text=None, checkState=False,
                     foreground="black", background=None, padx=10, pady=0,
                     column=None, row=None, columnspan=1, rowspan=1, sticky="W"):

        if background is None:
            background = self.backgroundColour

        self.checkbox[tag] = Checkbutton(self.frame, tag=tag, text=text, checkState=checkState,
                                         foreground=foreground, background=background,
                                         padx=padx, pady=pady,
                                         column=column, row=row, columnspan=columnspan, rowspan=rowspan, sticky=sticky)

    def add_button(self, tag, options, text=None, command=None,
                   foreground="black", background=None, padx=10, pady=0,
                   column=None, row=None, columnspan=1, rowspan=1, sticky="W"):


        if background is None:
            background = self.backgroundColour

        self.button[tag] = Button(self.frame, tag=tag, options=options, text=text, command=command,
                                  foreground=foreground, background=background, padx=padx, pady=pady,
                                  column=column, row=row, columnspan=columnspan, rowspan=rowspan, sticky=sticky)

    def add_combobox(self, tag, menuOptions=None, width=None,
                     foreground="black", background=None, padx=10, pady=0,
                     column=None, row=None, columnspan=1, rowspan=1, sticky="W"):

        if background is None:
            background = self.backgroundColour

        self.combobox[tag] = Combobox(self.frame, tag=tag, menuOptions=menuOptions, width=width,
                                      foreground=foreground, background=background, padx=padx, pady=pady,
                                      column=column, row=row, columnspan=columnspan, rowspan=rowspan,
                                      sticky=sticky)


class Menu():

    def __init__(self, root):
        self.menu = tk.Menu(root)
        self.newMenuItem = tk.Menu(self.menu)
        self.newMenuItem.add_command(label="New")
        self.newMenuItem.add_command(label="Open")
        self.newMenuItem.add_separator()
        self.newMenuItem.add_command(label="Exit", command=root.destroy)
        self.menu.add_cascade(label="File", menu=self.newMenuItem)
        root.configure(menu=self.menu)


class BB(tk.Frame):
    def __init__(self, root):

        from platform import system

        self.programTitle = "Bell Board Exporter - v1.0.0"
        self.backgroundColour = "#474641"##3E4149"

        tk.Frame.__init__(self, root)
        root.configure(background=self.backgroundColour)
        root.geometry('1300x800')
        root.title(self.programTitle)

        menu = Menu(root)

        self.canvas = tk.Canvas(root, borderwidth=0, background=self.backgroundColour)
        self.frame = tk.Frame(self.canvas, background=self.backgroundColour)


        self.frame.columnconfigure(0, weight=1)
        self.frame.columnconfigure(1, weight=1)


        self.vsb = tk.Scrollbar(root, orient="vertical", command=self.canvas.yview)
        self.canvas.configure(yscrollcommand=self.vsb.set)

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

        self.vsb.pack(side="right", fill="y")
        #self.hsb.pack(side="bottom", fill="x")
        self.canvas.pack(side="left", fill="both", expand=True)
        self.canvas.create_window((4,4), window=self.frame, anchor="nw", 
                                  tags="self.frame")

        self.frame.bind("<Configure>", self._onFrameConfigure)
        self.frame.grid_propagate=1

        self.populate()
        #self.populate_downloadOptions()


        self.downloader = Downloader(self.frame, self.options, self.advancedOptions)#, self.download)

        self.populate_downloadOptions()
        self.downloader.update_Download(self.downloadOptions)


        self.info_text = Text(self.frame, startingText=self.programTitle+"\nOutput Window:", column=4, row=5, columnspan=10, rowspan=16, padx=10)
        import sys
        # If .buf exists, clear it.
        with open('.buf', 'w'):
            pass
        # Set stdout to output to .buf
        # This allows us to display a virtual terminal
        # that intercepts print(info) statements from imported classes
        sys.stdout = open(".buf", 'a')

        # Check and refresh buf -- see function for details
        self.read_std_out()
        #sys.stdout = WriteToWindow(self.downloadOptions.label["terminalOutput"].update)

        self.downloader.download()


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
        self.advancedOptions.add_checkbox(tag="withComposition", text="With Composition", column=col_i, row=row_i+1)
        self.advancedOptions.add_checkbox(tag="machineReadableComposition", text="Machine-Readable Composition", column=col_i, row=row_i+2)
        self.advancedOptions.add_checkbox(tag="excludedNonCompliantPerformances", text="Exclude Non-Compliant Performances", column=col_i, row=row_i+3)
        self.advancedOptions.add_checkbox(tag="ringerIsConductor", text="Ringer is Conductor", column=col_i, row=row_i+4)
        self.advancedOptions.add_checkbox(tag="ringerIsStrapper", text="Ringer is Strapper", column=col_i, row=row_i+6)
        row_i += 6

        row_i += 1
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
        self.downloadOptions = BBOption(self.frame, self.backgroundColour)
        self.downloadOptions.add_label(tag="downloadOptions", text="Download Options:", font=("Arial Bold", 16), padx=5, column=4, row=0)

        self.downloadOptions.add_label(tag="savePath", text="Save Path:", padx=5, column=4, row=1, columnspan=2)
        self.downloadOptions.add_entry(tag="savePath", sanatiseEntry=False, width=62, padx=10, column=4, row=1+1, columnspan=5)

        self.downloadOptions.add_checkbox(tag="downloadPDF", text="Download as PDF", checkState=True, column=4, row=3)
        self.downloadOptions.add_checkbox(tag="downloadCSV", text="Download as CSV", checkState=True, column=5, row=3)
        self.downloadOptions.add_button(tag="downloadbutton", text="Download", options=self.options, command=self.downloader.download, column=4, row=4,
                                        columnspan=2)

        #self.downloadOptions.add_label(tag="terminalOutputTitle", text="Output:", font=("Arial Bold", 14), padx=5, column=4, row=5)
        #self.downloadOptions.add_label(tag="terminalOutput", text="Testing", background="white", font=("Arial", 14), column=4, row=6)#, width=37, height=10, padx=10, column=4, row=6, columnspan=5, rowspan=8)



    def read_std_out(self):
        """Put stdout messages into the info_box. Called once, auto-refreshes"""
        import sys
        sys.stdout.flush()  # Force write
        with open('.buf', 'r') as buf:
            read = buf.read()
            if read:  # Do not write if empty
                self.add_info(read)
        with open('.buf', 'w'):
            pass  # Clear file

        sys.stdout = open(".buf", 'a')
        self.after(500, self.read_std_out)  # Call this again soon

    def add_info(self, info):
        """Add informational message to info box. Use instead of print().
        arguments: (str) info
        effects: add line with info printed to screen in info box"""
        from tkinter import DISABLED, NORMAL, END

        # A basic bit of sanatising:
        #info = info.replace('\n', '').replace('\r', '')

        self.info_text.info_text.config(state=NORMAL)
        info = "> " + str(info) + "\n"
        self.info_text.info_text.insert(END, info)
        self.info_text.info_text.see(END)
        self.info_text.info_text.config(state=DISABLED)


class Downloader():

    def __init__(self, frame, options, advancedOptions, downloadOptions=None):
        self.frame = frame
        self.options = options
        self.advancedOptions = advancedOptions
        self.downloadOptions = downloadOptions


    def update_Download(self, downloadOptions):
        self.downloadOptions = downloadOptions


    def download(self):
        if self.options.entry["ringerName"].get() == "" and self.options.entry["conductorName"].get() == "" and self.options.entry["composerName"].get() == "":
            print('Error: Need at least one of Ringer, Conductor, or Composer to be filled in!')
        else:

            self.urlOptions = {"Association":self.options.entry["association"].get(),
                               "From":self.options.entry["dateRungFrom"].get(),
                               "To":self.options.entry["dateRungTo"].get(),
                               "Place":self.options.entry["place"].get(),
                               "County":self.options.entry["county"].get(),
                               "Dedication":self.options.entry["dedication"].get(),
                               "Method":self.options.entry["ringingMethod"].get(),
                               "Bell Type":self.options.combobox["bellType"].get(),
                               "Ringer Name":self.options.entry["ringerName"].get(),
                               "Conductor Name":self.options.entry["conductorName"].get(),
                               "Composer Name":self.options.entry["composerName"].get()}
            self.baseUrl = "https://bb.ringingworld.co.uk/export.php?"

            url = self.baseUrl + "&association=" + self.options.entry["association"].get()
            url += "&from=" + self.options.entry["dateRungFrom"].get()
            url += "&to=" + self.options.entry["dateRungTo"].get()
            url += "&place=" + self.options.entry["place"].get()
            url += "&region=" + self.options.entry["county"].get()
            url += "&address=" + self.options.entry["dedication"].get()

            ### Length

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
            # Bell Rung

            # Other Ringer

            # Other Ringer's Bell

            # Composition Details

            # Footnote

            # Tick boxes
            # With Photo
            #
            # With Composition
            #
            # Machine Readable Composition
            #
            # Exclude Non-Compliant Performances
            #
            # Ringer is Conductor
            #
            # Ringer is Strapper

            # Order Rung

            # Reverse results
            #Tested
            if self.advancedOptions.checkbox["reverseResults"].checkState is True:
                url += "&order=+reverse"

            self.urlBefore = "{}".format(url)
            for length in self.options.checkbox:
                if self.options.checkbox[length].get() == True:
                    url += "&length="
                    if length == "allRingingLengths":
                        if self.downloadOptions.checkbox["downloadPDF"].checkState is True:
                            self.download_url(url, saveName=self.downloadOptions.entry["savePath"].get()+"_"+length,
                                              downloadPDF=self.downloadOptions.checkbox["downloadPDF"].checkState,
                                              downloadCSV=self.downloadOptions.checkbox["downloadCSV"].checkState)
                    elif length == "shortTouchesRingingLengths":
                        url += "short"
                        if self.downloadOptions.checkbox["downloadPDF"].checkState is True:
                            self.download_url(url, saveName=self.downloadOptions.entry["savePath"].get()+"_"+length,
                                              downloadPDF=self.downloadOptions.checkbox["downloadPDF"].checkState,
                                              downloadCSV=self.downloadOptions.checkbox["downloadCSV"].checkState)
                    elif length == "quarterRingingLengths":
                        url += "quarter"
                        if self.downloadOptions.checkbox["downloadPDF"].checkState is True:
                            self.download_url(url, saveName=self.downloadOptions.entry["savePath"].get()+"_"+length,
                                              downloadPDF=self.downloadOptions.checkbox["downloadPDF"].checkState,
                                              downloadCSV=self.downloadOptions.checkbox["downloadCSV"].checkState)
                    elif length == "quartersOrLongerRingingLengths":
                        url += "q-or-p"
                        if self.downloadOptions.checkbox["downloadPDF"].checkState is True:
                            self.download_url(url, saveName=self.downloadOptions.entry["savePath"].get()+"_"+length,
                                              downloadPDF=self.downloadOptions.checkbox["downloadPDF"].checkState,
                                              downloadCSV=self.downloadOptions.checkbox["downloadCSV"].checkState)
                    elif length == "dateTouchesRingingLengths":
                        url += "date"
                        if self.downloadOptions.checkbox["downloadPDF"].checkState is True:
                            self.download_url(url, saveName=self.downloadOptions.entry["savePath"].get()+"_"+length,
                                              downloadPDF=self.downloadOptions.checkbox["downloadPDF"].checkState,
                                              downloadCSV=self.downloadOptions.checkbox["downloadCSV"].checkState)
                    elif length == "halfPealRingingLengths":
                        url += "half"
                        if self.downloadOptions.checkbox["downloadPDF"].checkState is True:
                            self.download_url(url, saveName=self.downloadOptions.entry["savePath"].get()+"_"+length,
                                              downloadPDF=self.downloadOptions.checkbox["downloadPDF"].checkState,
                                              downloadCSV=self.downloadOptions.checkbox["downloadCSV"].checkState)
                    elif length == "pealRingingLengths":
                        url += "peal"
                        if self.downloadOptions.checkbox["downloadPDF"].checkState is True:
                            self.download_url(url, saveName=self.downloadOptions.entry["savePath"].get()+"_"+length,
                                              downloadPDF=self.downloadOptions.checkbox["downloadPDF"].checkState,
                                              downloadCSV=self.downloadOptions.checkbox["downloadCSV"].checkState)
                    elif length == "longLengthsRingingLengths":
                        url += "long"
                        if self.downloadOptions.checkbox["downloadPDF"].checkState is True:
                            self.download_url(url, saveName=self.downloadOptions.entry["savePath"].get()+"_"+length,
                                              downloadPDF=self.downloadOptions.checkbox["downloadPDF"].checkState,
                                              downloadCSV=self.downloadOptions.checkbox["downloadCSV"].checkState)

                url = "{}".format(self.urlBefore)

    def download_url(self, url, saveName, downloadPDF=True, downloadCSV=True):
        import os
        import requests

        print("Using Options:")
        for key in self.urlOptions:
            if self.urlOptions[key] == "":
                pass
            else:
                print("   {}: {}".format(key, self.urlOptions[key]))
        if downloadPDF == True:
            print("Saving to file: {}".format(saveName+'.pdf'))
            myfile = requests.get(url+"&fmt="+"pdf")
            open(saveName+'.pdf', 'wb').write(myfile.content)
            print("Done!")
        if downloadCSV == True:
            print("Saving to file: {}".format(saveName+'.csv'))
            myfile = requests.get(url+"&fmt="+"csv")
            open(saveName+'.csv', 'wb').write(myfile.content)
            print("Done!")


if __name__ == "__main__":
    root=tk.Tk()
    BB(root).pack(side="top", fill="both", expand=True)

    root.mainloop()
