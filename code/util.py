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
    name = str(input("Informe o nome: "))
    years_str = str(input("Informe o array de anos: "))
    years_list = years_str.split(",")
    years_list = [int(year.strip()) for year in years_list]
    counter = 0
    data = ''
    for i in range(years_list[0], years_list[-1] + 1):
      result = 0
      if counter == len(years_list):
        return data
      elif years_list[counter] == i:
        result = result + 1
        name = name + str(result) + ','
        print('aumentou')
      else:
        name = name + str(result) + ','
      counter = counter + 1
      print(counter)
    data = name + ',' + str(result)
    return data

  def get_label(self):
    labels_str = str(input("Informe os labels: "))
    labels_str = labels_str + ','
    return labels_str
