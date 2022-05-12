# Name: Van Hao On
# CECS 451 Section 01
# Assignment#1

import sys
from queue import PriorityQueue
from math import sin, cos, asin, radians, sqrt
import re


class City:
    map = {}
    coordinates = {}

    # Parse the data from "coordinates.txt" into a list
    @staticmethod
    def parseCoordinates():
        with open("coordinates.txt", "r") as c:
            for line in c:
                data = re.split(r'[ ,:\(\)]+', line)
                City.coordinates[data[0]] = (float(data[1]), float(data[2]))

    # Parse the data from "map.txt" into a list
    @staticmethod
    def parseMap():
        with open("map.txt", "r") as m:
            for line in m:
                data = re.split(r'[ ,:\(\)-]+', line)
                City.map[data[0]] = {}
                for i in range(1, len(data) - 1, 2):
                    City.map[data[0]].update({data[i]: float(data[i + 1])})


# Calculate the straight line distance between two cities
def straight_line_distance(city1: str, city2: str):
    r = 3958.8
    lat1 = radians(City.coordinates[city1][0])
    lon1 = radians(City.coordinates[city1][1])
    lat2 = radians(City.coordinates[city2][0])
    lon2 = radians(City.coordinates[city2][1])

    dLat = lat2 - lat1
    dLon = lon2 - lon1

    a = (sin(dLat / 2) ** 2) + cos(lat1) * cos(lat2) * (sin(dLon / 2) ** 2)
    d = 2 * r * asin(sqrt(a))
    return d


# A* algorithm
def a_star_search(start, des):
    pq = PriorityQueue()
    pq.put((0.0, (start, start, 0)))
    history = {}
    visited = []
    res = []

    while not pq.empty():
        point = pq.get()
        connection = point[1]
        city = connection[0]
        prev = connection[1]
        res.append(connection)

        if city == des:
            break

        if city == start:
            path = 0
        else:
            path = history[prev].get(city)

        if city not in visited:
            history[city] = {}
            for i in City.map[city]:
                d = City.map[city].get(i)
                a = d + path
                history[city].update({i: a})
                pq.put(((a + straight_line_distance(i, des)), (i, city, a)))
        else:
            continue
        visited.append(city)
    return res

# Function that retrieves the correct path
def get_result(path):
    path_list = []
    final = path.pop()
    path_list.append(final[0])
    prev = final[1]
    distance = round(final[2] - City.map[prev].get(path_list[-1]), 2)

    for i in reversed(path):
        curr = i[0]
        curr_distance = i[2]
        if curr == prev and curr_distance == distance:
            path_list.append(curr)
            prev = i[1]
            if distance != 0:
                distance = round(distance - City.map[prev].get(path_list[-1]), 2)

    route = " - ".join(reversed(path_list))
    return final[2], route


if __name__ == '__main__':
    City.parseMap()
    City.parseCoordinates()
    depart = sys.argv[1]
    arrive = sys.argv[2]
    r = a_star_search(depart, arrive)
    total_distance, route = get_result(r)
    print("From city: ", depart)
    print("To city: ", arrive)
    print("Best Route: ", route)
    print("Total distance: %.2f mi" % total_distance)
