import requests
API_KEY = "72ccabdda04c0e6638fcd47ea5cfe658"


def get_data(place, days):
    url = f"http://api.openweathermap.org/data/2.5/forecast?q={place}&appid={API_KEY}"
    response = requests.get(url)
    data = response.json()
    filtered_data = data['list']
    num_values = 8 * days
    filtered_data = filtered_data[:num_values]
    return filtered_data


if __name__ == "__main__":
    print(get_data(place="Tokyo", days=3, option='Sky'))