# -*- coding: utf-8 -*-#
from sys import argv
import csv


ROTA_CSV = 'tabela/rotas.csv'
PRECO_CSV = 'tabela/preco_por_kg.csv'
ROTA_TSV = 'tabela2/rotas.tsv'
PRECO_TSV = 'tabela2/preco_por_kg.tsv'


def read_file(filename, delimiter):
    with open(filename, 'rb') as csvfile:
        lines = csv.reader(csvfile, delimiter=delimiter, quotechar='|')
        for line in lines:
            yield line


def between(value, ranges):
    if ranges[0].isdigit():
        if ranges[1].isdigit():
            return int(ranges[0]) < value and int(ranges[1]) > value
        return int(ranges[0]) < value
    return False


def read_rotas_file(line):
    return argv[1] == line[0] and argv[2] == line[1]


def define_kg(taxs):
    if len(taxs) is 6:
        return taxs[4]
    else:
        return taxs[7]


def total_price(taxs):
    # limite	prazo	seguro	icms	alfandega	kg preço/kg
    load_value = float(argv[4])*float(taxs[len(taxs)-1])
    if len(taxs) is 5:
        secure = float(argv[3])*int(taxs[1])/100
        subtotal = load_value + secure + float(argv[3]) + int(taxs[3])
        total = 100*subtotal/94
        print 'tabela: %s, %.2f' % (taxs[0], total)
    else:
        if taxs[0] != '0':
            if int(taxs[0]) < float(argv[4]):
                print 'tabela2: -, -'
                return
        secure = float(argv[3])*int(taxs[2])/100
        subtotal = load_value + secure + float(argv[3])
        customhouse = subtotal*int(taxs[4])/100
        subtotal = subtotal + customhouse
        icms_denominator = 100 - int(taxs[3])
        total = 100*subtotal/icms_denominator
        print 'tabela: %s, %.2f' % (taxs[1], total)
            


def calculate(taxs, price_filename, delimiter):
    kg = define_kg(taxs)
    for line in read_file(price_filename, delimiter):
        if line[0] == kg and between(argv[4], (line[1], line[2])):
            taxs.append(line[3])
            total_price(taxs[2:])
            return
    print 'tabela2: -, -'


def main():
    if len(argv) != 5:
        print 'axado.py <origem> <destino> <nota_fiscal> <peso>'
        return 1
    validate1 = argv[3].replace('.', '')
    validate2 = argv[4].replace('.', '')
    if not validate1.isdigit() or not validate2.isdigit():
        print '''O valor da nota fiscal e o peso da carga
devem ser números inteiros ou décimais'''
        return 1
    path = './'
    if '/' in argv[0]:
        new_len = argv[0].find('axado.py')
        path = argv[0][:new_len]
    exist_route = False
    for line in read_file(path + ROTA_CSV, ','):
        if read_rotas_file(line):
            calculate(line, path + PRECO_CSV, ',')
            exist_route = True
            break
    if exist_route:
        for line in read_file(path + ROTA_TSV, '\t'):
            if read_rotas_file(line):
                calculate(line, path + PRECO_TSV, '\t')
                break
    else:
        print 'Rota inexistente'


if __name__ == "__main__":
    main()
