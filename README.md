# EXPLICAÇÃO DO CÓDIGO

def read_file(filename, delimiter)
Abre o aquirvo csv ou tsv e devolve linha por linha(gerador) com um split pelo delimitado setado

def between(value, ranges)
Verifica se o valor esta entre os dois valores especificados se o segundo valor for nulo parte do
pré-suposto que não há um range limite

def read_rotas_file(line)
verifica os se é aquela linha que devo usar para obter parametros

def define_kg(taxs)
Define a unidade do peso a ser usada para ligar os arquivos csv/tsv
L:32 diferencia tabela um de tabela2 pelo tamanho para acesso direto a posição na lista passada por 
parametro da função

def total_price(taxs)
calcula o preço total de acordo com as tabelas
Explicação linha a linha:
L:40 calcula o preço total da carga usando o parametro passado por linha de comando * valor por
kg retirado da tabela, indifere da tabela
L:41 verifica se é a primeira tabela pelo tamanho da lista passada por parametro da função
L:47 verifica se há um limite de peso na rota segundo a tabela2
L:48 verifica se o peso passado pela linha de comando é superior ao limite se sim imprime a mensagem
'tabela2: -, -' e retorna

def calculate(taxs, price_filename, delimiter)
define os parametro do para o calculo de preço
Explicação linha a linha:
L:63 pesquisa no arquivo de preço por kg usando a função read_file
L:64 verifica se aquela linha esta no na unidade de medida usada e se o peso esta nos limites
L:68 caso o for seja completado imprime uma mensagem ao usuário

def main()
execução do programa em si
Explicação linha a linha:
L:72 verifica se todos os argumentos foram passados na linha de comando senão imprime uma mensagem ao usuário
com os a lista de argumentos necessários e sua ordem e termina a execução
L:75 e 76 retira . dos argumentos peso e nota_fiscal para futura verificação futura
L:77 verifica se o peso e o valor da nota são realmente numeros senão imprime uma mensagem de erro para o usuário
L:82 esse if foi adicionado para que se possa executar o program mesmo que de fora da pasta raiz
L:86 e 92 percorem arquivos de rota para carregamento de dados a parti do csv/tsv
L:91 verifica se o primeiro for acho uma rota no csv senão imprime uma mensagem de erro ao usuário
