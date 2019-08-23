import tkinter as tk


class Label():
    def __init__(self, frame, text=None, font=("Arial Bold", 14),
                 foreground="black", background="#3E4149",
                 padx=0, pady=0,
                 column=None, row=None, columnspan=1, rowspan=1, sticky="W"):

        self.text = text
        self.font = font
        self.foreground = foreground
        self.background = background
        self.padx = padx
        self.pady = pady
        self.column = column
        self.row = row
        self.columnspan = columnspan
        self.rowspan = rowspan
        self.sticky = sticky

        self.label = tk.Label(frame, text=self.text, font=self.font, fg=self.foreground, bg=self.background)
        self.label.grid(padx=self.padx, pady=self.pady,
                        column=self.column, row=self.row, columnspan=self.columnspan, rowspan=self.rowspan,
                        sticky=self.sticky)


class Entry():
    def __init__(self, frame, width=None, state="normal", foreground="black", background="white",##3E4149",
                 padx=0, pady=0,
                 column=None, row=None, columnspan=1, rowspan=1, sticky="W"):

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
        self.entryValue = self.entryValue.replace(" ", "+")
        self.entryValue = self.entryValue.replace("*", "%2A")

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
    def __init__(self, frame, tag=None, text=None, checkState=False, foreground="black", background="#3E4149",
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

class Button():
    def __init__(self, frame, options, tag=None, text=None, foreground="black", background="#3E4149", command=None,
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

        self.button = tk.Button(frame, text='Click Me', highlightbackground='#3E4149', background=self.background, foreground=self.foreground,
                                command=self.clicked)
        self.button.grid(padx=self.padx, pady=self.pady,
                         column=self.column, row=self.row, columnspan=self.columnspan, rowspan=self.rowspan,
                         sticky=self.sticky)


    def clicked(self):
        #lbl.configure(text="Button was clicked!!")
        # update values in fields to variables storing them

        # call function to make URL for downloading specific thing

        # Download

        #res = "Welcome to " + txt.get()
        #lbl.configure(text=res)
        #txt.configure(state="disabled")
        print("Button clicked!")

        self.options.entry["ringerName"].update()

        print(self.options.entry["ringerName"].get())

        if self.command is not None:
            self.command()



class BBOption():
    def __init__(self, frame):
        self.frame = frame
        self.label = {}
        self.entry = {}
        self.checkbox = {}
        self.button = {}


    def add_label(self, tag, text=None, font=("Arial Bold", 14),
                  foreground="black", background="#3E4149", padx=0, pady=0,
                  column=None, row=None, columnspan=1, rowspan=1, sticky="W"):

        self.label[tag] = Label(self.frame, text=text, font=font,
                                foreground=foreground, background=background,
                                padx=padx, pady=pady,
                                column=column, row=row, columnspan=columnspan, rowspan=rowspan, sticky=sticky)

    def add_entry(self, tag, width=None, state="normal",
                  foreground="black", background="white", padx=0, pady=0,
                  column=None, row=None, columnspan=1, rowspan=1, sticky="W"):

        self.entry[tag] = Entry(self.frame, width=width, state=state, foreground=foreground, background=background,
                                padx=padx, pady=pady,
                                column=column, row=row, columnspan=columnspan, rowspan=rowspan, sticky=sticky)

    def add_checkbox(self, tag, text=None, checkState=False,
                     foreground="black", background="#3E4149", padx=10, pady=0,
                     column=None, row=None, columnspan=1, rowspan=1, sticky="W"):

        self.checkbox[tag] = Checkbutton(self.frame, tag=tag, text=text, checkState=checkState,
                                         foreground=foreground, background=background,
                                         padx=padx, pady=pady,
                                         column=column, row=row, columnspan=columnspan, rowspan=rowspan, sticky=sticky)

    def add_button(self, tag, options, text=None, command=None,
                   foreground="black", background="#3E4149", padx=10, pady=0,
                   column=None, row=None, columnspan=1, rowspan=1, sticky="W"):

        self.button[tag] = Button(self.frame, tag=tag, options=options, text=text, command=command,
                                  foreground=foreground, background=background, padx=padx, pady=pady,
                                  column=column, row=row, columnspan=columnspan, rowspan=rowspan, sticky=sticky)


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

        self.programTitle = "Bell Board Exporter - v0.0.1"
        self.backgroundColour = "#3E4149"

        tk.Frame.__init__(self, root)
        root.configure(background=self.backgroundColour)
        root.geometry('800x600')
        root.title(self.programTitle)
        menu = Menu(root)

        self.canvas = tk.Canvas(root, borderwidth=0, background=self.backgroundColour)
        self.frame = tk.Frame(self.canvas, background=self.backgroundColour)
        self.vsb = tk.Scrollbar(root, orient="vertical", command=self.canvas.yview)
        self.canvas.configure(yscrollcommand=self.vsb.set)

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

        self.downloader.download()


    def _onFrameConfigure(self, event):
        '''Reset the scroll region to encompass the inner frame'''
        self.canvas.configure(scrollregion=self.canvas.bbox("all"))

    def _onMousewheel_windows(self, event):
        '''Enable frame scrolling for Windows'''
        self.canvas.yview_scroll(int(-1*(event.delta/120)), "units")
        
    def _onMousewheel_linux(self, event):
        '''Enable frame scrolling for Linux'''
        self.canvas.yview_scroll(int(-1*(event.delta/120)), "units")

    def _onMousewheel_mac(self, event):
        '''Enable frame scrolling for Mac'''
        self.canvas.yview_scroll(int(-1*(event.delta)), "units")



    def populate(self):
        row_i = 0
        col_i = 0
        lbl_title = Label(self.frame, text=self.programTitle, font=("Arial Bold", 24), padx=5, column=col_i, row=row_i, columnspan=2)
        row_i += 1
        col_i = 0
        self.options = BBOption(self.frame)
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
        self.options.add_checkbox(tag="towerAndHand", text="Tower and Hand", column=col_i, row=row_i+1)
        self.options.add_checkbox(tag="handbellsOnly", text="Handbells Only", column=col_i, row=row_i+2)
        self.options.add_checkbox(tag="towerBellsOnly", text="Tower Bells Only", column=col_i, row=row_i+3)
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

        self.advancedOptions = BBOption(self.frame)
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

        #footnote.entry["footnote"].print()

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
        self.advancedOptions.add_checkbox(tag="orderByDateRung", text="Date Rung", column=col_i+1, row=row_i+1)
        self.advancedOptions.add_checkbox(tag="orderByDateSubmitted", text="Date Submitted", column=col_i, row=row_i+1)
        self.advancedOptions.add_checkbox(tag="orderByPlace", text="Place", column=col_i+1, row=row_i+2)
        self.advancedOptions.add_checkbox(tag="orderByLength", text="Length", column=col_i, row=row_i+2)
        self.advancedOptions.add_checkbox(tag="orderByDuration", text="Duration", column=col_i+1, row=row_i+3)
        self.advancedOptions.add_checkbox(tag="orderByPealSpeed", text="Peal Speed", column=col_i, row=row_i+3)
        self.advancedOptions.add_checkbox(tag="orderByMethod(orTitle)", text="Method (or Title)", column=col_i+1, row=row_i+4)
        self.advancedOptions.add_checkbox(tag="orderByScoreFromLikes", text="Score From Likes", column=col_i, row=row_i+4)
        self.advancedOptions.add_checkbox(tag="orderByNumberOfLikes", text="Number of Likes", column=col_i+1, row=row_i+5)
        self.advancedOptions.add_checkbox(tag="orderByPerformanceViews", text="Performance Views", column=col_i, row=row_i+5)
        row_i += 11

        self.advancedOptions.add_checkbox(tag="reverseResults", text="Reverse Order of Results", checkState=True, column=col_i, row=row_i+1)

    def populate_downloadOptions(self):
        self.downloadOptions = BBOption(self.frame)
        self.downloadOptions.add_label(tag="downloadOptions", text="Download Options:", font=("Arial Bold", 16), padx=5, column=4, row=0)

        self.downloadOptions.add_label(tag="savePath", text="Save Path:", padx=5, column=4, row=1, columnspan=2)
        self.downloadOptions.add_entry(tag="savePath", width=32, padx=10, column=4, row=1+1, columnspan=2)

        self.downloadOptions.add_checkbox(tag="downloadPDF", text="Download as PDF", checkState=True, column=4, row=3)
        self.downloadOptions.add_checkbox(tag="downloadCSV", text="Download as CSV", checkState=True, column=5, row=3)
        self.downloadOptions.add_button(tag="downloadbutton", options=self.options, command=self.downloader.download, text="Click here!", column=4, row=4)


class Downloader():

    def __init__(self, frame, options, advancedOptions, downloadOptions=None):
        self.frame = frame
        self.options = options
        self.advancedOptions = advancedOptions
        self.downloadOptions = downloadOptions


    def update_Download(self, downloadOptions):
        self.downloadOptions = downloadOptions


    def download(self):

        import os
 
        import requests
         
        #bar = Progressbar(self.frame, length=200)
         
        #r = requests.get(url, stream=True)

        #import requests
 
        url = "https://bb.ringingworld.co.uk/export.php?ringer=sam%2A+sen%2A&fmt=pdf"
        
        url = "https://bb.ringingworld.co.uk/export.php?"

        url += "ringer=" + self.options.entry["ringerName"].get()

        if self.downloadOptions.checkbox["downloadPDF"].checkState is True:
            url += "&fmt=" + "pdf"

        if self.advancedOptions.checkbox["reverseResults"].checkState is True:
            url += "&order=+reverse"

        print('"{}"'.format(url))

        myfile = requests.get(url)
         
        open('testing.pdf', 'wb').write(myfile.content)

         
        #with open("LearnPython.pdf", "wb") as Pypdf:
        # 
        # #   total_length = int(r.headers.get('content-length'))
        # #
        # #   for ch in progress.bar(r.iter_content(chunk_size = 2391975), expected_size=(total_length/1024) + 1):
        # #
        # #       if ch:
        # #
        #    #        Pypdf.write(ch)


if __name__ == "__main__":
    root=tk.Tk()
    BB(root).pack(side="top", fill="both", expand=True)

    root.mainloop()
