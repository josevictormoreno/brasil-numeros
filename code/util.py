import os

class Util:
  
  def clear(self):
    if os.name == 'posix':
      os.system('clear')
    elif os.name == 'nt':
      os.system('cls')

  def get_years(self):
    first_year = int(input("Informe o ano inicial: "))
    last_year = int(input("Informe o ano final: "))
    result = ''
    for x in range(first_year, last_year):
        result = result + str(x) + ','

    result = result + str(last_year) + "\n"
    return result

  def get_counter(self):
    years_str = str(input("Informe o array de anos: "))
    years_list = years_str.split(",")
    years_list = [int(year.strip()) for year in years_list]
    print(years_list)

  def get_label(self):
    labels_str = str(input("Informe os labels: "))
    labels_str = labels_str + ','
    return labels_str
