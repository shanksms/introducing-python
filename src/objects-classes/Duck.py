class Duck:
    def __init__(self, input_name):
        self.__name = input_name

    @property
    def name(self):
        print('inside getter')
        return self.__name
    @name.setter
    def name(self, input_name):
        print('inside setter')
        self.__name = input_name


if __name__ == '__main__':
    fowl = Duck('Howard')
    print(fowl.name)
    fowl.name = 'George'
    print(fowl.name)