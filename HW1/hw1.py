#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 18 02:07:19 2021

@author: egehancosgun
"""
import random
random.seed(40557) # My ID number


class Portfolio():
    
    def __init__(self):
        
        self.cash = 0
        self.stocks = {}
        self.mutual_funds = {}
        self.hist = ""
        
    def __str__(self):
        
        statement = "Portfolio Holdings are given below: \n" + "Cash: " + str(self.cash) + "$\n"
        if len(self.stocks) > 0:
            statement += "Stocks: "
            for i in [str(value[0]) + " " + key for key, value in self.stocks.items()]:
                statement += i + "\n"
        if len(self.mutual_funds) > 0:
            statement += "Mutual Funds: "
            for i in [str(value[0]) + " " + key for key, value in self.mutual_funds.items()]:
                statement += i + "\n"
        
        return statement 
    
    def addCash(self, cash):
    
        self.cash += cash
        self.hist += "\n" + "Action Type: Cash Addition: " + "$" + str(cash) + " has been added to your account."
    
    def withdrawCash(self, cash):
        
        if self.cash < cash: 
            print("There is not enough cash balance of $", cash ," to withdraw in the account.")
        else:
            self.cash = self.cash - cash
            self.hist += "\n" + "Action Type: Cash Withdrawal: " + "$" + str(cash) + " has been withdrawn from your account."
            
    def buyStock(self, shares, stock):
        
        amount = stock.price * int(shares) 
        if self.cash >= amount:
            self.withdrawCash(amount)
            if stock.ticker not in self.stocks.keys():   
                self.stocks[stock.ticker] = [int(shares), stock.price]
            else:
                owned = self.stocks[stock.ticker][0]
                self.stocks[stock.ticker] = [owned + int(shares), stock.price]
            self.hist += "\n" + "Action Type: Stock Purchase: " + str(int(shares)) + " shares of " + str(stock.ticker)
            self.hist += " has been purchased for $" + str(amount) + "."
        else:
            print("You do not have enough account balance to buy.")
    
    def sellStock(self, ticker, shares):
        
        if (ticker not in self.stocks.keys()) or (self.stocks[ticker][0] == 0):
            print("Sorry, you do not have this stock. ")
        else:
            owned = self.stocks[ticker][0]
            if shares > owned:
                print("Sorry you cannot sell more than you have.")
            else:
                owned = owned - shares 
                buy_price = self.stocks[ticker][1]
                sell_price = random.uniform(0.5 * buy_price, 1.5 * buy_price)
                self.stocks[ticker] = [owned, buy_price]
                self.hist += "\n" + "Action Type: Stock Sale: " + str(int(shares)) + " shares of " + str(ticker)
                self.hist += " has been sold for $" + str(sell_price * shares) + ". Sell price is $" + str(sell_price) + " per share."
                self.addCash(sell_price * shares)
                
    def buyMutualFund(self, shares, mf):
        
        amount = float(shares) * 1
        if self.cash >= amount:
            self.withdrawCash(amount)
            if mf.ticker not in self.mutual_funds.keys():   
                self.mutual_funds[mf.ticker] = [float(shares), 1]
            else:
                owned = self.mutual_funds[mf.ticker][0]
                self.mutual_funds[mf.ticker] = [owned + float(shares), 1]
            self.hist += "\n" + "Action Type: Mutual Fund Purchase: " + str(float(shares)) + " shares of " + str(mf.ticker)
            self.hist += " has been purchased for $" + str(amount) + "."
        else:
            print("You do not have enough account balance to buy.")
            
    def sellMutualFund(self, ticker, shares):
        
        if (ticker not in self.mutual_funds.keys()) or (self.mutual_funds[ticker][0] == 0):
            print("Sorry, you do not have this mutual fund. ")
        else:
            owned = self.mutual_funds[ticker][0]
            if shares > owned:
                print("Sorry you cannot sell more than you have.")
            else:
                owned = owned - shares 
                sell_price = random.uniform(0.9, 1.2)
                self.mutual_funds[ticker] = [owned, 1]
                self.hist += "\n" + "Action Type: Mutual Fund Sale: " + str(float(shares)) + " shares of " + str(ticker)
                self.hist += " has been sold for $" + str(sell_price * shares) + ". Sell price is $" + str(sell_price) + " per share."
                self.addCash(sell_price * shares)
                
    def history(self):
        
        print(self.hist)
    
class Stock():
    
    def __init__(self, price, ticker):
        
        self.price = price
        self.ticker = ticker
        
class MutualFund():
    
    def __init__(self, ticker):
        
        self.price = 1
        self.ticker = ticker
        

