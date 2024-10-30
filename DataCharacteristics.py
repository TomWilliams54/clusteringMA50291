import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def data_init(Filename):
    
    data = pd.read_csv(Filename)
    # Calculating mean
    mean = data.mean()

    # Calculating median
    med = data.median()

    # Calculating variance
    var = data.var()

    # Calculating standard deviation
    std_dev = data.std()

    return data,mean,med,var,std_dev