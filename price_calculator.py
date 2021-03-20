import os
import PySimpleGUI as sg
from PySimpleGUI.PySimpleGUI import ColorChooserButton, Window, popup, theme_button_color
sg.theme('Darkblue13')
# layout
layout = [
    [sg.Text('Qual o valor da compra?')],
    [sg.Text('R$'), sg.Input(size=(10, 1), default_text=0.0)],
    [sg.Text('Forma de pagamento')],
    [sg.Combo(['Dinheiro', 'Cartão de crédito'], default_value='Dinheiro')],
    [sg.Text('Ignorar o campo abaixo caso forma de pagameto seja dinheiro.')],
    [sg.Text('Parcelas (até 12X)'), sg.Slider(range=(1, 12),
    default_value=1,
    size=(20, 10),
    orientation='horizontal')],
    [sg.Button('Calcular', size=(10,1)), sg.Button('Sair', button_color='red')],
    [sg.Output(size=(55,6), background_color='black', text_color='white', key='output')]
]
# janela
janela = sg.Window('Compras').layout(layout)
# Extrair os dados da tela
while True:
    eventos, valores = janela.read()
    if eventos == sg.WIN_CLOSED or eventos == 'Sair':
        break
    #definir variaveis para o Output
    preço = float(valores[0])
    parcelas = int(valores[2])
    formpagamento = valores[1]
    desconto_ou_juros = ' '
    if formpagamento == 'Dinheiro':
        parcelasnome = 'Avista'
        desconto_ou_juros = ('Desconto de 10%.')
        total = preço - (preço/100)*10
    elif formpagamento == 'Cartão de crédito':
        parcelasnome = (f'em {parcelas}X')
        if parcelas == 1:
            desconto_ou_juros = ('Desconto de 5%.')
            total = preço - (preço/100)*5
        elif parcelas == 2:
            desconto_ou_juros = ('Preço Normal')
            total = preço
        else:
            desconto_ou_juros = ('20% de juros')
            total = preço + (preço/100)*20
    #OUTPUT
    if eventos == 'Calcular':
        janela.FindElement('output').Update('')
        if preço == 0:
            print('INSIRA UM VALOR PARA CONTINUAR!')
        else:
            print(f'• preço original é R${preço}')
            print(f'• A forma de pagamento escolhida foi {formpagamento}, {parcelasnome}')
            print(f'• {desconto_ou_juros}')
            if formpagamento == 'Cartão de crédito' and parcelas > 1:
                print(f'• {parcelas} parcelas de R${total/parcelas}')
            print(f'• O total a ser pago é R${total}')
janela
