from PyPDF2 import PdfWriter

inputs = []

times = int(input("Enter how many files you want to Merge : "))

for i in range(0,times):
    files = input(f"Enter the {i+1} File name :  ")
    inputs.append(files)

merger = PdfWriter()

for pdf in inputs:
    merger.append(pdf)

output_file_name = input("Enter the output file name : ")

merger.write(output_file_name)
merger.close()