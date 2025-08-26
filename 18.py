class Resourse:
    def __init__(self):
        self.f = open('data.txt', 'w')
        self.f.write('Hello, world!')
        print('resourse is created')


    def __del__(self):
        self.f.close()
        print('resourse is deleted')
            
my = Resourse()