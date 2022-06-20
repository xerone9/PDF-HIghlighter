import fitz
from PyPDF2 import PdfFileReader, PdfFileWriter
import re
import os
import random
import sys
# sys.stderr = open('file', 'w')

desktop = os.path.expanduser("~\desktop\\")

def listToStringWithoutBrackets(value):
    return str(value).replace('[','').replace(']','').replace("'","")


def pdfHighlighter(txt, pdf):
    if os.path.getsize(txt) < 1:
        print("Text File Attached is empty. Please Recheck")
        print("")
        input("Press Enter To Exit...")
    elif os.path.getsize(pdf) < 1:
        print("PDF File Attached is empty. Please Recheck")
        print("")
        input("Press Enter To Exit...")
    else:
        notFound = []
        found = []
        values = []
        occurs = []
        repeatedValues = []
        multiColor = 0


        doc = fitz.open(pdf)

        file1 = open(txt, 'r')
        Lines = file1.readlines()
        count = 0
        print("Searching! Please Wait...")
        print("")
        for line in Lines:
            count += 1
            String = line.strip()
            if String not in values:
                values.append(String)
                occurence = 0
                multiColor += 1

                for page in doc:
                    text = str(String)
                    text_instances = page.search_for(text)
                    receipts = [int(s) for s in str(page).split() if s.isdigit()]
                    pages = int(listToStringWithoutBrackets(receipts))


                    object = PdfFileReader(pdf)
                    PageObj = object.getPage(pages)
                    Text = PageObj.extractText()
                    ResSearch = re.search(String, Text)



                    if ResSearch is not None:
                        fileName = os.path.basename(pdf)
                        print('Value Found: ' + text + ' On Page ' + str(pages+1) + ' in file ' + fileName)

                        if text not in found:
                            found.append(text)

                        for inst in text_instances:
                            highlight = page.add_highlight_annot(inst)
                            red = 0.72
                            green = 0.72
                            blue = 0.72

                            if count == 1:
                                with open('color.ini') as f:
                                    for line in f:
                                        # For Python3, use print(line)
                                        if 'red' in line:
                                            txt = str(line)
                                            removingSpace = str((txt.split("= ", 1)[1])).replace("\n", "")
                                            red = float(removingSpace)
                                        if 'green' in line:
                                            txt = str(line)
                                            removingSpace = str((txt.split("= ", 1)[1])).replace("\n", "")
                                            green = float(removingSpace)
                                        if 'blue' in line:
                                            txt = str(line)
                                            removingSpace = str((txt.split("= ", 1)[1])).replace("\n", "")
                                            blue = float(removingSpace)
                            else:
                                with open('multiColor.ini') as f:
                                    for line in f:
                                        # For Python3, use print(line)
                                        if 'red' in line:
                                            txt = str(line)
                                            removingSpace = str((txt.split("= ", 1)[1])).replace("\n", "")
                                            red = float(removingSpace)
                                        if 'green' in line:
                                            txt = str(line)
                                            removingSpace = str((txt.split("= ", 1)[1])).replace("\n", "")
                                            green = float(removingSpace)
                                        if 'blue' in line:
                                            txt = str(line)
                                            removingSpace = str((txt.split("= ", 1)[1])).replace("\n", "")
                                            blue = float(removingSpace)

                                if occurence == 0 and count != 1:
                                    red = random.uniform(0.50, 0.90)
                                    green - random.uniform(0.50, 0.90)
                                    blue = random.uniform(0.50, 0.90)
                                    file = open("multiColor.ini", "w")
                                    file.write("red= " + str(red) + "\ngreen= " + str(green) + "\nblue = " + str(blue))
                                    file.close()


                            highlight.set_colors({"stroke":(red, green, blue)})
                            highlight.update()
                            doc.save(desktop + "RUBICK.pdf", garbage=4, deflate=True, clean=True)
                            occurence += 1

                            # print(text + " " + str(occurence))

                    else:
                        if text not in found and text not in notFound:
                            notFound.append(text)

                occurs.append(occurence)

            else:
                repeatedValues.append(String)


    missing = list(set(found).symmetric_difference(set(notFound)))
    # missed = list(set(found).symmetric_difference(set(notFound).symmetric_difference(set(missing))))

    print("")

    if len(found) == 0:
        print("No Value Found")
        print("")
        input("Press Enter To Exit...")

    else:
        if len(notFound) == 0:
            print("All Values Found")
        else:
            for value in missing:
                if value not in found:
                    print('Value Not Found: ' + value)

                # print(notFound)

        print("")

        for value, counts in zip(found, occurs):
            print(value + ': occurs ' + str(counts) + ' times')
        print("")

        if len(repeatedValues) != 0:
            for value in repeatedValues:
                print(value + ' - REPEATED VALUE !!!')
        print("")

        print("")
        input("Please Note if there is any Missing Values and Press Enter to Open Output File...")
        open("text.txt", "w")
        open("pdf.txt", "w")
        os.startfile(desktop + 'RUBICK.pdf')
        # print("")
        # print(found)
        # print(notFound)
        # print(occurs)





def pdfHighlighterAndSeparator(txt, pdf):
    # isDirectory = os.path.isdir(pdf)
    # if isDirectory is True:
    #     os.chdir(pdf)
    #     file_dict = {}
    #     for file in glob.glob("*.pdf"):
    #         filepath = file
    #         if filepath.endswith((".pdf", ".PDF")):
    #             file_dict[file] = filepath
    #     merger = PdfFileMerger(strict=False)
    #
    #     for k, v in file_dict.items():
    #         merger.append(v)
    #
    #     merger.write(pdf + "/merged.pdf")
    #     merger.close()
    #     pdf = pdf + "/merged.pdf"
    # else:
    #     pass
    if os.path.getsize(txt) < 1:
        print("Text File Attached is empty. Please Recheck")
        print("")
        input("Press Enter To Exit...")
    elif os.path.getsize(pdf) < 1:
        print("PDF File Attached is empty. Please Recheck")
        print("")
        input("Press Enter To Exit...")
    else:
        notFound = []
        found = []
        values = []
        occurs = []
        repeatedValues = []
        pdfWriter = PdfFileWriter()
        doc = fitz.open(pdf)


        file1 = open(txt, 'r')
        Lines = file1.readlines()
        count = 0
        print("Searching! Please Wait...")
        print("")
        for line in Lines:
            count += 1
            String = line.strip()

            for page in doc:
                text = str(String)
                text_instances = page.search_for(text)
                receipts = [int(s) for s in str(page).split() if s.isdigit()]
                pages = int(listToStringWithoutBrackets(receipts))

                object = PdfFileReader(pdf)
                PageObj = object.getPage(pages)
                Text = PageObj.extractText()
                ResSearch = re.search(String, Text)

                if ResSearch is not None:
                    fileName = os.path.basename(pdf)
                    print('Value Found: ' + text + ' On Page ' + str(pages + 1) + ' in file ' + fileName)
                    if text not in found:
                        found.append(text)

                    for inst in text_instances:
                        highlight = page.add_highlight_annot(inst)
                        red = 0.72
                        green = 0.72
                        blue = 0.72

                        with open('color.ini') as f:
                            for line in f:
                                # For Python3, use print(line)
                                if 'red' in line:
                                    txt = str(line)
                                    removingSpace = str((txt.split("= ", 1)[1])).replace("\n", "")
                                    red = float(removingSpace)
                                if 'green' in line:
                                    txt = str(line)
                                    removingSpace = str((txt.split("= ", 1)[1])).replace("\n", "")
                                    green = float(removingSpace)
                                if 'blue' in line:
                                    txt = str(line)
                                    removingSpace = str((txt.split("= ", 1)[1])).replace("\n", "")
                                    blue = float(removingSpace)

                        highlight.set_colors({"stroke": (red, green, blue)})
                        highlight.update()
                        doc.save("output.pdf", garbage=4, deflate=True, clean=True)

                        pdf_file_path = "output.pdf"
                        pdfExtractor = PdfFileReader(pdf_file_path)
                        file_base_name = pdf_file_path.replace('.pdf', '')

                        pdfWriter.addPage(pdfExtractor.getPage(pages))

                        with open(desktop + 'RUBICK.pdf'.format(file_base_name), 'wb') as f:
                            pdfWriter.write(f)
                            f.close()
                            annot = page.firstAnnot
                            while annot:
                                annot = page.delete_annot(annot)
                            doc.save("output.pdf", garbage=4, deflate=True, clean=True)


                else:
                    if text not in found:
                        notFound.append(text)
        try:
            os.remove("output.pdf")
        except FileNotFoundError:
            pass
        missing = list(set(found).symmetric_difference(set(notFound)))

        print("")

        if len(found) == 0:
            print("No Value Found")
            print("")
            input("Press Enter To Exit...")

        else:
            if len(notFound) == 0:
                print("All Values Found")
            else:
                for value in missing:
                    if value not in found:
                        print('Value Not Found: ' + value)

                    # print(notFound)

                print("")

                for value, counts in zip(found, occurs):
                    print(value + ': occurs ' + str(counts) + ' times')
                print("")

                if len(repeatedValues) != 0:
                    for value in repeatedValues:
                        print(value + ' - REPEATED VALUE !!!')
                print("")

                print("")
                input("Please Note if there is any Missing Values and Press Enter to Open Output File...")
                open("text.txt", "w")
                open("pdf.txt", "w")
                os.startfile(desktop + 'RUBICK.pdf')
