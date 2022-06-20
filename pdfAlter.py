from tkinter import *
from tkinter import filedialog
from pdfHighlighter import pdfHighlighter, pdfHighlighterAndSeparator
from PyPDF2 import PdfFileMerger
import re
import glob, os
import webbrowser

def callback(url):
    webbrowser.open_new(url)


def listToStringWithoutBrackets(value):
    return str(value).replace('[','').replace(']','').replace("'","")


def fileOrFolder():
    if (var.get()) == 1:

        # getTextLocation.config(text="Select Text File", font=("arial black", 15, 'bold'))
        # getPDFLocation.config(text="Select PDF File", font=("arial black", 15, 'bold'))
        browseButtonPDFFolder.place(x=425, y=999)
    elif (var.get()) == 2:

        # getTextLocation.config(text="Select Text File", font=("arial black", 15, 'bold'))
        # getPDFLocation.config(text="Select PDF File", font=("arial black", 15, 'bold'))

        browseButtonPDFFolder.place(x=425, y=200)


def UploadText():
    filetypes = (
        ('Text Files', '*.txt'),
    )

    filename = filedialog.askopenfilename(
        title='Open a file',
        filetypes=filetypes)
    file = open("text.txt", "w")
    file.write(filename)
    file.close()
    file = open("text.txt", "r")
    # data = os.path.basename(filename)
    data = file.read()
    if len(data) > 0:
        getTextLocation.config(text=data, foreground="black", font=(8))
    # savedLocation.config(text=data)

def UploadPDF():
    filetypes = (
        ('PDF Files', '*.pdf'),
    )

    filename = filedialog.askopenfilename(
        title='Open a file',
        filetypes=filetypes)
    file = open("pdf.txt", "w")
    file.write(filename)
    file.close()
    file = open("pdf.txt", "r")
    data = file.read()
    if len(data) > 0:
        getPDFLocation.config(text=data, foreground="black", font=(8))


def UploadFolder():
    oldpwd = os.getcwd()
    filetypes = (
        ('PDF Files', '*.pdf')
    )
    filename = filedialog.askdirectory()
    file = open("pdf.txt", "w")
    file.write(filename)
    file.close()
    file = open("pdf.txt", "r")
    data = file.read()

    if len(data) > 0:
        getPDFLocation.config(text=filename, foreground="black", font=(8))
        os.chdir(filename)
        file_dict = {}
        for file in glob.glob("*.pdf"):
            filepath = file
            if filepath.endswith((".pdf", ".PDF")):
                file_dict[file] = filepath
        merger = PdfFileMerger(strict=False)

        for k, v in file_dict.items():
            merger.append(v)

        os.chdir(oldpwd)
        merger.write("merged.pdf")
        merger.close()
        f = open("pdf.txt", "w")
        f.write("merged.pdf")
        f.close()
    merger.close()


def highlighter():
    root.destroy()
    f = open("text.txt", "r")
    txt = f.read()
    f.close()
    f = open("pdf.txt", "r")
    pdf = f.read()
    pdfHighlighter(txt, pdf)
    open("text.txt", "w")
    open("pdf.txt", "w")
    # open("color.ini", "w")

def separator():
    root.destroy()
    f = open("text.txt", "r")
    txt = f.read()
    f.close()
    f = open("pdf.txt", "r")
    pdf = f.read()
    pdfHighlighterAndSeparator(txt, pdf)
    open("text.txt", "w")
    open("pdf.txt", "w")
    # open("color.ini", "w")


def start():
    f = open("text.txt", "r")
    txt = f.read()
    f.close()
    f = open("pdf.txt", "r")
    pdf = f.read()
    f.close()

    if len(txt) == 0 and len(pdf) == 0:
        getTextLocation.config(text="Select TXT File", foreground="red", font=("arial black", 15, 'bold'))
        getPDFLocation.config(text="Select PDF File", foreground="red", font=("arial black", 15, 'bold'))
    elif len(txt) == 0:
        getTextLocation.config(text="Select TXT File", foreground="red", font=("arial black", 15, 'bold'))
        getPDFLocation.config(text=pdf, foreground="black", font=(8))
    elif len(pdf) == 0:
        getTextLocation.config(text=txt, foreground="black", font=(8))
        getPDFLocation.config(text="Select PDF File", foreground="red", font=("arial black", 15, 'bold'))
    else:
        if (var.get()) == 1:
            highlighter()
        elif (var.get()) == 2:
            separator()


def selectColor(event):
    label.configure(bg=variable.get())
    color = variable.get()

    if color == "Light Grey":
        red = 0.82
        green = 0.82
        blue = 0.82
        savedColor = 0
    elif color == "Light Green":
        red = 0.56
        green = 0.93
        blue = 0.56
        savedColor = 1
    elif color == "Light Blue":
        red = 0.68
        green = 0.84
        blue = 0.90
        savedColor = 2
    elif color == "Light Pink":
        red = 1
        green = 0.71
        blue = 0.75
        savedColor = 3
    elif color == "Grey":
        red = 0.50
        green = 0.50
        blue = 0.50
        savedColor = 4
    elif color == "White":
        red = 1
        green = 1
        blue = 1
        savedColor = 5
    elif color == "Black":
        red = 0
        green = 0
        blue = 0
        savedColor = 6
    elif color == "Yellow":
        red = 1
        green = 1
        blue = 0
        savedColor = 7
    elif color == "Red":
        red = 1
        green = 0
        blue = 0
        savedColor = 8
    elif color == "Blue":
        red = 0
        green = 0
        blue = 1
        savedColor = 9
    elif color == "Green":
        red = 0
        green = 0.50
        blue = 0
        savedColored = 10
    elif color == "Brown":
        red = 0.64
        green = 0.16
        blue = 0.16
        savedColor = 11
    elif color == "Orange":
        red = 1
        green = 0.64
        blue = 0
        savedColor = 12

    file = open('color.ini', 'w')
    file.write('red= ' + str(red) + '\ngreen= ' + str(green) + '\nblue= ' + str(blue) + '\nsavedColor= ' + str(savedColor) + '\ncolorName= ' + str(color))
    file.close()





colors = [
    "Light Grey",
    "Light Green",
    "Light Blue",
    "Light Pink",
    "Grey",
    "White",
    "Black",
    "Yellow",
    "Red",
    "Blue",
    "Green",
    "Brown",
    "Orange"

]

root = Tk()
open("text.txt", "w")
open("pdf.txt", "w")
open("multiColor.ini", "w")
var = IntVar(None, 1)
variable = StringVar(root)
variable.set(colors[0]) # default value
exist = os.path.exists("color.ini")
if exist is True:
    with open('color.ini') as f:
        for line in f:
            # For Python3, use print(line)
            if 'savedColor' in line:
                txt = str(line)
                receipts = str(re.findall(r'\d+(?:\.\d+)?', txt))
                game = listToStringWithoutBrackets(receipts)
                savedColor = float(game)
                variable.set(colors[int(savedColor)]) # default value
else:
    open("color.ini", "w")

root.resizable(0,0)
root.title('PDF Highlighter (Beta) - V-1.0')
root.iconbitmap('icon.ico')
root.geometry("620x620")
root.configure(bg="white")


# myFont = font.Font(family='Helvetica', size=20, weight='bold')


label = Label(root, text="PDF HIGHLIGHTER", font=("OCR A Extended", 25, 'bold'), justify='center')
label.configure(foreground="black")
label.configure(bg=variable.get())
label.place(x=160, y=20)

getTextLocation = Label(root, text="Select Text File", font=("arial black", 15, 'bold'))
getTextLocation.configure(bg="white")
getTextLocation.place(x=18, y=95)

textLabel = Label(root, text="Select text file that contains all the values you want to highlight in a PDF file. Each Value must be separated by a line space", font=(6), wraplength=580, justify='left', borderwidth=1, relief="solid", padx=7, pady=7)
textLabel.configure(bg="white")
textLabel.configure(bd=2)
textLabel.configure(foreground="grey")
textLabel.place(x=10, y=125)


browseButtonTXT = Button(root, text='Select File', command=UploadText)
browseButtonTXT.place(x=525, y=95)

getPDFLocation = Label(root, text="Select PDF File", font=("arial black", 15, 'bold'))
getPDFLocation.configure(bg="white")
getPDFLocation.place(x=18, y=200)

pdfLabel = Label(root, text="Slect PDF file/files to highlight values entered in a text file.", font=(6), wraplength=580, justify='left', borderwidth=1, relief="solid", padx=7, pady=7)
pdfLabel.configure(bg="white")
pdfLabel.configure(bd=2)
pdfLabel.configure(foreground="grey")
pdfLabel.place(x=10, y=230)

browseButtonPDF = Button(root, text='Select File', command=UploadPDF)
browseButtonPDF.place(x=525, y=200)

browseButtonPDFFolder = Button(root, text='Select Folder', command=UploadFolder)
browseButtonPDFFolder.place(x=425, y=999)

radioButtonHighlighter = Radiobutton(root, text="PDF Highlighter", variable=var,  value=1, font=(10), command=fileOrFolder)
radioButtonHighlighter.configure(bg="white")
radioButtonHighlighter.place(x=10, y=300)

radioButtonHighlighterLabel = Label(root, text="This option will create a copy of PDF file uploaded and highlight values found entered in the text file", font=(6), wraplength=580, justify='left', borderwidth=1, relief="solid", padx=7, pady=7)
radioButtonHighlighterLabel.configure(bg="white")
radioButtonHighlighterLabel.configure(bd=2)
radioButtonHighlighterLabel.configure(foreground="grey")
radioButtonHighlighterLabel.place(x=10, y=335)

radioButtonHighlighterAndExtractor = Radiobutton(root, text="PDF Hightlighter & Extractor", variable=var,  value=2, font=(10), command=fileOrFolder)
radioButtonHighlighterAndExtractor.configure(bg="white")
radioButtonHighlighterAndExtractor.place(x=10, y=400)

radioButtonHighlighterAndExtractorLabel = Label(root, text="This option will find the values entered in the text file and if value found in the PDF file will create another PDF file and add page with highlighted value in it. If text file contains 20 values and pdf file contains 100 pages. Only 20 pages will be exracted with single highlights of values in it", font=(6), wraplength=580, justify='left', borderwidth=1, relief="solid", padx=7, pady=7)
radioButtonHighlighterAndExtractorLabel.configure(bg="white")
radioButtonHighlighterAndExtractorLabel.configure(bd=2)
radioButtonHighlighterAndExtractorLabel.configure(foreground="grey")
radioButtonHighlighterAndExtractorLabel.place(x=10, y=435)

startButton = Button(root, text="S T A R T", font=("Arial", 15, 'bold'), justify='center', command=start)
startButton.configure(foreground="black")
startButton.configure(bg="light green")
startButton.place(x=255, y=540)


option = OptionMenu(root, variable, *colors, command=selectColor)
option.place(x=500, y=540)



footer = Label(root, text="softwares.rubick.org", font=(14), cursor="hand2")
footer.bind("<Button-1>", lambda e: callback("http://softwares.rubick.org"))
footer.configure(foreground="white")
footer.configure(bg="black")
footer.pack(side=BOTTOM)
root.mainloop()









