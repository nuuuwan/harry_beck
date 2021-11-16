import json

from harry_beck._utils import log


class Map:
    def __init__(self, places, roads):
        self.__places__ = places
        self.__roads__ = roads

    def __str__(self):
        return json.dumps(
            dict(places=self.__places__, roads=self.__roads__), indent=1
        )

    def validate(self):
        for road, road_places in self.__roads__.items():
            for place in road_places:
                if place not in self.__places__:
                    log.error(f'Missing place in {road}: {place}')

    @staticmethod
    def create_example1():
        places = {
            'Colombo': [0, 0],
            'Ambepussa': [0.5, 0.5],
            'Kandy': [1.5, 0.5],
            'Kurunegala': [1, 1],
            'Dambulla': [2, 2],
            'Trincomalee': [3, 3],
            'Puttalam': [0, 2],
        }
        roads = {
            'A1': ['Colombo', 'Ambepussa', 'Kandy'],
            'A3': ['Colombo', 'Puttalam'],
            'A6': ['Ambepussa', 'Kurunegala', 'Dambulla', 'Trincomalee'],
            'A10': ['Kandy', 'Kurunegala', 'Puttalam'],
        }
        return Map(places, roads)


if __name__ == '__main__':
    m = Map.create_example1()
    m.validate()
    print(m)
