import csv

class Car:
    all_cars = []
    def __init__(self, make: str, model: str, year: int, color:str, value=0):
        self.make = make
        self.model = model
        self.year = year
        self.color = color
        self.value = value

        Car.all_cars.append(self)

    @staticmethod
    def smog_test_failed(year):
        '''Returns True if car year is older than 2016'''
        if year < 2016:
            return True

    def expensive(self):
        if self.value > 50000:
            return True

    @classmethod
    def instantiate_from_csv(cls):
        with open('Cars.csv', 'r') as f:
            reader = csv.DictReader(f)
            items = list(reader)

        for item in items:
            print(item)
            Car(
                make = item.get("Make"),
                model = item.get("Model"),
                year = item.get("Year"),
                color = item.get("Color")
            )

    def __repr__(self):
        return f"Car({self.make},{self.model},{self.year},{self.color})"

def main():
    return Car.instantiate_from_csv()

if __name__ == "__main__":
    main()

