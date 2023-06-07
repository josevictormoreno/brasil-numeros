from util import Util

class Menu:
  util = Util()

  def reset(self):
    self.util.clear()
    print(Colors.BLUE + '-_-*-_-*-_-*-_-_-*-_-*-_-*-_' + Colors.GREEN + ' Gerador CSV ' + Colors.BLUE +'-_-*-_-*-_-*-_-_-*-_-*-_-*-_' + Colors.RESET)

  def main_menu(self):
    self.reset()
    print(Colors.BLUE + "-" + Colors.RESET)
    print(Colors.BLUE + "-" + Colors.RESET + "    " + Colors.GREEN + "1-" + Colors.RESET + " Gerar anos")
    print(Colors.BLUE + "-" + Colors.RESET + "    " + Colors.GREEN + "2-" + Colors.RESET + " Gerar contador")
    print(Colors.BLUE + "-" + Colors.RESET + "    " + Colors.GREEN + "3-" + Colors.RESET + " Gerar arquivo")
    print(Colors.BLUE + "-" + Colors.RESET + "    " + Colors.GREEN + "0-" + Colors.RESET + " Sair")

class Colors:  
  RED = "\033[1;31m"  
  BLUE = "\033[1;34m"
  CYAN = "\033[1;36m"
  GREEN = "\033[0;32m"
  RESET = "\033[0;0m"
  BOLD = "\033[;1m"
  REVERSE = "\033[;7m"

menu = Menu()
menu.reset()