A python script to geotag ADC Tetracam pictures based on Exiv2 and  gexiv2.

The script Works only in linux as gexiv2 has not been ported to Windows.

Invalid tags should be removed before saving metadata to avoid errors.
E.g. `exif.clear_tag('Exif.Image.Compression')`

Require a GPX file from PixelWrench2. Should work with other formats such jpg.


Example:

```python

path_to_csv_folder = "path_to_csv_folder"
path_to_images_folder
csv_file_name  = csv_file_name
image_extension = image_extension # TIFF

l = list_csv(path_to_csv_folder, csv_file_name, image_extension)

geotag_file(path_to_images_folder, l, "TIF")

```


Check some useful resource:

**Exiv2**

http://www.exiv2.org/index.html

**Metadata reference tables: Exif Schema for TIFF Properties**

http://www.exiv2.org/tags-xmp-tiff.html


**gexiv2 Python support**

https://wiki.gnome.org/Projects/gexiv2/PythonSupport


**gexiv2 source**

https://git.gnome.org/browse/gexiv2/tree/GExiv2.py
