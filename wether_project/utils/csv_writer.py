import pandas as pd

def write_pd(name):
    df=pd.DataFrame(name.get_city())
    df.to_csv(r'utils\cities.csv', index=False)
