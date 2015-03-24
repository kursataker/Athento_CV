=============
TessPy
=============

TessPy is a simple Tesseract-OCR API in Python. It provides the same functiona-
lity as the tesseract command, using functions in Python and calling the 
tesseract instruction using the subprocess Python's package.

This API implements the most methods and parameters included in Tesseract's
manual page.

However, there might be some combination of instructions or parameters which
are not included in this API. In order to perform your custom tesseract
operation you can use the *exec_tess(cmd)* where *cmd* has the structure:

Let's assume you want to run the following command using the exec_tess()
function. In the CLI you would write:

    ```
        tesseract input_image output_file -psm 0
    ```

In order to use the exec_tess() method you should write the following in
your Python file:

    ```
        import tesseract_api as ta
        cmd = ['tesseract', 'input_image', 'output_file', '-psm', '0']
        exec_tess(cmd)```
    ```
    
Note than even numeric parameters have to be included between ''.

This is not an official implementation of Tesseract in Python, use at your own
risk.


