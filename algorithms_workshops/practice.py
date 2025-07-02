import functools

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
async_session_maker = async_sessionmaker(engine, class_=AsyncSession)


async def get_async_session():
    async with async_session_maker() as session:
        yield session
