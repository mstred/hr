def main():
    from argparse import ArgumentParser
    from sys import stdout
    from hr import export, users as users_module

    parser = ArgumentParser()

    parser.add_argument('--path', help='A custom path to the export file')
    parser.add_argument('--format', default='json', choices=['csv', 'json'], type=str.lower)

    args = parser.parse_args()

    export_file = open(args.path, 'w', newline='') if args.path else stdout
    users = users_module.fetch_users()

    if args.format == 'csv':
        export.to_csv_file(export_file, users)
    elif args.format == 'json':
        export.to_json_file(export_file, users)

