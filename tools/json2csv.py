import json
import csv
from django.conf import settings
from os.path import join, splitext

# Opening JSON file and loading the data
# into the variable data
def json2csv(json_file):
    data = json.load(json_file)

    # now we will open a file for writing
    csv_output_file = join(settings.MEDIA_ROOT, splitext(json_file.name)[0]  + ".csv")
    data_file = open(csv_output_file, 'w')  

    # create the csv writer object
    csv_writer = csv.writer(data_file)

    header_written = False
    for item in data:
        if not header_written:
            # Writing headers of CSV file
            header = item.keys()
            csv_writer.writerow(header)
            header_written = True
        # Writing data of CSV file
        csv_writer.writerow(item.values())
    
    data_file.close()
    return csv_output_file
