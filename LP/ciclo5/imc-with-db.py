from datetime import date
from PySimpleGUI import PySimpleGUI as sg
import sqlite3

connection = sqlite3.connect('imc.db')
cursor = connection.cursor()

cursor.execute(
    """Create table if not exists imc (id integer not null primary key autoincrement, name varchar(100),  weight real, height real, imc real, date text, result varchar(100))""")

sg.theme('BrownBlue')

layout = [[sg.Text('Nome do Paciente'), sg.Input(key='name', size=(40, 1))],
          [sg.Text('Endereço Completo'), sg.Input(
              key='address', size=(39, 1))],
          [sg.Column([[sg.Text('Altura (cm)'), sg.Input(key='height', size=(20, 1))],
                      [sg.Text('Peso (Kg)'), sg.Input(key='weight', size=(20, 1))]]),
           sg.Column([[sg.Text('', key='result', text_color='red')]])],
          [sg.Button('Calcular'), sg.Button('Reiniciar'), sg.Button('Resultados'), sg.Button('Sair')]]

janela = sg.Window('Cálculo do IMC - Indice de Massa Corporal',
                   layout, location=(800, 400))


def calc_imc(weight, height):
    return round(weight / (height ** 2), 2)


while True:
    event, values = janela.read()
    if event == sg.WINDOW_CLOSED:
        break

    if event == 'Calcular':

        if values['height'] == '' or values['weight'] == '':
            sg.popup('Preencha todos os campos!')
            continue

        imc = calc_imc(float(values['weight']), (float(values['height'])/100))

        if imc < 17:
            sg.Window.find_element(janela, 'result').update(
                'IMC: {:.2f}\nVocê esta muito abaixo do peso'.format(imc))
        elif (imc >= 17) and (imc <= 18.49):
            sg.Window.find_element(janela, 'result').update(
                'IMC: {:.2f}\nVocê esta abaixo do peso'.format(imc))
        elif (imc >= 18.50) and (imc <= 24.99):
            sg.Window.find_element(janela, 'result').update(
                'IMC: {:.2f}\nPeso normal'.format(imc))
        elif (imc >= 25) and (imc <= 29.99):
            sg.Window.find_element(janela, 'result').update(
                'IMC: {:.2f}\nAcima do peso'.format(imc))
        elif (imc >= 30) and (imc <= 34.99):
            sg.Window.find_element(janela, 'result').update(
                'MMC: {:.2f}\nObesidade I'.format(imc))
        elif (imc >= 35) and (imc <= 39.99):
            sg.Window.find_element(janela, 'result').update(
                'MMC: {:.2f}\nObesidade II (severa)'.format(imc))
        else:
            sg.Window.find_element(janela, 'result').update(
                'IMC: {}\nObesidade III (mórbida)'.format(imc))

        cursor.execute("""insert into imc (name, weight, height, imc, date, result) values (?, ?, ?, ?, ?, ?)""",
                       (values['name'], values['weight'], values['height'], imc, str(date.today()), sg.Window.find_element(janela, 'result').Get().split('\n')[1]))
        connection.commit()

    if event == 'Reiniciar':
        sg.Window.find_element(janela, 'name').update('')
        sg.Window.find_element(janela, 'address').update('')
        sg.Window.find_element(janela, 'height').update('')
        sg.Window.find_element(janela, 'weight').update('')
        sg.Window.find_element(janela, 'result').update('')

    if event == 'Resultados':
        result = cursor.execute(
            """select * from imc order by id asc""").fetchall()
        if len(result) == 0:
            sg.popup('Não há resultados cadastrados!')
            continue

        sg.popup_scrolled(
            'Nome\t\tPeso\t\tAltura\t\tIMC\t\tData\t\tResultado\n' + '-'*200 + '\n' + '\n'.join(['{}\t\t{}\t\t{}\t\t{}\t\t{}\t\t{}'.format(
                i[1], i[2], i[3], i[4], i[5], i[6]) for i in result]), title='Resultados', font='Any 12', size=(800, 600), location=(0, 0))
        continue

    if event == 'Sair':
        break
