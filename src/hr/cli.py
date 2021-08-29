from argparse import ArgumentParser

def create_parser():
    parser = ArgumentParser()

    parser.add_argument('--path', help='A custom path to the export file')
    parser.add_argument('--format', default='json', options=['csv', 'json'], type=str.lower)

    return parser

