import json
import argparse
from geopy.distance import vincenty


def load_data(filepath):
    with open(filepath, 'r', encoding='utf-8') as json_file:
        return json.loads(json_file.read())


def get_biggest_bar(bar_list):
    biggest_bar = max(
        bar_list,
        key=lambda bar: bar['properties']['Attributes']['SeatsCount']
    )
    return biggest_bar


def get_smallest_bar(bar_list):
    smallest_bar = min(
        bar_list,
        key=lambda bar: bar['properties']['Attributes']['SeatsCount']
    )
    return smallest_bar


def get_closest_bar(bar_list, user_location):
    closest_bar = min(
        bar_list,
        key=lambda bar: vincenty(get_bar_point(bar), user_location).m
    )
    return closest_bar


def get_bar_list(json_data):
    return json_data['features']


def get_bar_point(bar):
    longitude, latitude = bar['geometry']['coordinates']
    return longitude, latitude


def get_bar_name(bar):
    return bar['properties']['Attributes']['Name']


def get_commandline_arguments():
    parser = argparse.ArgumentParser(description='Get the link to json file.')
    parser.add_argument('filepath', type=str)
    return parser.parse_args()

if __name__ == '__main__':
    json_data = load_data(get_commandline_arguments().filepath)
    bar_list = get_bar_list(json_data)
    try:
        user_longitude, user_latitude = map(
            float,
            input('Input longitude, latitude:')
            .split()
        )
    except ValueError:
        exit('Need to enter two float values ')
    user_location = (user_longitude, user_latitude)
    print(
        'The biggest bar is: {}\n'
        'The smallest bar is: {}\n'
        'The closest bar is: {}'.format(
            get_bar_name(get_biggest_bar(bar_list)),
            get_bar_name(get_smallest_bar(bar_list)),
            get_bar_name(get_closest_bar(bar_list, user_location)),
        )
    )
