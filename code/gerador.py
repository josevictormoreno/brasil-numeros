from util import Util
from menu import Colors
from menu import Menu

class GeradorCsv:
  util = Util()
  menu = Menu()

  def start(self):
    self.menu.reset()
    self.menu.main_menu()
    self.input_data()
  
  def input_data(self):
    op = int(input())

    if op == 1:
      self.menu.reset()
      self.util.get_years()

    elif op == 0:
      return
    
  def set_file(self):
    print("gerar arquivo com saida csv")
    
gerador = GeradorCsv()
gerador.start()
