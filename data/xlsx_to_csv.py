import glob
import pandas as pd
import re

source_path = './Raw_data/ALL BILLS 21-22_Megha Sales'
destination_path = "./21-22csv"


for name in glob.glob(source_path+'/*.*'):
    # print(name)
    file_name = name.split("/")[3]
    # print(file_name)

    read_file = pd.read_excel(source_path+"/"+file_name, sheet_name=None)

    file_name = re.sub(r'\s+', '', file_name)

    for sheet_name, data in read_file.items():
        if "xlsx" in file_name:
            data.to_csv(destination_path+"/"+file_name.replace(".xlsx", ".csv"), index=False)
        else:
            data.to_csv(destination_path+"/"+file_name.replace(".xls", ".csv"), index=False)
    print("Converted "+file_name+" to csv")
