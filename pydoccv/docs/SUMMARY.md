This file contains a basic description of each function included in the
PyDocCV package and their common parameters and error codes, as a basic guide to 
use it in the CLI .

##Common parameters

    - input_file: input filepath
    - thresh_val: list of values used to threshold.
    - quality: quality to use in the pdf_to_png transformation.
    - window_size: size of the window used to blurr. As this values increases so
                    does the blurr.
    - kernel_size: size of the kernel used to blurr. As this values increases so
                    does the blurr.

##Summary

Each module names identifies the kind of noise which we will try to remove
using the functions within the modules.

- **bg_color**:  transforms the image into grayscale and applies a series
 of threshold values to the image if none is indicated by parameter. Functions:

    ```clean(input_file, thresh_val =  [225, 220, 215, 210, 205, 200],
                         window_size = 3)```


- **salt_pepper**: transforms the image into grayscale and performs a complete 
erode operation. This is used to improve the quality of the text when it has 
much “salt and pepper” noise. Functions:

    ```clean(input_file,  thresh_val = [250, 245, 240, 230, 225, 220], 
                window_size = 5, kernel_size = 5)```

- **threshold**: applies a series of threshold values to an input image. 
    Functions:
    
    ```apply(image, thresh_values, output_name)```



##Use in CLI

Some of the functions described below may be used directly in the CLI. In order 
to know how to properly use the commands, open a terminal and navigate to the 
image_cleaning folder and type:

    ```python remove_bg_color.py -h```
    ```python salt_pepper.py -h```
    ```python threshold.py -h```



##salt_pepper

This script cleans an image with white noise (ie: text dotted due to bad pixel 
definition).

Once it receives the necessary parameters, it transforms the image into gray-
scale and applies a Gaussian Blur + a Median Blur to get extra definition to the 
text. After getting extra pixels for the letters, we use the function erode to 
outline the text in order to improve the quality of the data readed by OCR.
        
In the end, it applies a series of threshold values (or the ones received by 
parameter) to the modified image and shows them one by one asking the user to 
save the current thresholded image.
        
Returns:
    The input image with a blur and median filter in a series with different 
    threshold values.
                
Use in CLI:
    python clean_erode.py -i myImage.png
    python clean_erode.py -i myImage.png -t X, X = threshold value.
    python clean_erode.py -i myImage.png -k X, X = kernel size used in the erode
                                                     function.
    python clean_erode.py -i myImage.png -w X, where X is the size of the window
                                                     used in the Gaussian Blur.
                
    As usual, you can use any combination of parameters that you may need.
        
Import:
    To import this function into your application, you must include the follo-
    wing line at the beginning:

    ```from clean_erode import clean_erode```

    

##bg_color

This script allows to clean an image with noisy background (ie: coloured 
background).

Once it receives the parameters, it transforms the image to grayscale and 
applies a Gaussian Blur to the image. 
        
In the end, it applies a series of threshold values (or the ones received by 
parameter) to the modified image and shows them asking the user to save the the 
current thresholded image.
                       
Returns:
The original image thresholded in a series of values. The output image will be 
saved as:
                
    input_name-GREY-(V)THRESH, where (V) is the value of the applied threshold.
                
Use in CLI:
python remove_bg_color.py -i myImage.png
python remove_bg_color.py -i myImage.png -t X, where X is the threshold value
python remove_bg_color.py -i myImage.png -w X, where X is the size of the window 
                                                used in the Gaussian Blur.
                
As usual, you can use any combination of parameters that you may need.
        
Import:
To import this function into your application, you must include the following 
line at the beginning:
    ```from remove_bg_color import remove_bg_color```
    


##threshold

This function applies a series of threshold values (or the ones received by 
parameter) to the modified image and shows them asking the user to save the the 
current thresholded.

The output images are saved in the same directory as the source.

Returns:
    0 if everything works fine.
    -1 if error.

Use in CLI
python threshold.py -i myImage.png
python threshold.py -i myImage.png -t X, where X is the threshold value
python threshold.py -i myImage.png -o N, where N is the custom name for the
                                            output without the file extension.

Import:
To import this function into your application, you must include the following 
line at the beginnings:
    ```from thresh_list import threshold_list```
