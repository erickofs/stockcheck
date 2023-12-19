# pylint: disable=consider-using-with
# . Cada linha contem um certo numero de campos separados por virgulas (arquivo CSV)
# . O numero de campos não é o mesmo em todas as linhas, algumas linhas tem mais campos, outras tem menos campos.
# . Podem haver mais de uma linha do mesmo item com estoques de diferentes localidades

# . Usar o minimo possivel de imports
import sys
# . Ler um arquivo texto chamado data.txt linha por linha
# . Imprimir mensagem de erro caso o arquivo data.txt não exista
try:
    file = open('data.txt', 'r', encoding='ansi')
except FileNotFoundError:
    print("File 'data.txt' does not exist in currennt directory.")
    sys.exit(1)
stock = {}
for line in file:
    # . Ignorar linhas em branco
    if line == "":
        continue
    fields = line.strip().split(',')
    # . Ignorar linhas de comentário (que começam com '#') e linhas com menos de 3 campos
    if fields[0].startswith('#') or len(fields) < 3:
        continue
    if fields[-1] == "":
        continue
    # . O primeiro campo da linha é o codigo do item, o ultimo campo da linha é o numero em estoque
    # . O codigo do item é uma string e o numero em estoque é um inteiro
    # . Itens Geladeira, geladeira e GELADEIRA são o mesmo item.
    # . Se o campo item tiver espaços antes ou depois, tem que tirar. Ou seja: "geladeira  " conta como "geladeira".
    # . Na impressão os itens vão estar só com a primeira letra maiúscula. 
    # . Ignorar espaços no inicio e no final da linha
    item = fields[0].strip().lower().capitalize()
    quantity = int(fields[-1])
    # . O programa deve somar o total de estoque por item em um dicionário e no final imprimir esse dicionário
    if item in stock:
        stock[item] += quantity
    else:
        stock[item] = quantity
file.close()
for item in sorted(stock):
    print(f'Product Code:{item}, Total Stock: {stock[item]}')
