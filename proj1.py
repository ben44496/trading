# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import quandl
import pandas as pd
import numpy as np
import datetime

from sklearn.linear_model import LinearRegression
from sklearn import preprocessing, cross_validation, svm

quandl.ApiConfig.api_key = "yxKUKwHK1vvfgdvsi3Ci"


df = quandl.get("WIKI/AMZN")

print(df.tail())

