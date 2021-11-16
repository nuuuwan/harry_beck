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
            'Akuressa': [1.5, -2.5],
            'Ambepussa': [1, 1],
            'Anuradhapura': [2.75, 4],
            'Avissawella': [1, 0],
            'Badulla': [5, 0],
            'Batticaloa': [6.5, 1.5],
            'Colombo': [0, 0],
            'Dambulla': [3, 3],
            'Galle': [0, -4],
            'Habarana': [3.5, 3.5],
            'Hambantota': [5, -4],
            'Horowupotana': [4, 5],
            'Jaffna': [3, 8],
            'Kalkudah': [6.5, 3.5],
            'Kandy': [3, 1],
            'Kurunegala': [2, 2],
            'Madampe': [3.5, -2.5],
            'Mankulam': [3, 6],
            'Mannar': [1.5, 6.5],
            'Maradankadawala': [3, 3.5],
            'Matara': [1.5, -4],
            'Medawachchiya': [3, 5],
            'Mihintale': [3, 4],
            'Mullaitivu': [3.5, 6.5],
            'Nonagama': [3.5, -4],
            'Nuwara-Eliya': [3, 0],
            'Panadura': [0, -1.5],
            'Paraiyanalankulam': [2, 6],
            'Parantan': [3, 7],
            'Pelmadulla': [2.5, -1.5],
            'Polonnaruwa': [5, 3.5],
            'Pottuvil': [6.5, 0],
            'Puttalam': [0, 4],
            'Ratnapura': [1, -1.5],
            'Trincomalee': [5, 5],
            'Vavuniya': [3, 6],
            'Wellawaya': [5, -1.5],
            'Padiyathalawa': [6, 1],
            'Galkulama': [3, 3.75],
            'Beragala': [3, -1.5],
            'Hali-Ela': [4.5, 0],
            'Kegalle': [1.5, 1],
            'Polgahawela': [1.5, 1.5],
            'Rambewa': [3, 4.25],
            'Karawanella': [2.5, 0],
            'Passara': [5.5, 0.5],
            'Moneragala': [5.5, -1],
            'Kumbalwela': [4, -0.5],
            'Maha Oya': [6.25, 1.25],
            'Ampara': [6.25, 0.75],
            'Siyambalanduwa': [6.25, -0.25],
            'Padeniya': [1.375, 2.625],
            'Karaitivu': [6.5, 1.0],
            'Ja-Ela': [0, 0.5],
            'Yakkala': [0.5, 0.5],
        }
        roads = {
            'A1': ['Colombo', 'Yakkala', 'Ambepussa', 'Kandy'],
            'A2': [
                'Colombo',
                'Panadura',
                'Galle',
                'Matara',
                'Nonagama',
                'Hambantota',
                'Wellawaya',
            ],
            'A3': ['Colombo', 'Ja-Ela', 'Puttalam'],
            'A4': [
                'Colombo',
                'Avissawella',
                'Ratnapura',
                'Pelmadulla',
                'Wellawaya',
                'Moneragala',
                'Siyambalanduwa',
                'Pottuvil',
                'Karaitivu',
                'Batticaloa',
            ],
            'A5': [
                'Kandy',
                'Nuwara-Eliya',
                'Badulla',
                'Passara',
                'Padiyathalawa',
                'Maha Oya',
                'Batticaloa',
            ],
            'A6': [
                'Ambepussa',
                'Kurunegala',
                'Dambulla',
                'Habarana',
                'Trincomalee',
            ],
            'A7': ['Avissawella', 'Nuwara-Eliya'],
            'A8': ['Panadura', 'Ratnapura'],
            'A9': [
                'Kandy',
                'Dambulla',
                'Maradankadawala',
                'Mihintale',
                'Medawachchiya',
                'Vavuniya',
                'Mankulam',
                'Parantan',
                'Jaffna',
            ],
            'A10': ['Kandy', 'Kurunegala', 'Padeniya', 'Puttalam'],
            'A11': ['Maradankadawala', 'Habarana', 'Kalkudah'],
            'A12': [
                'Puttalam',
                'Anuradhapura',
                'Mihintale',
                'Horowupotana',
                'Trincomalee',
            ],
            'A13': ['Anuradhapura', 'Galkulama'],
            'A14': ['Medawachchiya', 'Paraiyanalankulam', 'Mannar'],
            'A15': ['Batticaloa', 'Kalkudah', 'Trincomalee'],
            'A16': ['Beragala', 'Kumbalwela', 'Hali-Ela'],
            'A17': ['Madampe', 'Akuressa', 'Galle'],
            'A18': ['Pelmadulla', 'Madampe', 'Nonagama'],
            'A19': ['Kegalle', 'Polgahawela'],
            'A20': ['Anuradhapura', 'Rambewa'],
            'A21': ['Kegalle', 'Karawanella'],
            'A22': ['Passara', 'Moneragala'],
            'A23': ['Wellawaya', 'Kumbalwela'],
            'A24': ['Akuressa', 'Matara'],
            'A25': ['Siyambalanduwa', 'Ampara'],
            'A26': ['Kandy', 'Padiyathalawa'],
            'A27': ['Ampara', 'Maha Oya'],
            'A28': ['Anuradhapura', 'Padeniya'],
            'A29': ['Vavuniya', 'Horowupotana'],
            'A30': ['Vavuniya', 'Paraiyanalankulam'],
            'A31': ['Ampara', 'Karaitivu'],
            'A32': ['Mannar', 'Jaffna'],
            'A33': ['Ja-Ela', 'Yakkala'],
            'A34': ['Mankulam', 'Mullaitivu'],
            'A35': ['Parantan', 'Mullaitivu'],
        }
        return Map(places, roads)


if __name__ == '__main__':
    m = Map.create_example1()
    m.validate()
    print(m)
