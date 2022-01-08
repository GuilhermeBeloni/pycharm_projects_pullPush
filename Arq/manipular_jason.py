import json
inventario={}
opcao = int(input('Digite: '
                  '\n<1> para registrar'
                  '\n<2> para exibir')


while opcao > 0 and opcao < 3:
    if opcao == 1:
        resp = 'S'
        while resp == 'S':
            inventario[input('Digite o número patrimonial: ')] = [
                input('Data: '),
                input('Descriço: '),
                input('Departameno: ')]
            resp = input('Continuar? <s>').upper()
        with open('inventario_json.json', 'w') as arq_json:
            json.dump(inventario, arq_json)
        print('JSON gerado!')
