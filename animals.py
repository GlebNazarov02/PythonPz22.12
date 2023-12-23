import logging
import argparse

class Animal:
    def __init__(self, name):
        self.name = name

class Bird(Animal):
    def __init__(self, name, wingspan):
        super().__init__(name)
        self.wingspan = wingspan

    def wing_length(self):
        return self.wingspan / 2

class Fish(Animal):
    def __init__(self, name, max_depth):
        super().__init__(name)
        self.max_depth = max_depth

    def depth(self):
        if self.max_depth < 10:
            return 'Мелководная рыба'
        elif self.max_depth > 100:
            return 'Глубоководная рыба'
        return 'Средневодная рыба'

class Mammal(Animal):
    def __init__(self, name, weight):
        super().__init__(name)
        self.weight = weight

    def category(self):
        if self.weight < 1:
            return 'Малявка'
        elif self.weight > 200:
            return 'Гигант'
        return 'Обычный'

class AnimalFactory:
    @staticmethod
    def create_animal(animal_type, *args):
        if animal_type == 'Bird':
            return Bird(*args)
        elif animal_type == 'Fish':
            return Fish(*args)
        elif animal_type == 'Mammal':
            return Mammal(*args)
        else:
            raise ValueError('Недопустимый тип животного')
        
logging.basicConfig(filename='animallog', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def main():
    parser = argparse.ArgumentParser(description='AnimalInfo')
    parser.add_argument('type',type = str, help='AnimalType')
    parser.add_argument('name',type = str, help='AnimalName')
    parser.add_argument('par',type = int, help='AnimalPar')
    args = parser.parse_args()
    try:
        if args.type == 'Bird':
            animal1 = AnimalFactory.create_animal("Bird", args.name, args.par)
            logging.info('Animal Bird created Successfully')
        elif args.type == 'Fish':
            animal1 = AnimalFactory.create_animal("Fish", args.name, args.par)
            logging.info('Animal Fish created Successfully')
        elif args.type == 'Mammal':
            animal1 = AnimalFactory.create_animal("Mammal", args.name, args.par)
            logging.info('Animal Mammal created Successfully')
        else:
            logging.error('Incorrect data')
    except ValueError as e:
    # Логируем ошибку при создании животного
        logging.error('Incorrect data')

if __name__ == '__main__':
    main()
