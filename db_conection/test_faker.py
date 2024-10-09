import pandas as pd
import random
from faker import Faker


fake = Faker()
data = []

dates = pd.date_range('1951-01-01', '2006-12-31').to_list()

for i in range(1000):
    f_name = fake.first_name()
    l_name = fake.last_name()
    b_date = random.choice(dates)
    country = fake.country()
    email = fake.email() if random.random() > 0.3 else None
    anual_salary = random.uniform(8000.00, 300000.00)

    data.append([f_name, l_name, b_date, email, country, anual_salary])


cols = ['f_name', 'l_name', 'b_date', 'email', 'country', 'anual_salary']
df_main = pd.DataFrame(data, columns=cols)

print(df_main.head(15))