from utils.requests_sender import WeatherFetcher
from utils.cities import Cities
from utils.csv_writer import write_pd
import pandas as pd
from datetime import datetime

citys=Cities()
citys.add_city('Berlin')
citys.add_city('Sosnogorsk')
citys.add_city('Moscow')
citys.add_city('Voronezh')

write_pd(citys)

def main():
    wf = WeatherFetcher()
    results = wf.get_weather_from_csv(r"utils\cities.csv")
    for r in results:
        print(r)
    return results

log='/home/wether_project/logs'
results=main()
df=pd.DataFrame(results)
now = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
df.to_csv(f'{log}/{now}.csv', index=False)
