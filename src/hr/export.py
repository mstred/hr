from csv import writer
from json import dump as json_dump

def to_csv_file(export_file, users):
    export_file.write('name,id,home,shell\n') # add header row

    csv_writer = writer(export_file)
    # convert an object map to a list of properties, for each user (csv-friendly)
    rows = [[user['name'], user['id'], user['home'], user['shell']] for user in users]
    csv_writer.writerows(rows)

    export_file.close()


def to_json_file(export_file, users):
    json_dump(users, export_file, indent=4)
    export_file.close()

