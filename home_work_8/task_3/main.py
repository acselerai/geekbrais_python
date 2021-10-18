class FillListWithDigits():
    STOP = 'stop'

    def __init__(self):
        self.__result_list = []

    def call(self):
        self.__print_help()
        while True:
            read_input = self.__read_input()
            if read_input == self.STOP:
                break
            else:
                if read_input.isdigit():
                    self.__result_list.append(int(read_input))
                else:
                    print(f'{read_input} is not a number')
        print(self.__result_list)

    def __print_help(self):
        print('Type "stop" to exit')
        print('Enter the number:')

    def __read_input(self):
        return input()


FillListWithDigits().call()
