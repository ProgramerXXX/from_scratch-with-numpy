
import numpy as np 

class One_Hot():
  def __init__(self):
    super().__init__()
    self.labels = []

  def Create_OneHot(self,x):
    #input string 
    str_input = x 
    for i in range(len(str_input)):
      #create np.array unique value 
      if  str_input[i] not in self.labels:
        self.labels.append(str_input[i]) 

    #create one_hot with array unique and array input string 
    One_hot = np.zeros((len(str_input),len(self.labels)))
    for i in range(len(str_input)):
      One_hot[i][self.labels.index(str_input[i])] = 1
    
    return One_hot

  def Convert_OneHot(self,one_hot):
    #check index in one_hot for return index value from convert to string 
    result = np.where(one_hot == 1)
    Str = ''
    for i in range(len(result[1])):
      Str = Str + self.labels[result[1][i]]
    return Str

if __name__ == '__main__':
  model = One_Hot()
  inputs = '(o’’)o<3'
  x = model.Create_OneHot(inputs)
  print('One_Hot Encoding')
  print(x)
  y = model.Convert_OneHot(x)
  print(f'Convert to string  {y}')