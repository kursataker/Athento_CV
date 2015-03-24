import os

"""
        Author: Daniel Ramirez Torres
        
        The transform function uses the command pdftoppm to transform a PDF file
        into a PNG file. As it uses a system command to make the transformation,
        this script might not work if your computer if you don't have the 
        library installed or your OS uses a different syntax 
        
        Requirements:
                pdftoppm installed
        
        Parameters:
                input_file, the source file
                dpi, the DPI resolution of the output file
        
        Install:
                pdftoppm is included in the poppler-utils packages.
                sudo apt-get install poppler-utils
                
                Tested in Ubuntu 14.04
                
        Returns:
                The name of the PNG file
                
                
- **pdf_to_png**: set of functions that check if the input file has a PDF exten-
sion (get_pdf function). If so, it transforms each page of the PDF file into a 
PNG image (transform). Functions:

    ```transform(input_file, dpi = 400)```
    ```get_png(file_name, quality = 400)```

"""

def transform(input_file, dpi = 400):
        try:
                output_name = input_file[:-4]
                print "Transforming PDF to PNG..."
                cmd = "pdftoppm -png -rx {0} -ry {0} {1} {2}".format( 
                      dpi, input_file, output_name)
                os.popen(cmd)
                print "Done."
                return output_name+"-1.png"
                                        
        except OSError as e:
                print "Error: {0}".format(e)
                
"""
        The get_png function checks if the file as input has a PDF extension. 
        If so, it calls the transform function to get the PNG's of the PDF.
        
        Warning: this script doesn't work properly with multi-page PDF's.
"""
def get_png(file_name, quality = 400):
        if file_name[-3::] == "pdf":
                        file_name = transform(file_name, quality)
                        print file_name
        return file_name
