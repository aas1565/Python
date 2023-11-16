class Transport():
    def __init__(self, coordinates, speed, brand, year, number):
        self._coordinates = coordinates
        self._speed = speed
        self._brand = brand
        self._year = year
        self._number = number

    def __str__(self):
        '''
           Представление всей информации для вывода в методе print()
        '''
        return f"Transport:{self._brand} {self._year} {self._number}"

    def isInArea(self, pos_x, pos_y, length, width) -> bool:
        '''
        Присутствие транспортного средства в пределах заданнй области
        pos_x, pos_y - координата левого верхнего угла области
        length, width - длина и ширина области
        '''
        x,y = self._coordinates
        if pos_x <=x <=pos_x+length and pos_y<=y <= pos_y+width:
            return True
        else:
            return False

    @property
    def coordinates(self):
        return self._coordinates
    @coordinates.setter
    def coordinates(self, coordinates):
        self._coordinates=coordinates

    @property
    def speed(self):
        return self._speed
    @speed.setter
    def speed(self, speed):
        self._speed=speed

    @property
    def brand(self):
        return self._brand
    @brand.setter
    def brand(self, brand):
        self._brand=brand

    @property
    def year(self):
        return self._year
    @year.setter
    def year(self, year):
        self._year=year

    @property
    def number(self):
        return self._number
    @number.setter
    def number(self, number):
        self._number=number


class Passenger():
    def __init__(self):
        self._passengers_capacity=None
        self._number_of_passengers=None
    @property
    def passengers_capacity(self):
        return self._passengers_capacity

    @passengers_capacity.setter
    def passengers_capacity(self, passengers_capacity):
        self._passengers_capacity=passengers_capacity

    @property
    def number_of_passengers(self):
        return self._number_of_passengers

    @number_of_passengers.setter
    def number_of_passengers(self, number_of_passengers):
        self._number_of_passengers=number_of_passengers


class Cargo():
    def __init__(self):
        self._carrying=None
    @property
    def carrying(self):
        return self._carrying

    @carrying.setter
    def carrying(self, carrying):
        self._carrying=carrying


class Plane(Transport):
    def __init__(self, coordinates, speed, brand, year, number, height):
        super().__init__(coordinates, speed, brand, year, number)
        self._height = height
    @property
    def height(self):
        return self._height
    @height.setter
    def height(self, height):
        self._height=height

class Auto(Transport):
    def __init__(self, coordinates, speed, brand, year, number):
        super().__init__(coordinates, speed, brand, year, number)


class Ship(Transport):
    def __init__(self, name, coordinates, speed, brand, year, number, port):
        super().__init__(coordinates, speed, brand, year, number)
        self._port = port
        self._name=name

    @property
    def port(self):
        return self._port
    @port.setter
    def port(self, port):
        self._port=port

    @property
    def name(self):
        return self._name
    @name.setter
    def name(self, name):
        self._name=name

class Car(Auto):
    def __init__(self, coordinates, speed, brand, year, number, model):
        super().__init__(coordinates, speed, brand, year, number)
        self._model=model

    @property
    def model(self):
        return self._model
    @model.setter
    def model(self, model):
        self._model=model


class Bus(Auto, Passenger):
    def __init__(self, coordinates, speed, brand, year, number, passengers_capacity, number_of_passengers):
        super().__init__(coordinates, speed, brand, year, number)
        self._passengers_capacity=passengers_capacity
        self._number_of_passengers=number_of_passengers
    @property
    def passengers_capacity(self):
        return self._passengers_capacity
    @passengers_capacity.setter
    def passengers_capacity(self, passengers_capacity):
        self._passengers_capacity=passengers_capacity

    @property
    def number_of_passengers(self):
        return self._number_of_passengers
    @number_of_passengers.setter
    def number_of_passengers(self, number_of_passengers):
        self._number_of_passengers=number_of_passengers

class CargoAuto(Auto, Cargo):
    def __init__(self, coordinates, speed, brand, year, number, carrying):
        super().__init__(coordinates, speed, brand, year, number)
        self._carrying=carrying
    @property
    def carrying(self):
        return self._carrying
    @carrying.setter
    def carrying(self, carrying):
        self._carrying=carrying

class Boat(Ship):
    def __init__(self, coordinates, speed, brand, year, number, port, name):
        super().__init__(coordinates, speed, brand, year, number, port, number)
        self._port=port
        self._name=name

    @property
    def port(self):
        return self._port
    @port.setter
    def port(self, port):
        self._port=port

    @property
    def name(self):
        return self._name
    @name.setter
    def name(self, name):
        self._name=name

class PassengerShip(Ship, Passenger):
    def __init__(self, coordinates, speed, brand, year, number, port, name, passengers_capacity, number_of_passengers):
        super().__init__(coordinates, speed, brand, year, number, name, port)
        self._name=name
        self.port=port
        self.passengers_capacity=passengers_capacity
        self.number_of_passengers=number_of_passengers

    @property
    def port(self):
        return self._port

    @port.setter
    def port(self, port):
        self._port = port

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name

    @property
    def passengers_capacity(self):
        return self._passengers_capacity

    @passengers_capacity.setter
    def passengers_capacity(self, passengers_capacity):
        self._passengers_capacity = passengers_capacity

    @property
    def number_of_passengers(self):
        return self._number_of_passengers

    @number_of_passengers.setter
    def number_of_passengers(self, number_of_passengers):
        self._number_of_passengers = number_of_passengers


class CargoShip(Ship, Cargo):
    def __init__(self, coordinates, speed, brand, year, number, port, name, carrying):
        super().__init__(coordinates, speed, brand, year, name, number, port)
        self._port=port
        self._name=name
        self._carrying=carrying

    @property
    def port(self):
        return self._port

    @port.setter
    def port(self, port):
        self._port = port

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name

    @property
    def carrying(self):
        return self._carrying

    @carrying.setter
    def carrying(self, carrying):
        self._carrying = carrying


plane=Plane((10,20), 500, "Boeing", 2000, "abc12", 10000)
plane.height=20000
auto=Auto((30,40), 100, "auto", 2010, 'FHFJD')
ship=Ship("titanic", (10,20), 50, "ocean", 1990, "def123", "moscow")
ship.name="titan"
car=Car((20, 30), 100, "audi", 2023, "aas", "audi-q8")
bus= Bus((30,40), 70, "lexus", 2004, "asde21", 40, 30)
cargoAuto=CargoAuto((50,100), 80, "volf", 1990, "awq12", "yes")
boat=Boat((10,30), 120, "arena", 2150, "awq12", "royal", "art")
passengerShip=PassengerShip((60,80), 60, "luxe", 2009, "aqw123", "paris", "beda", 100, 99)
cargoShip=CargoShip((100,200), 100, "aut", 1999, "tr56", "russia", "qw","no")

area=ship.isInArea(0,0,50,50)
print(area)

print(plane)
print(ship)
print(auto)
print(car)
print(bus)
print(cargoAuto)
print(boat)
print(passengerShip)
print(cargoShip)