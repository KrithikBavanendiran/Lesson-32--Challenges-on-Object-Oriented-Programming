class Integer:
    def __init__(self, num, Roman):
        self.num=num
        self.Roman= Roman

    
    def convert(self):
        for i in self.Roman:
            if self.num==i:
                print(self.Roman[i])

num=input("Enter a number")
Roman={'1':'I', '5':'V', '10':'X', '50':'L', '100':'C', '500':'D'}

obj= Integer(num, Roman)
obj.convert()
    