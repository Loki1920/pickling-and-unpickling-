#pickling and unpickling 
import pickle
class Student:
  def __init__(self,name,roll,address):
    self.name = name
    self.roll = roll
    self.address = address
  def disp(self):
    print(f'Name:{self.name} Roll:{self.roll} Address:{self.address}')

with open("student.dat",'wb') as f:
  Stu1 = Student('Rahul',101,'Ranchi')
  pickle.dump(Stu1,f)
  print("pickling done!")

#unpickling
with open("student.dat",'rb') as f:
  obj = pickle.load(f)
  print("upickling done!")
  obj.disp()
  
    