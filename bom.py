import urllib.request
import xml.etree.ElementTree as ET

icon_map = {
    1: "☀",
    2: "🌙",
    3: "⛅",
    4: "☁",
    6: "☀",
    8: "🌧",
    9: "🌬",
    10: "🌫️",
    11: "🌦",
    12: "🌧",
    13: "🌬",
    14: "❄",
    15: "❄",
    16: "⛈",
    17: "🌦",
    18: "🌧",
    19: "🌀"
}

# QLD Precis XML - http://www.bom.gov.au/catalogue/data-feeds.shtml#precis
def get_forecast(location, index) -> dict:
    data = urllib.request.urlopen("ftp://ftp.bom.gov.au/anon/gen/fwo/IDQ11295.xml").read().decode('utf-8')
    root = ET.fromstring(data)
    for area in root.iter("area"):
        if area.get('description') == location or area.get('aac') == location:
            forecasts = area
            break
    forecast_dict = {
        "location": forecasts.get('description'),
        "index": index,
    }
    for element in forecasts[index]:
        forecast_dict[element.attrib["type"]] = element.text
    return(forecast_dict)

# QLD Observation XML - http://www.bom.gov.au/catalogue/data-feeds.shtml#obs-state

# TODO: Get full observation not just latest
def get_observation(location) -> dict:
    data = urllib.request.urlopen("ftp://ftp.bom.gov.au/anon/gen/fwo/IDQ60920.xml").read().decode('utf-8')
    root = ET.fromstring(data)
    for station in root.iter("station"):
        if station.get('description') == location:
            observation = station
            break
    observation_dict = {
        "location": observation.get("description"),
        "time-local": observation[0].attrib["time-local"]
    }
    for element in observation[0][0]:
        observation_dict[element.attrib["type"]] = element.text
    return(observation_dict)

def icon_emote(icon:int) -> dict:
    return icon_map[icon]

# TODO: Gets the latest image for a specified location
def get_radar_image(location):
    pass

# TODO: Gets the locations for a specified area/latlon
def get_forecast_loc(location):
    pass

def get_observ_loc(location):
    pass

def main():
    print(get_forecast("Robina", 1))
    print(get_observation("Coolangatta"))

if __name__ == "__main__":
    main()