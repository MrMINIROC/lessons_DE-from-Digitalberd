import pandas as pd

def write_pd(name):
    df=pd.DataFrame(name.get_city())
    df.to_csv(r'C:\Users\dm440\OneDrive\Рабочий стол\lessons_DE-from-Digitalberd\wether_project\utils\cities.csv', index=False)
