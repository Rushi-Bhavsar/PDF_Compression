import os
import time
from datetime import datetime
import logging

# logging.basicConfig(filename='basic_logs.log', encoding='utf-8', level=logging.DEBUG)
# file_name = ["sample_file_1"]
# file_name = ["sample_file_1", "sample_file_2", "sample_file_3", "sample_file_4", "sample_file_5", "sample_file_6",
#              "sample_file_7", "sample_file_8", "sample_file_9", "sample_file_10", "sample_file_11"]
file_name = ["file_1", "file_2"]
for pdf_file in file_name:
    start_time = time.time()
    print(f"Start Time = {start_time}")
    pdf_file_name = str(pdf_file) + ".pdf"
    new_file_name = str(pdf_file) + "_compressed.pdf"
    print(f"Working on {pdf_file_name}")
    output = os.system(f"ps2pdf -dPDFSETTINGS=/ebook {pdf_file_name} {new_file_name}")
    # print(output)
    end_time = time.time()
    print(f"End Time = {end_time}")
    print(f"Final Time = {end_time - start_time}")
    print("=*="*50)
