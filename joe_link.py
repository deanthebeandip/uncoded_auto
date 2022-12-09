from re import L
import pandas as pd
import matplotlib.pyplot as plt
import math
import os
import shutil

from math import isnan
import time
import seaborn as sns
import matplotlib.pyplot as plt 
# from matplotlib import dates
import matplotlib.dates as mdates
from datetime import timedelta
import numpy as np
import plotly.graph_objects as go
from pptx import Presentation
from pptx.enum.text import PP_ALIGN
from pptx.dml.color import RGBColor
from pptx.enum.dml import MSO_THEME_COLOR
from pptx.util import Pt
from pptx.util import Inches
from tqdm import tqdm
from openpyxl import load_workbook


import urllib.request, json 


def link_data(link):
    start = time.time()
    # with urllib.request.urlopen(link) as url:
    #     data = json.load(url)
    data = pd.read_csv(link)
    

    end = time.time()
    t_d = end - start
    print("Total time it took to load: %d" % t_d)
    return data



def create_report(plant_name):
    pass


def link_api(base_link, date, stime, etime):
    # grab the base link, return link with correct date and time range...

    pass

def df_to_csv(data, filename, path):
    data.to_csv(filename)


def main():
    marion_test = 'http://mrnstg.na.graphicpkg.pri:8088/system/webdev/GPI_MES_CORP/DowntimeMESExport/?start=2022-12-08%2007:00:00%20-05:00&end=2022-12-08%2019:00:00%20-05:00'
    # marion_production = 'http://mrn.na.graphicpkg.pri:8088/system/webdev/GPI_MES_CORP/DowntimeMESExport/?start=2022-12-07%2007:00:36%20-05:00&end=2022-12-08%2007:00:00%20-05:00'
    marion_production = 'http://mrn.na.graphicpkg.pri:8088/system/webdev/GPI_MES_CORP/DowntimeMESExport/?start=2022-12-08%2007:00:00%20-05:00&end=2022-12-8%2019:00:00%20-05:00'
    test_link = marion_test
    # test_link = marion_production
    
    data = link_data(test_link)

    df_to_csv(data, 'marion_stage_221209.csv', ".")

    # print(data.values)
    # for line in data.values:
    #     print(line)

    # for d in data:
    #     print(data[d])

    print('testing git')







if __name__ == '__main__':
    main()

















'''
ddloader:
    # ig_date = []
    # month_list = []
    # df1 = pd.read_excel(dd_file)
    # month_list.append(df1)
    # combined = pd.concat(month_list, ignore_index=True)

    # qv_date = []
    # qv_table = pd.read_excel(dd_qv_path)

    # qv_date = qv_table['Date'].to_list()
    # ig_date = list(set(combined['Scheduled Shift Start Date Time'].to_list()))
    # qv_date = [dt2d(d2) for d2 in qv_date]
    # ig_date = [dt2d(d) for d in ig_date]
    # qv_date = list(set(qv_date))
    # ig_date = list(set(ig_date))


'''