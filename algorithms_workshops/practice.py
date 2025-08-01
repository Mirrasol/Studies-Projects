import functools
from abc import ABC, abstractmethod

#1.
class MyIterator:
    def __init__(self, initial):
        self.number = initial
    
    def __iter__(self):
        return self

    def __next__(self):
        if self.number < 0:
            raise StopIteration
        value = self.number
        self.number -= 1
        return value

#2.
def my_deco(func):
    @functools.wraps(func)
    def inner(*args, **kwargs):
        return func(*args, **kwargs)
    return inner

#3.
# async_session_maker = async_sessionmaker(engine, class_=AsyncSession)


# async def get_async_session():
#     async with async_session_maker() as session:
#         yield session


class Base(ABC):
    @abstractmethod
    def get_info(self):
        pass


class Animal(Base):
    def __init__(self, name, color):
        self.name = name
        self.color = color
    
    def get_info(self):
        return f'{self.name}\'s color is {self.color}'


class BirdAnimal(Animal):
    def __init__(self, name, color, plumage):
        super().__init__(name, color)
        self.plumage = plumage


bird = BirdAnimal('Pete', 'black', 'long-feathered')
# print(bird.get_info())


coll = [str(i) for i 
        in range(0, 5)]
print(coll)


# updating for testing purposes