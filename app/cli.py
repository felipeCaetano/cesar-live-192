from argparse import ArgumentParser

from app.cesar import decripta, encripta


parser = ArgumentParser(description='Cifra de Cesar')
parser.add_argument(
    'message', help='Menssagem a ser encriptada/decriptada', type=str
)
parser.add_argument(
    '-n', help='Valor de Rotação', default=13, type=int, required=False
)
parser.add_argument('-d', help='Decripta', required=False, action='store_true')


def cli():
    args = parser.parse_args()
    if args.d:
        resultado = decripta(args.message, args.n)
    else:
        resultado = encripta(args.message, args.n)

    print(f'Entrada: {args.message}')
    print(f'Saída: {resultado}')
