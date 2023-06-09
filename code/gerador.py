from util import Util
from menu import Colors
from menu import Menu

class GeradorCsv:
  
  def __init__(self):
    self.util = Util()
    self.menu = Menu()
    self.data = ['']
    self.label = ''
    self.file = open("data_base.csv", "w")


  def main(self):
    self.menu.reset()
    self.label = self.util.get_label()
    self.menu.reset()
    self.label = self.label + self.util.get_years()
    self.menu.main_menu()
    self.data.append(self.label)
    self.input_data()
  
  def input_data(self):
    op = int(input())

    if op == 1:
      self.menu.reset()
      self.data.append(self.util.get_counter())
      self.set_file(self.data)
      self.close_file()
    
    if op == 2:
      print("para valores")
    
  def set_file(self, data):
    with open("data_base.csv", "w") as file:
        file.writelines(data)

    self.menu.reset()

  def close_file(self):
    self.menu.reset
    print(Colors.GREEN + "    Arquivo data_base.csv criado com sucesso! " + Colors.RESET)
    self.file.close()

gerador = GeradorCsv()
gerador.main()
