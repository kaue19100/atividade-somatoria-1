print('bem vindo ao monitoramento de saúde com imc !!! ')
kg = int(input('quntos kg você pesa ?'))
altura = float(input('qual a sua altura atual ?'))
imc = kg / (altura ** 2)

if imc < 18.5:
    print(' ________________________________________________________________________')
    print(f'| seu imc é {imc:.2f}, ou seja, abaixo do peso segundo a (OMS).            |')
    print(' |O melhor a se fazer é ajustar a sua alimentação e praticar exercicios |')
    print(' |______________________________________________________________________|')
elif imc <= 24.9:
    print('_____________________________________________________________________________________|')
    print(f'| O seu imc é {imc:.2f}, ou seja, você pesa o tanto ideal pra sua altura segundo a (OMS)|')
    print(' | O risco de problemas relacionados ao peso (como desnutrição ou obesidade) é menor.|')
    print(' |___________________________________________________________________________________|')

elif imc <= 29.9:
    
    print('___________________________________________________________________')
    print(f'| seum imc é {imc:.2f} você tem sobrepeso segundo a (OMS).           | ')
    print(' |O risco de desenvolver problemas de saúde começa a aumentar     |')
    print(' |especialmente se houver outros fatores associados, como:        |')
    print(' |pressão alta; colesterol alto; pré diabetes e etc...            | ')
    print(' |procure um nutricionista e Reduza o consumo de ultraprocessados |')
    print(' |________________________________________________________________|')

elif imc <= 34.9:
    print(' _________________________________________________________________________')
    print(f'|seu imc é {imc:.2f}. segundo a (OMS) você considerado um obeso de grau 1   |')
    print(' | isso já almenta os seus riscos de pegar algumas doenças, como:        |')
    print(' | diabetes tipo 2; Hipertensão arterial; Dores nas articulações e etc...|')
    print(' | procure ajuda de especialistas e mude o seu estilo de vida.           |')
    print(' |_______________________________________________________________________|')
elif imc <= 39.9:
    print('________________________________________________________________________________________')
    print(f'|seu imc é {imc:.2f}, você é considerado um obeso de grau 2 (obesidade severa             |) ')
    print(' | Nessa faixa, os riscos de saúde aumentam bastante, almentando a provabilidade de    |')
    print(' | Doenças cardiovasculares (infarto, AVC, hipertensão); Doenças respiratórias e etc...|')
    print(' | PROCURE URGENTIMENTE UM NUTICIONISTA !!! faça Atividade física supervisionada e     |')
    print(' | mude seu estilo de vida.                                                            |')
    print(' _______________________________________________________________________________________')

else: 

    print('________________________________________________________________________________________________________________')
    print(f'|seu imc é {imc:.2f}, você é um obeso de grau 3 ! procure ajuda.                                                  |')
    print(' |  Essa é a faixa mais grave da obesidade. Nela, o risco de complicações de saúde é muito alto                |')
    print(' | porque o excesso de gordura afeta diretamente órgãos vitais. PROCURE AJUDA !!!                              |')
    print(' | você precisa de um Acompanhamento médico obrigatório, Tratamento multidisciplinar e uma Cirurgia bariátrica.|')
    print(' | já mandei você ir procurar ajuda ?                                                                          |')
    print('________________________________________________________________________________________________________________')