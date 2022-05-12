import math

class City(object) :

    position = {}
    connection = {}

    def __init__(self,name,g,parent=None):
        self.name = name
        self.parent = parent
        self.g = g
        self.f = None

    def __str__(self):
        return str(self.name)

    def __eq__(self, other):
        return self.name == other

    def __hash__(self):
        return str(self).__hash__()

    def __repr__(self):
        return str(self)

    def legal(self):
        return True

    def final(self, destination):
        return self.name == destination

    def h0(self, final_values):
        return 0

    def h1(self, final_values):
        return math.fabs(int(self.position[final_values][0]) - int(self.position[self.name][0]))

    def h2(self, final_values):
        return math.fabs(int(self.position[final_values][1]) - int(self.position[self.name][1]))

    def h3(self, final_values):
        return math.sqrt(self.h1(final_values)*self.h1(final_values) + self.h2(final_values)*self.h2(final_values))

    def h4(self, final_values):
        return self.h1(final_values) + self.h2(final_values)

    h = {
        1 : h0,
        2 : h1,
        3 : h2,
        4 : h3,
        5 : h4,
    }

    def applicable_operators(self):
        ops = []
        for cle,valeur in City.connection[self.name].items() :
            ops.append((cle,valeur))
        return ops

    def apply(self, op):
        return City(op[0],int(op[1]) + self.g, self)

    def distance(self, final_values,methode):
        self.f = self.h[methode](self, final_values) + self.g
        return self.f

    @staticmethod
    def parsePosition():
        with open("positions.txt", "r") as fichier:
            for line in fichier :
                data = line.split()
                City.position[data[0]] = (data[1],data[2])


    @staticmethod
    def parseConnection():
        with open("connections.txt", "r") as fichier:
            for line in fichier :
                data = line.split()
                if not data[0]in City.connection :
                    City.connection[data[0]] = {data[1] : data[2]}
                else :
                    City.connection[data[0]].update({data[1] : data[2]})

                if not data[1]in City.connection :
                    City.connection[data[1]] = {data[0] : data[2]}
                else :
                    City.connection[data[1]].update({data[0] : data[2]})


City.parsePosition()
City.parseConnection()
print(City.position)
print(City.connection)