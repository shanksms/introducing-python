class Duck:
    def __init__(self, input_name):
        self.hidden_name = input_name

    @property
    def name(self):
        print('inside getter')
        return self.hidden_name
    @name.setter
    def name(self, input_name):
        print('inside setter')
        self.hidden_name = input_name


if __name__ == '__main__':
    fowl = Duck('Howard')
    print(fowl.name)
    fowl.name = 'George'
    print(fowl.name)