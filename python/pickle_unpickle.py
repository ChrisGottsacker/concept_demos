import pickle

prices = {'8GB DVD':'$1', '8GB USB':'$5'}
print(prices) # {'8GB DVD':'$1', '8GB USB':'$5'}
pickle.dump(prices, open('prices.pkl', mode='wb'))
prices = {}
print(prices) # {}
prices = pickle.load(open('prices.pkl', mode='rb'))
print(prices) # {'8GB DVD':'$1', '8GB USB':'$5'}
