#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec 15 19:19:10 2021

@author: egehancosgun
"""

import wbdata
import datetime as dt
from linear_regression import linear_regression_function
import pandas as pd
import matplotlib.pyplot as plt


low_income_countries = [country['id'] for country in wbdata.get_country(incomelevel='LIC')]

infant_mortality = "SP.DYN.IMRT.IN"
gdp_per_capita_ppp = "NY.GDP.PCAP.PP.CD"

date_range = dt.datetime(2000, 1, 1), dt.datetime(2019, 1, 1)

infant_mortality  = wbdata.get_data(infant_mortality, country = low_income_countries, data_date = date_range)
gdp_per_capita_ppp = wbdata.get_data(gdp_per_capita_ppp, country = low_income_countries, data_date = date_range)

row_list = []
for val in list(infant_mortality): 
    row = {"Date": val["date"], "Country": val["country"]["value"],  "Infant Mortality (per 1000)": val["value"]}
    row_list.append(row)
    
infant_mortality_df = pd.DataFrame(row_list)
infant_mortality_df.to_csv("infant_mortality.csv")

row_list = []
for val in list(gdp_per_capita_ppp): 
    row = {"Date": val["date"], "Country": val["country"]["value"],  "GDP Per Capita PPP": val["value"]}
    row_list.append(row)

gdp_per_capita_ppp_df = pd.DataFrame(row_list)
gdp_per_capita_ppp_df.to_csv("gdp_per_capita_ppp.csv")

infant_mortality_df.set_index(["Date", "Country"], inplace = True)
gdp_per_capita_ppp_df.set_index(["Date", "Country"], inplace = True)

y_pred, alpha, beta, residuals, confidence_lower, confidence_upper = linear_regression_function(gdp_per_capita_ppp_df, 
                                                                            infant_mortality_df)



# Plotting

# Drop NA
nan_indices_x = gdp_per_capita_ppp_df[gdp_per_capita_ppp_df.iloc[:,-1].isnull()].index.tolist()
nan_indices_y = infant_mortality_df[infant_mortality_df.iloc[:,-1].isnull()].index.tolist()

nan_indices = list(set(nan_indices_x + nan_indices_y))

gdp_per_capita_ppp_df.drop(nan_indices, inplace = True)
infant_mortality_df.drop(nan_indices, inplace = True)

plt.scatter(gdp_per_capita_ppp_df ,infant_mortality_df, color = "turquoise" )
plt.plot(gdp_per_capita_ppp_df, y_pred, color = "brown") 
plt.plot(gdp_per_capita_ppp_df, confidence_upper, color = "r")
plt.plot(gdp_per_capita_ppp_df, confidence_lower, color = "r")
plt.title("GDP Per Capita(PPP) vs Infant Mortality")
plt.ylabel("Infant Mortality (per 1000)")
plt.xlabel("GDP Per Capita PPP ($)")






