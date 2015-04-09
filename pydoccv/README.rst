========
PyDocCV
========

PyDocCV is a package developed using Python and OpenCV to improve OCR in
documents. Among the documents tested using this package are: passports, bills,
delivery notes, budgets, and other common documents.


This package includes several functions to transform images, for example: 
    - Delete coloured background.
    - Delete "salt and pepper" noise.

    
The quality of the output and it's OCR performance will depend on:

    - The quality of the source document, as the quality value increases so does
    the OCR.
    - The amount of noise in the document and where it's located.
    - The existance of watermarks.
    - The colour of the document. Clear colours are easier to remove than darker
        colours due to the proximity of the pixel values between the background
        and the text.
    - Your personal experience in image transformation. As you might need to 
        perform a combination of operations or change the parameters values 
        significantly.
