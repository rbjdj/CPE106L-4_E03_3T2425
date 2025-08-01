import csv
import matplotlib.pyplot as plt
from io import StringIO

csv_data = '''Year,Jan,Feb,Mar,Apr,May,Jun,Jul,Aug,Sep,Oct,Nov,Dec
2012,1.423,1.442,1.395,1.426,1.412,1.403,1.427,1.407,1.401,1.422,1.418,1.436
2013,1.422,1.411,1.412,1.409,1.401,1.439,1.434,1.408,1.419,1.358,1.382,1.385
2014,1.365,1.388,1.359,1.388,1.401,1.400,1.413,1.396,1.405,1.414,1.420,1.466
2015,1.479,1.435,1.440,1.454,1.463,1.467,1.447,1.420,1.432,1.418,1.409,1.428
2016,1.425,1.407,1.416,1.406,1.382,1.333,1.349,1.341,1.329,1.343,1.362,1.362
2017,1.351,1.358,1.329,1.328,1.327,1.335,1.327,1.348,1.349,1.328,1.295,1.316
2018,1.281,1.265,1.309,1.281,1.293,1.279,1.293,1.302,1.288,1.277,1.274,1.290
2019,1.274,1.282,1.261,1.285,1.289,1.280,1.281,1.275,1.296,1.325,1.361,1.363
2020,1.351,1.375,1.374,1.406,1.412,1.474,1.485,1.495,1.492,1.503,1.515,1.538
2021,1.546,1.537,1.526,1.510,1.511,1.510,1.491,1.467,1.580,1.526,1.547,1.532
2022,1.555,1.578,1.607,1.612,1.606,1.691,1.716,1.734,1.746,1.768,1.773,1.778
'''

csv_file = StringIO(csv_data)
reader = csv.reader(csv_file)
headers = next(reader)  # skip header

years = []
average_prices = []

for row in reader:
    year = int(row[0])
    monthly_prices = [float(value) for value in row[1:]]
    average_price = sum(monthly_prices) / len(monthly_prices)
    years.append(year)
    average_prices.append(average_price)

# Plotting
plt.figure(figsize=(10, 6))
plt.plot(years, average_prices, marker='o', linestyle='-', color='brown', label='Average Bread Price')
plt.title('Average Price of Bread Over Time')
plt.xlabel('Year')
plt.ylabel('Price (in USD)')
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show()
