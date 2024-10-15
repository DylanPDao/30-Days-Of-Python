from collections import Counter

class Statistics:
    def __init__(self, data):
        self.data = sorted(data)
    
    def count(self):
        return len(self.data)
    
    def sum(self):
        return sum(self.data)
    
    def min(self):
        return min(self.data)
    
    def max(self):
        return max(self.data)
    
    def range(self):
        return self.max() - self.min()
    
    def mean(self):
        return self.sum() / self.count()
    
    def median(self):
        n = self.count()
        middle = n // 2
        if n % 2 == 0:
            return (self.data[middle - 1] + self.data[middle]) / 2
        else:
            return self.data[middle]
    
    def mode(self):
        data_counter = Counter(self.data)
        mode_data = data_counter.most_common(1)[0]
        return {'mode': mode_data[0], 'count': mode_data[1]}
    
    def std(self):
        mean = self.mean()
        variance = sum((x - mean) ** 2 for x in self.data) / self.count()
        return variance ** 0.5
    
    def var(self):
        mean = self.mean()
        return sum((x - mean) ** 2 for x in self.data) / self.count()
    
    def freq_dist(self):
        freq_dist = Counter(self.data)
        return sorted(freq_dist.items(), key=lambda x: x[1], reverse=True)

# Sample data for testing
data = [26, 26, 32, 24, 37, 27, 29, 26, 33, 34, 38, 26, 31, 27, 29, 25, 30, 29, 25, 31, 25, 30, 31, 25, 30]

# Create Statistics object
statistics = Statistics(data)

# Output
print('Count:', statistics.count()) 
print('Sum: ', statistics.sum()) 
print('Min: ', statistics.min()) 
print('Max: ', statistics.max()) 
print('Range: ', statistics.range()) 
print('Mean: ', statistics.mean()) 
print('Median: ', statistics.median()) 
print('Mode: ', statistics.mode()) 
print('Standard Deviation: ', statistics.std()) 
print('Variance: ', statistics.var()) 
print('Frequency Distribution: ', statistics.freq_dist()) 

class PersonAccount:
    def __init__(self, firstname, lastname, incomes, expenses, total_income, total_expense, account_info, add_income, add_expense, account_balance):
        self.firstname = firstname
        self.lastname = lastname
        self.incomes = incomes
        self.expenses = expenses
        self.total_income = total_income
        self.total_expense = total_expense
        self.account_info = account_info
        self.add_income = add_income
        self.add_expense = add_expense
        self.account_balance = account_balance

