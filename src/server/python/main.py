import requests
import bs4
import re
import os
import datetime




def get_csv_link(links_dict):
    # print(links_dict)
    csv_links = {}
    for key in links_dict:
        print(links_dict[key])
        response = requests.get(links_dict[key])
        if response.status_code == 200:
            soup = bs4.BeautifulSoup(response.text, 'html.parser')
            src = soup.select('.download a')
            csv_links[key] = (src[0]["href"])

    return csv_links


def get_files(urls):
    for key in urls:
        r = requests.get(urls[key], stream=True)
        time = get_time()
        if os.path.isdir('./data/'):
            if os.path.isfile(f"./data/{key}{time}data.csv"):
                pass
            else:
                with open(f"./data/{key}{time}data.csv", "wb") as data_csv:
                    for chunk in r.iter_content(chunk_size=1024):
                        if chunk:
                            data_csv.write(chunk)
        else:
            os.makedirs('./data', exist_ok=True)
            with open(f"./data/{key}{time}data.csv", "wb") as data_csv:
                for chunk in r.iter_content(chunk_size=1024):
                    if chunk:
                        data_csv.write(chunk)


def get_links(url):
    response = requests.get(url + "/users/segdi")
    if response.status_code == 200:
        soup = bs4.BeautifulSoup(response.text, 'html.parser')
        links = soup.select(
            '.view-content .views-row article .search-result-resource a')

        data = {}
        for link in links:
            x = re.findall("positivo por COVID-19", link.text)
            y = re.findall("Fallecidos por COVID-19", link.text)
            if x:
                data["positivos"] = url + link["href"]
            elif y:
                data["fallecidos"] = url + link["href"]
        return data


def get_time():
    year = datetime.datetime.now().year
    month = datetime.datetime.now().month
    day = datetime.datetime.now().day

    return f"{day}{month}{year}"


if __name__ == "__main__":
    url = "https://www.datosabiertos.gob.pe"
    links = get_links(url)
    csv_links = get_csv_link(links)
    get_files(csv_links)
    print(csv_links)
