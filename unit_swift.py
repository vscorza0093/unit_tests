import pytest


user_in_x = 1
user_in_y = 1
user_in_z = 1

coordinates_list = []

class WordWraper():
    def __init__(self):



def get_coordinates():
    for coordX in range(0, user_in_x + 1):
        for coordY in range(0, user_in_y + 1):
            for coordZ in range(0, user_in_z + 1):
                temp_list = []
                temp_list.append(coordX)
                temp_list.append(coordY)
                temp_list.append(coordZ)
                coordinates_list.append(temp_list)
    return coordinates_list


def test_get_coordinates():
    assert get_coordinates() == [[coordX, coordY, coordZ]
                                 for coordX in range(user_in_x + 1)
                                 for coordY in range(user_in_y + 1)
                                 for coordZ in range(user_in_z + 1)
                                 ]

