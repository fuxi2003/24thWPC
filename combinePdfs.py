#!python3
#combinePdfs.py-Combine all the PDFs in the current working directory into
# a simgle PDFs
import PyPDF2, os
#Get all the PDF filenames.
pdfFiles = ['/Users/adelegrace/20180811201013546684/2018-08-13.pdf','/Users/adelegrace/20180811201013546684/2018-08-14.pdf','/Users/adelegrace/20180811201013546684/2018-08-14.pdf',
'/Users/adelegrace/20180811201013546684/2018-08-15.pdf','/Users/adelegrace/20180811201013546684/2018-08-16.pdf','/Users/adelegrace/20180811201013546684/2018-08-17.pdf',
'/Users/adelegrace/20180811201013546684/2018-08-18.pdf','/Users/adelegrace/20180811201013546684/2018-08-19.pdf','/Users/adelegrace/20180811201013546684/2018-08-20.pdf']
for filename in os.listdir('.'):
    if filename.endswith('.pdf'):
        pdfFiles.append(filename)
pdfFiles.sort(key/str.lower)

pdfWriter=PyPDF2.PdfFileWriter()
# TODO: Loop through all the PDF filenames
for filename in pdfFiles:
    pdfFileObj = open('/Users/adelegrace/20180811201013546684/2018-08-13.pdf','rb')
    pdfReader = PyPDF2.PdfFileReader(pdfFileObj)

#TODO:Loop through all the pages(except the first) and add them
for pageNum in range(1,pdfReader.numPages):
    pageObj = pdfReader.getPage(pageNum)
    pdfWriter.addPage(pageObj)
#TODO:Save the resulting PDF to a filename
pdfOutput = open('combined2018-08-1314.pdf','wb')
pdfWriter.write(pdfOutput)
pdfOutput.close()
