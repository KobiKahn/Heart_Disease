import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
plt.style.use('Solarize_Light2')
import math
import statistics as stats
from scipy.stats import gaussian_kde

# FUNCTIONS

def mean(data):
    total = sum(data)
    m = total / len(data)
    return m

def median(data):
    data.sort()
    if len(data) % 2 == 0:
        m = (data[len(data) // 2] + data[len(data) // 2 - 1]) / 2
    else:
        m = data[len(data) // 2]
    return m

def variance(data):
    new_list = [(val - mean(data)) ** 2 for val in data]
    v = mean(new_list)
    return v

def stand_dev(data):
    v = variance(data)
    s = math.sqrt(v)
    return s


def plot_hist(h_list):
    for col in h_list:
        yes_list = heart1_df[col]
        no_list = heart0_df[col]
        # print(yes_list)
        # print(no_list)
        plt.hist(no_list)
        plt.hist(yes_list)
        plt.legend(['Not affected', 'Yes affected'])
        plt.title(f'{col}')
        plt.show()

def get_percent(num1, num2):
    percent1 = (num1 / (num1 + num2)) * 100
    percent2 = (num2 / (num1 + num2)) * 100
    return round(percent1, 2), round(percent2, 2)

def calc_demographics(demo):
    if demo == 'all':
        NCHD = len(heart0_df)
        CHD = len(heart1_df)
        no_percent, yes_percent = get_percent(NCHD, CHD)
        print(f'NCHD: {NCHD}     CHD: {CHD}\nNCHD: {no_percent}%     CHD: {yes_percent}%')

    elif demo == 'age':
        LE45 = heart_df.index[heart_df['age'] <= 45].tolist()
        GT45 = heart_df.index[heart_df['age'] > 45].tolist()
        LE45_df = heart_df.drop(GT45)
        GT45_df = heart_df.drop(LE45)
        LE45_no = len(LE45_df.index[LE45_df['TenYearCHD'] == 0].tolist())
        LE45_yes = len(LE45_df.index[LE45_df['TenYearCHD'] == 1].tolist())

        GT45_no = len(GT45_df.index[GT45_df['TenYearCHD'] == 0].tolist())
        GT45_yes = len(GT45_df.index[GT45_df['TenYearCHD'] == 1].tolist())
        LE_no_percent, LE_yes_percent = get_percent(LE45_no, LE45_yes)
        GT_no_percent, GT_yes_percent = get_percent(GT45_no, GT45_yes)
        print(f'LE45   NCHD: {LE45_no}     CHD: {LE45_yes}\nGT45   NCHD: {GT45_no}     CHD: {GT45_yes}\nLE45: NCHD: {LE_no_percent}%     CHD: {LE_yes_percent}%\nGT45   NCHD:{GT_no_percent}%     CHD: {GT_yes_percent}%')

    elif demo == 'gender':
        M_num = heart_df.index[heart_df['male'] == 1].tolist()
        F_num = heart_df.index[heart_df['male'] == 0].tolist()
        M_df = heart_df.drop(F_num)
        F_df = heart_df.drop(M_num)
        M_no = len(M_df.index[M_df['TenYearCHD'] == 0].tolist())
        M_yes = len(M_df.index[M_df['TenYearCHD'] == 1].tolist())
        F_no = len(F_df.index[F_df['TenYearCHD'] == 0].tolist())
        F_yes = len(F_df.index[F_df['TenYearCHD'] == 1].tolist())
        M_no_percent, M_yes_percent = get_percent(M_no, M_yes)
        F_no_percent, F_yes_percent = get_percent(F_no, F_yes)
        print(f'NCHD   Male: {M_no}     Female: {F_no}\nCHD   Male: {M_yes}     Female: {F_yes}\nMale   NCHD: {M_no_percent}%     CHD: {M_yes_percent}%\nFemale   NCHD: {F_no_percent}%     CHD: {F_yes_percent}%')

    elif demo == 'education':
        ed_1_df = heart_df[heart_df['education'] == 1]
        ed_2_df = heart_df[heart_df['education'] == 2]
        ed_3_df = heart_df[heart_df['education'] == 3]
        ed_4_df = heart_df[heart_df['education'] == 4]
        ed1_no = len(ed_1_df.index[ed_1_df['TenYearCHD'] == 0].tolist())
        ed1_yes = len(ed_1_df.index[ed_1_df['TenYearCHD'] == 1].tolist())
        ed2_no = len(ed_2_df.index[ed_2_df['TenYearCHD'] == 0].tolist())
        ed2_yes = len(ed_2_df.index[ed_2_df['TenYearCHD'] == 1].tolist())
        ed3_no = len(ed_3_df.index[ed_3_df['TenYearCHD'] == 0].tolist())
        ed3_yes = len(ed_3_df.index[ed_3_df['TenYearCHD'] == 1].tolist())
        ed4_no = len(ed_4_df.index[ed_4_df['TenYearCHD'] == 0].tolist())
        ed4_yes = len(ed_4_df.index[ed_4_df['TenYearCHD'] == 1].tolist())
        ed1_no_percent, ed1_yes_percent = get_percent(ed1_no, ed1_yes)
        ed2_no_percent, ed2_yes_percent = get_percent(ed2_no, ed2_yes)
        ed3_no_percent, ed3_yes_percent = get_percent(ed3_no, ed3_yes)
        ed4_no_percent, ed4_yes_percent = get_percent(ed4_no, ed4_yes)
        print(f'Level 1   NCHD: {ed1_no}     CHD: {ed1_yes}\nLevel 2   NCHD: {ed2_no}     CHD: {ed2_yes}\nLevel 3   NCHD: {ed3_no}     CHD: {ed3_yes}\nLevel 4   NCHD: {ed4_no}     CHD: {ed4_yes}\n\nLevel 1   NCHD: {ed1_no_percent}%     CHD: {ed1_yes_percent}%\nLevel 2   NCHD: {ed2_no_percent}%     CHD: {ed2_yes_percent}%\nLevel 3   NCHD: {ed3_no_percent}%     CHD: {ed3_yes_percent}%\nLevel 4   NCHD: {ed4_no_percent}%     CHD: {ed4_yes_percent}%')


def graph_hist(col, title):
    col_mean = mean(col)
    col_std = stand_dev(col)
    plt.subplot(1, 2, 1)
    plt.hist(col)
    plt.subplot(1, 2, 2)
    col.plot.density()
    plt.title(title)
    plt.show()

# CREATE THE TWO SEPERATE HEART DF
heart_df = pd.read_csv('Heart_stuff.csv', delim_whitespace=False)
one_list = heart_df.index[heart_df['TenYearCHD'] != 1].tolist()
zero_list = heart_df.index[heart_df['TenYearCHD'] == 1].tolist()

heart1_df = heart_df.drop(one_list)
heart1_df = heart1_df.reset_index()
heart0_df = heart_df.drop(zero_list)
heart0_df = heart0_df.reset_index()

# print(heart1_df)
# print(heart1_df)
# print()
# print(heart0_df)
plot = False
if plot:
    hist_list = ['totChol', 'BMI', 'sysBP', 'diaBP', 'glucose', 'heartRate', 'cigsPerDay']
    plot_hist(hist_list)

# calc_demographics('education')

graph_hist(heart_df['age'], 'AGE HISTOGRAM VS GAUSSIAN')












