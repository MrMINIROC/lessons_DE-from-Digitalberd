from wether_project.utils.requests_sender import WeatherFetcher
from wether_project.utils.cities import Cities
from wether_project.utils.csv_writer import write_pd
citys=Cities()
citys.add_city('Praga')
citys.add_city('Tunis')
citys.add_city('Sosnogorsk')
citys.add_city('Moscow')

write_pd(citys)

def main():
    wf = WeatherFetcher()
    results = wf.get_weather_from_csv(r"C:\Users\dm440\OneDrive\Рабочий стол\lessons_DE-from-Digitalberd\wether_project\utils\cities.csv")
    for r in results:
        print(r)

main()
