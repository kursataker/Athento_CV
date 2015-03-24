This file contains a basic description of each function included in the
TessPy package and a description of their common parameters and error codes.


##Common parameters

    - cmd: list of each element (word) of the command.
    - file_path: the path of the source file.
    - output_file: name of the output file without extension. Automatically txt
                    extension.
    - lang: The language to use. If none is specified, English is assumed. 
            Multiple languages may be specified, separated by plus characters. 
            Tesseract uses 3-character ISO 639-2 language codes.
    - config_file: the name of the config file to use. A config is a
                        plaintext file which contains a list of variables and
                        their values, one per line, with a space separating
                        variable from value.
                        Interesting config files include:

                            hocr: output in hOCR format instead of as a text
                                    file.


##Summary

    - exec_tess: core method, used to call the tesseract commands. Returns the
                    terminal output of the command received as parameter.

    - get_info: returns the complete orientation and script detection values
                obtained by:
      ```tesseract input_img output -psm 0```

    - get_orientation: returns the orientation of the document obtained by:
      ```tesseract img -psm 0```

    - get_orientation_confidence: returns the orientation confidence of the
                                    document obtained by:
      ```"tesseract img -psm 0```
      
    - get_orientation_degrees: returns the orientation in degrees of the 
                                document obtained by:
      ```tesseract img -psm 0```

    - get_script: returns the script value of the document obtained by: 
      ```tesseract img -psm 0```

    - get_script_confidence: returns the script confidence value obtained by:
      ```tesseract img -psm 0```

    - get_text: returns the text of an image. Equivalent to use 
                    get_text_autops_full()
    
    - get_text_autops: returns the text of an image using an automatic page 
                        segmentation without OSD or OCR.
    
    - get_text_autops_full: returns the text of an image using a fully automatic
                            page segmentation without OSD (default operation).
                            Similar to get_text()
    
    - get_text_autops_osd: returns the text of an image using an automatic page
                            segmentation with OSD.
    
    - get_text_single_block: returns the text of an image assuming a single
                                block of text.
    
    - get_text_single_block_vertical: returns the text of an image assuming a
                                        single block of vertically aligned text.
    
    - get_text_single_character: returns the text of an image treating the
                                    image as a single character.
    
    - get_text_single_column: returns the text of an image assuming a single
                                column of text of variable sizes.
    
    - get_text_single_line: returns the text of an image treating the image as
                            a single text line.
    
    - get_text_single_word: returns the text of an image treating the image as
                            a single word.
    
    - get_text_single_word_circle: returns the text of an image treating the
                                    image as a single word in a circle.

    - psm: set tesseract to run a subset of layout analysis and assume a certain
            form of image. This function is the generic form of the previous
            ones, except for exec_tess which is independent.
            
            Receives one of the following values as option:

        - 0 = Orientation and script detection (OSD) only.
        - 1 = Automatic page segmentation with OSD.
        - 2 = Automatic page segmentation, but no OSD, or OCR.
        - 3 = Fully automatic page segmentation, but no OSD. (Default)
        - 4 = Assume a single column of text of variable sizes.
        - 5 = Assume a single uniform block of vertically aligned text.
        - 6 = Assume a single uniform block of text.
        - 7 = Treat the image as a single text line.
        - 8 = Treat the image as a single word.
        - 9 = Treat the image as a single word in a circle.
        - 10 = Treat the image as a single character.
        
            Returns terminal output of "tesseract input_img output -psm option"
            
     - read_txt: returns the text of the txt file received by parameter.


##Error codes

    - get_text* functions returns None.
    - get_orientation*, get_script*, psm and exec_tess return -1.
    
Note: get_text* means all functions starting with the *get_text* string.
