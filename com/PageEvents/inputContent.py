# -*- coding: utf-8 -*-
import config
import time
from Utilities.unicodeCSVWriter import UnicodeWriter
import csv


class Result:
    Name = None
    Street = None
    Phone = None
    Email = None
    City = None


def write_csv_results():
    fileName = config.outputDir + "\\" + get_filename()
    ofile = open(fileName, 'wb')
    csv_writer = UnicodeWriter(ofile, delimiter=',', quotechar='"', quoting=csv.QUOTE_ALL)

    csv_writer.writerow(["Name", "Street", "City", "Phone", "Email"])

    for curr_result in config.Results:
        csv_writer.writerow([curr_result.Name, curr_result.Street,
                             curr_result.City, curr_result.Phone,
                             curr_result.Email])

    ofile.close()


def get_filename():
    return "output_" + time.strftime("%Y") + time.strftime("%m") + time.strftime("%d") + "_" + time.strftime("%H") + \
           time.strftime("%M") + time.strftime("%S") + ".csv"