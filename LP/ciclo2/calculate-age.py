from datetime import date
import re

patern = re.compile(r'\d{2}/\d{2}/\d{4}')

currentDate = date.today()

while (True):
    birthDateString = input('Digite sua data de nascimento (dd/mm/yyyy): ')
    if (patern.match(birthDateString)):
        birthYear = int(birthDateString[6:])
        if (birthYear < 0):
          print('Ano inválido')
          continue
        birthMonth = int(birthDateString[3:5])
        if (birthMonth < 0 or birthMonth > 12):
          print('Mês inválido')
          continue
        birthDay = int(birthDateString[0:2])
        if (birthDay < 0 or birthDay > 31):
          print('Dia inválido')
          continue
        birthDate = date(birthYear, birthMonth, birthDay)
        if (birthDate > currentDate):
            print('Você ainda não nasceu!')
        else:
          ages = currentDate.year - birthDate.year
          months = currentDate.month - birthDate.month
          days = currentDate.day - birthDate.day
          if (days < 0):
              months -= 1
              days += 30
          if (months < 0):
              ages -= 1
              months += 12
          print('Você tem {} anos, {} meses e {} dias de idade.'.format(ages, months, days))
          break
    else:
        print('Formato inválido!')
        continue