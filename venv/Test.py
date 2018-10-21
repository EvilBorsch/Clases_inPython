import csv

class CarBase:
    def __init__(self, brand, photo_file_name, carrying):
        self.brand = brand
        self.photo_file_name = photo_file_name
        self.carrying = carrying
    def get_photo_file_ext(self):
        return self.photo_file_name.split(".")[-1]


class Car(CarBase):
    def __init__(self, brand, photo_file_name, carrying, passenger_seats_count):
        super().__init__(brand, photo_file_name, carrying)
        self.car_type = "car"
        self.passenger_seats_count = passenger_seats_count


class Truck(CarBase):
    def __init__(self, brand, photo_file_name, carrying, body_whl):
        super().__init__(brand, photo_file_name, carrying)
        self.car_type = "truck"
        paramenters = body_whl.split("x")
        if paramenters == [""]:
            self.body_width = self.body_height = self.body_length = 0
        else:
            self.body_width = float(paramenters[0])
            self.body_height = float(paramenters[1])
            self.body_length = float(paramenters[2])

    def get_body_volume(self):
        return self.body_width * self.body_height * self.body_length


class SpecMachine(CarBase):
    def __init__(self, brand, photo_file_name, carrying, extra):
        super().__init__(brand, photo_file_name, carrying)
        self.car_type = "spec_machine"
        self.extra = extra


def get_car_list(csv_filename):
    car_list = []
    with open(csv_filename) as csv_fd:
        reader = csv.reader(csv_fd, delimiter=';')
        next(reader)  # пропускаем заголовок
        for row in reader:
            if len(row) == 7 and row[1] != "" and row[3] != "" and row[5] != "":
                if row[0] == "car":
                    if row[2] != "":
                        car_list.append(Car(row[1], row[3], float(row[5]), int(row[2])))
                elif row[0] == "truck":
                    car_list.append(Truck(row[1], row[3], float(row[5]), row[4]))
                else:
                    if row[6] != "":
                        car_list.append(SpecMachine(row[1], row[3], float(row[5]), row[6]))
    return car_list

