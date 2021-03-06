# %load q02_get_wicket_delivery_numbers_array/build.py
#Default Imports
import numpy as np

ipl_matches_array =np.genfromtxt('data/ipl_matches_small.csv', dtype='|S50', skip_header=1, delimiter=',')

#Your Solution
def get_wicket_delivery_numbers_array(player = 'player'):
    out_deliveries = np.array([])
    for index, x in enumerate(ipl_matches_array):
        if x[20] == b'ST Jayasuriya':
            out_deliveries = np.append(out_deliveries, x[11])
    return out_deliveries




