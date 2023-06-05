import util

class GeradorCsv:
  RED = "\033[1;31m"  
  BLUE = "\033[1;34m"
  CYAN = "\033[1;36m"
  GREEN = "\033[0;32m"
  RESET = "\033[0;0m"
  BOLD = "\033[;1m"
  REVERSE = "\033[;7m"

  def start(self):
    util.clear()
    print(self.BLUE + '-_-*-_-*-_-*-_-_-*-_-*-_-*-_' + self.GREEN + ' Gerador CSV ' +self.BLUE +'-_-*-_-*-_-*-_-_-*-_-*-_-*-_' + self.RESET)
    self.getYears()

  def getYears(self):
    firstYear = int(input("Informe o ano inicial: ")) 
    lastYear = int(input("Informe o ano final: ")) 
    result = ''
    for x in range(firstYear, lastYear):
      result = result + str(x) + ', '

    result = result + lastYear
    print(result)

gerador = GeradorCsv()
gerador.start()