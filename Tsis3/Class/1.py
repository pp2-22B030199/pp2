class String():
    def GetString(self):
        n = input()
        return n


    def PrintString(self):

        print(self.GetString().upper())

s = String()
s.PrintString()