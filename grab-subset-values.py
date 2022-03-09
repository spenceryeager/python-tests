# grabbing subset of values from a csv file

import pandas as pd
import numpy as np


def main():
    file = "bulb-3a.csv"
    save_loc = "bulb-3a_concat.csv"

    grabSubset(file, save_loc)


def grabSubset(file, save_loc):
    values = pd.read_csv(file)
    xList = []
    yList = []
    for i in values.iloc[0:, 0]:
        if np.remainder(i, 5) == 0:
            xList.append(i)
    for i in xList:
        # print(values[values==i].index[0])
        index = values[values.iloc[0:,0]==i].index[0]
        yList.append(values.iloc[index,1])
    
    concat = {"Wavelength": xList, "Irradiance": yList}

    concat_frame = pd.DataFrame(concat)
    concat_frame.to_csv(save_loc)

if __name__ == "__main__":
    main()