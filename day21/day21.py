import statistics
import pandas

class Statistics():
    
    def __init__(self,ages):
        self.ages=ages

    def count(self):
        return len(self.ages)

    def sum(self):
        return sum(self.ages)
    
    def min(self):
        return min(self.ages)

    def max(self):
        return max(self.ages)

    def range(self):
        return max(self.ages)-min(self.ages)

    def mean(self):
        return sum(self.ages)/len(ages)

    def median(self):
        self.ages.sort()
        return self.ages[int(len(self.ages)/2)]

    def mode(self):
        return statistics.mode(self.ages)

    def std(self):
        return statistics.stdev(self.ages)
    
    def var(self):
        return statistics.variance(self.ages)
    
    def freq_dist(self):
        a=pandas.Series(self.ages)
        return a.value_counts()
    
    def describe(self):
        return self.count(),self.sum(),self.min(),self.max(),self.range(),self.mean(),self.median(),self.mode(),self.std(),self.var(),self.freq_dist()

ages = [31, 26, 34, 37, 27, 26, 32, 32, 26, 27, 27, 24, 32, 33, 27, 25, 26, 38, 37, 31, 34, 24, 33, 29, 26]
data=Statistics(ages)

#print(data.describe())


class PersonAccount():
    def __init__(self,firstname,lastname,incomes,expenses):
        self.firstname=firstname
        self.lastname=lastname
        self.incomes=incomes
        self.expenses=expenses

    def total_income(self):
        return self.incomes

    def total_expense(self):
        return self.expenses

    def account_info(self):
        return self.firstname,self.lastname,self.incomes,self.expenses

    def add_income(self,income):
        self.incomes+=income
        return self.incomes

    def add_expense(self,expense):
        self.expenses+=expense
        return self.expenses

    def account_balance(self):
        return self.incomes-self.expenses

data=PersonAccount("firstname", "lastname", 10, 3)
data.add_income(10)
print(data.account_balance())