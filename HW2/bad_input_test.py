#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec 26 21:30:00 2021

@author: egehancosgun
"""

import pandas as pd
import wbdata
import datetime as dt
from linear_regression import linear_regression_function
import matplotlib.pyplot as plt

low_income_countries = [country['id'] for country in wbdata.get_country(incomelevel='LIC')]
date_range = dt.datetime(2010, 1, 1), dt.datetime(2019, 1, 1)
gdp_per_capita_ppp = "NY.GDP.PCAP.PP.CD"

# Independent variable has many NA values
harmonized_test_scores  = wbdata.get_data("HD.HCI.HLOS", country = low_income_countries, data_date = date_range)
gdp_per_capita_ppp = wbdata.get_data(gdp_per_capita_ppp, country = low_income_countries, data_date = date_range)

row_list = []
for val in list(harmonized_test_scores): 
    row = {"Date": val["date"], "Country": val["country"]["value"],  "Harmonized Test Scores": val["value"]}
    row_list.append(row)
    
harmonized_test_scores_df = pd.DataFrame(row_list)
harmonized_test_scores_df.to_csv("harmonized_test_scores.csv")

row_list = []
for val in list(gdp_per_capita_ppp): 
    row = {"Date": val["date"], "Country": val["country"]["value"],  "GDP Per Capita PPP": val["value"]}
    row_list.append(row)

gdp_per_capita_ppp_df = pd.DataFrame(row_list)
gdp_per_capita_ppp_df.to_csv("gdp_per_capita_ppp.csv")

harmonized_test_scores_df.set_index(["Date", "Country"], inplace = True)
gdp_per_capita_ppp_df.set_index(["Date", "Country"], inplace = True)

y_pred, alpha, beta, residuals, confidence_lower, confidence_upper = linear_regression_function(gdp_per_capita_ppp_df, 
                                                                            harmonized_test_scores_df)

# Plotting

# Drop NA
nan_indices_x = gdp_per_capita_ppp_df[gdp_per_capita_ppp_df.iloc[:,-1].isnull()].index.tolist()
nan_indices_y = harmonized_test_scores_df[harmonized_test_scores_df.iloc[:,-1].isnull()].index.tolist()

nan_indices = list(set(nan_indices_x + nan_indices_y))

gdp_per_capita_ppp_df.drop(nan_indices, inplace = True)
harmonized_test_scores_df.drop(nan_indices, inplace = True)

plt.scatter(gdp_per_capita_ppp_df ,harmonized_test_scores_df, color = "turquoise" )
plt.plot(gdp_per_capita_ppp_df, y_pred, color = "brown") 
plt.plot(gdp_per_capita_ppp_df, confidence_upper, color = "r")
plt.plot(gdp_per_capita_ppp_df, confidence_lower, color = "r")
plt.ylabel("Harmonized Test Scores")
plt.xlabel("GDP Per Capita PPP ($)")
