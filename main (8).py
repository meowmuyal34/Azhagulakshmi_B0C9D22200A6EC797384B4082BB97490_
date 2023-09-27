class Student:
  def __init__(self):
    self.__name=''
  def setname(self, name):
    print('setname() called')
    self.__name=name
  def getname(self):
    print('getname() called')
    return self.__name
  name=property(getname, setname)

#create object  
std = Student()
std.name="Steve" #calls setname()
print(std.name)  #calls getname()