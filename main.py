import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
plt.style.use('Solarize_Light2')
import math
import statistics as stats

# FUNCTIONS
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
hist_list = ['totChol', 'BMI', 'sysBP', 'diaBP', 'glucose', 'heartRate', 'cigsPerDay']
plot_hist(hist_list)

# for each risk
# factor for those who are not at risk and those that are.
# print(heart_df)












