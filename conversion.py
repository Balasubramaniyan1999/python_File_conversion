import os
path = r"text_file"
file = os.listdir(path)

class conversion():
    def json_conversion(self):
        if not os.path.isdir("json_file"):
            os.mkdir("json_file")

        #dat = []

        for files in file:
            with open(os.path.join(path,files),'r+') as f:
                fi_read = f.read()
                with open(os.path.join("json_file",files.split(".")[0]+".json" ),'a') as f1:
                    f1.write(fi_read)
    def csv_conversion(self):
        if not os.path.isdir("csv_file"):
            os.mkdir("csv_file")
        for files in file:
            with open(os.path.join(path,files),'r+') as f:
                csv_read = f.read()
                with open(os.path.join("csv_file", files.split(".")[0] + ".csv"), 'a') as f2:
                    f2.write(csv_read)
    def pdf_conversion(self):
        if not os.path.isdir("pdf_file"):
            os.mkdir("pdf_file")
        for files in file:
            with open(os.path.join(path,files),'r+') as f:
                pdf_read = f.read()
                with open(os.path.join("pdf_file", files.split(".")[0] + ".pdf"), 'a') as f3:
                    f3.write(pdf_read)

if __name__ == '__main__':
    convert = conversion()
    print("choose Type-- 1.json  2.csv  3.pdf")
    user = input("Type of conversion:")
    if user == "json":
        convert.json_conversion()
    elif user == "csv":
        convert.csv_conversion()
    elif user == "pdf":
        convert.pdf_conversion()





