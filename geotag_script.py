#!/usr/bin/python3

from gi.repository import GExiv2
import os
import csv

def list_csv(input_folder, csv_file_name):
    """
        Return a list. Require a tetracam GPS file and two arguments: path to folder and csv file name
    """
    csv_file_path = os.path.join(input_folder, csv_file_name)
    with open(csv_file_path, 'r') as f:
        reader = csv.reader(f)
        csv_list = list(reader)
    return csv_list



def geotag_file(input_folder, csv_list, ext = "TIF"):
    """
        Geotag files. Require a path to the folder containing the images, the list returned by list_csv function and the images extension.
        Invalid tags should be removed before saving metadata to avoid errors.
    """
    for item in list(csv_list):
        try:
            filename = item[0][:-4]
            abs_input_file_path = os.path.join(input_folder, filename + "." + ext)
            exif = GExiv2.Metadata(abs_input_file_path)
            exif.clear_tag('Exif.Image.Compression')  # remove invalid tag
            exif.set_gps_info(float(item[2]), float(item[1]), float(item[3])) # long lat alt
            exif.save_file()
        except Exception as e: print(e)
