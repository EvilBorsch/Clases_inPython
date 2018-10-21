import csv
import os
import csv
import operator


class CarBase:
    def __init__(self, brand, photo_file_name, carrying):

        def get_photo_file_ext(photo_file_name):
            try:
                temp = photo_file_name.split('.')[1]
            except IndexError:
                return ""
            else:
                return ('.' + temp)

        self.brand = brand
        self.photo_file_name = get_photo_file_ext(photo_file_name)
        self.carrying = carrying


class Car(CarBase):
    def __init__(self, brand, photo_file_name, carrying, passenger_seats_count):
        super().__init__(brand, photo_file_name, carrying)
        self.passenger_seats_count = passenger_seats_count

    def __repr__(self):
        return (f" Car Brand:{self.brand};" + f" Car photo_file_name:{self.photo_file_name};"
                + f" Carrying:{self.carrying};" + f" Passenger seats count:{self.passenger_seats_count}")


class Truck(CarBase):

    def __init__(self, brand, photo_file_name, carrying, body_whl):
        super().__init__(brand, photo_file_name, carrying)
        self.body_whl = body_whl

    def get_body_volume(self):
        if self == "":
            return 0
        temp = self.body_whl.split('x')
        try:
            return (float(temp[0]) * float(temp[1]) * float(temp[2]))
        except (TypeError, ValueError):
            print("WRONG TRUCK RAZMER")
            return ""
        else:
            return (float(temp[0]) * float(temp[1]) * float(temp[2]))

    def __repr__(self):
        return (f" TRUCK Brand:{self.brand};" + f" Truck photo_file_name:{self.photo_file_name};"
                + f" Carrying:{self.carrying};" + f" Body_whl:{self.body_whl}")


class SpecMachine(CarBase):
    def __init__(self, brand, photo_file_name, carrying, extra):
        super().__init__(brand, photo_file_name, carrying)
        self.extra = extra

    def __repr__(self):
        return (f" SPECIAL Brand:{self.brand};" + f" special photo_file_name:{self.photo_file_name};"
                + f" Carrying:{self.carrying};" + f" EXTRA:{self.extra}")


def get_car_list(csv_filename):
    car_list = []
    with open(csv_filename) as csv_fd:
        reader = csv.reader(csv_fd, delimiter=';')
        next(reader)  # пропускаем заголовок
        for row in reader:

            if not '.' in row[3]:
                continue

            if row[0] == "car":
                try:
                    car = Car(row[1], row[3], float(row[5]), int(row[2]))
                    car_list.append(car)
                except(ValueError):
                    print("Неправильное значение carrying")
                    continue

            elif row[0] == "truck":
                temp = row[4].split('x')
                flag = 0
                for i in temp:
                    try:
                        float(i)
                    except(ValueError):
                        flag = 1
                        break
                try:
                    if flag == 1:
                        flag = 0
                        continue
                    truck = Truck(row[1], row[3], float(row[5]), row[4])
                    car_list.append(truck)
                except(ValueError):
                    print("Неправильное значение carrying")
                    continue

            elif row[0] == "spec_machine":
                try:
                    special = SpecMachine(row[1], row[3], float(row[5]), row[6])
                    car_list.append(special)
                except(ValueError):
                    continue
            else:
                print("В первой калонке для этой строки не заполнен тип тачилы")
                continue
    return car_list

csv_filename = "C:\\PythonFiles\\coursera.csv"
try:
    car_list = (get_car_list(csv_filename))
except:
    print("Такого файла не существует")
else:
    print(car_list)
