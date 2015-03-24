import subprocess as sp
import sys

"""
TessPy is a simple Tesseract-OCR API in Python. It provides the same functiona-
lity as the tesseract command, using functions in Python and calling the 
tesseract instruction using the subprocess Python's package.
"""

# Basic methods

def exec_tess(cmd):
    """
    :param cmd: a list of strings containing the whole command
    :return:
        if error: -1
        else: returns the terminal output of the command received as parameter.

    This method works as our wrapper, as it is the only place where Tesseract
    is actually called.
    """

    try:
        output = sp.check_output(cmd, stderr=sp.STDOUT)
    except:
        output = -1
        print "Unexpected error: " + sys.exc_info()[0]
        raise
    return output



def get_info(file_path):
    """
    :param file_path: input file path
    :return: returns the complete orientation and script detection information
                obtained by "tesseract input_img output -psm 0"
    """

    return psm(file_path)



def get_orientation(file_path):
    """
    :param file_path: input file path
    :return:
        if error: -1
        else: returns the orientation of the document obtained by:
                "tesseract img -psm 0"
    """

    try:
        output = get_info(file_path)
        aux = output.split("Orientation: ")
        orientation = aux[1].split("\n")
    except:
        orientation = -1
        print "Unexpected error: " + sys.exc_info()[0]
        raise
    return orientation[0]



def get_orientation_confidence(file_path):
    """
    :param file_path: input file path
    :return:
        if error: -1
        else: returns the orientation confidence of the document obtained by:
                "tesseract img -psm 0"
    """

    try:
        output = get_info(file_path)
        aux = output.split("Orientation confidence: ")
        confidence = aux[1].split("\n")
    except:
        confidence = -1
        print "Unexpected error: " + sys.exc_info()[0]
        raise
    return confidence[0]



def get_orientation_degrees(file_path):
    """
    :param file_path: input file path
    :return:
        if error: -1
        else: returns the orientation in degrees of the document obtained by:
                ```tesseract img -psm 0```
    """

    try:
        output = get_info(file_path)
        aux = output.split("Orientation in degrees: ")
        degrees = aux[1].split("\n")
    except:
        degrees = -1
        print "Unexpected error: " + sys.exc_info()[0]
        raise
    return degrees[0]



def get_script(file_path):
    """
    :param file_path:  input file path
    :return:
        if error: -1
        else: returns the script value of the document obtained by:
                ```tesseract img -psm 0```
    """

    try:
        output = get_info(file_path)
        aux = output.split("Script: ")
        script = aux[1].split("\n")
    except:
        script = -1
        print "Unexpected error: " + sys.exc_info()[0]
        raise
    return script[0]



def get_script_confidence(file_path):
    """
    :param file_path: input file path
    :return:
        if error: -1
        else: returns the script confidence value obtained by:
                ```tesseract img -psm 0```
    """

    try:
        output = get_info(file_path)
        aux = output.split("Script confidence: ")
        confidence = aux[1].split("\n")
    except:
        confidence = -1
        print "Unexpected error: " + sys.exc_info()[0]
        raise
    return confidence[0]



def get_text(file_path, output_file = "", lang = "eng", config_file = ""):
    """
    :param file_path: path of the input file.
    :param output_file: output file name
    :param lang: set of languages to use in OCR. To use multiple languages use
                lang = "eng + esp" as parameter.
    :param config_file: the name of the config file to use. A config is a
                        plaintext file which contains a list of variables and
                        their values, one per line, with a space separating
                        variable from value.
                        Interesting config files include:

                            hocr: output in hOCR format instead of as a text
                                    file.
    :return: if error: None
            else: returns the text of an image. Equivalent to use
                    get_text_autops_full()
    """

    if(output_file == ""):
        output_file = file_path[:-4]
    file_path = file_path.encode("utf-8")
    output_file = output_file.encode("utf-8")

    cmd = ["tesseract", file_path, output_file, "-l", lang, config_file]
    output = exec_tess(cmd)

    if output != -1:
        out_file = open(output_file + ".txt")
        text = out_file.read()
        out_file.close()
    else:
        text = None
    return text



def get_text_autops(file_path, output_file = "", lang = "eng",
                    config_file = ""):
    """
    :param file_path: input file path
    :param output_file: output file name
    :param lang: set of languages to use in OCR. To use multiple languages use
                lang = "eng + esp" as parameter.
    :param config_file: the name of the config file to use. A config is a
                        plaintext file which contains a list of variables and
                        their values, one per line, with a space separating
                        variable from value.
                        Interesting config files include:

                            hocr: output in hOCR format instead of as a text
                                    file.
    :return:
        if error: None
        else: returns the text of an image using an automatic page segmentation
                without OSD or OCR.
    """

    if(output_file == ""):
        output_file = file_path[:-4]
    file_path = file_path.encode("utf-8")
    output_file = output_file.encode("utf-8")

    cmd = ["tesseract", file_path, output_file, "-psm", "2", "-l", lang,
           config_file]
    output = exec_tess(cmd)

    if output != -1:
        text = read_txt_file(output_file)
    else:
        text = None
    return text



def get_text_autops_full(file_path, output_file = "", lang = "eng",
                         config_file = ""):
    """
    :param file_path: input file path
    :param output_file: output file name
    :param lang: set of languages to use in OCR. To use multiple languages use
                lang = "eng + esp" as parameter.
    :param config_file: the name of the config file to use. A config is a
                        plaintext file which contains a list of variables and
                        their values, one per line, with a space separating
                        variable from value.
                        Interesting config files include:

                            hocr: output in hOCR format instead of as a text
                                    file.
    :return:
        if error: None
        else: returns the text of an image using a fully automatic page
                segmentation without OSD (default operation).
                Similar to get_text()
    """

    if(output_file == ""):
        output_file = file_path[:-4]
    file_path = file_path.encode("utf-8")
    output_file = output_file.encode("utf-8")

    cmd = ["tesseract", file_path, output_file, "-psm", "3", "-l", lang,
           config_file]
    output = exec_tess(cmd)

    if output != -1:
        text = read_txt_file(output_file)
    else:
        text = None
    return text



def get_text_autops_osd(file_path, output_file = "", lang = "eng",
                        config_file = ""):
    """
    :param file_path: input file path
    :param output_file: output file name
    :param lang: set of languages to use in OCR. To use multiple languages use
                lang = "eng + esp" as parameter.
    :param config_file: the name of the config file to use. A config is a
                        plaintext file which contains a list of variables and
                        their values, one per line, with a space separating
                        variable from value.
                        Interesting config files include:

                            hocr: output in hOCR format instead of as a text
                                    file.
    :return:
        if error: None
        else: returns the text of an image using an automatic page segmentation
                with OSD.
    """

    if(output_file == ""):
        output_file = file_path[:-4]
    file_path = file_path.encode("utf-8")
    output_file = output_file.encode("utf-8")

    cmd = ["tesseract", file_path, output_file, "-psm", "1", "-l", lang,
           config_file]
    output = exec_tess(cmd)

    if output != -1:
        text = read_txt_file(output_file)
    else:
        text = None
    return text



def get_text_single_block(file_path, output_file = "", lang = "eng",
                          config_file = ""):
    """
    :param file_path: input file path
    :param output_file: output file name
    :param lang: set of languages to use in OCR. To use multiple languages use
                lang = "eng + esp" as parameter.
    :param config_file: the name of the config file to use. A config is a
                        plaintext file which contains a list of variables and
                        their values, one per line, with a space separating
                        variable from value.
                        Interesting config files include:

                            hocr: output in hOCR format instead of as a text
                                    file.
    :return:
        if error: None
        else: returns the text of an image assuming a single block of text.
    """

    if(output_file == ""):
        output_file = file_path[:-4]
    file_path = file_path.encode("utf-8")
    output_file = output_file.encode("utf-8")

    cmd = ["tesseract", file_path, output_file, "-psm", "6", "-l", lang,
           config_file]
    output = exec_tess(cmd)

    if output != -1:
        text = read_txt_file(output_file)
    else:
        text = None
    return text



def get_text_single_block_vertical(file_path, output_file = "", lang = "eng",
                                   config_file = ""):
    """
    :param file_path: input file path
    :param output_file: output file name
    :param lang: set of languages to use in OCR. To use multiple languages use
                lang = "eng + esp" as parameter.
    :param config_file: the name of the config file to use. A config is a
                        plaintext file which contains a list of variables and
                        their values, one per line, with a space separating
                        variable from value.
                        Interesting config files include:

                            hocr: output in hOCR format instead of as a text
                                    file.
    :return:
        if error: None
        else: returns the text of an image assuming a single block of vertically
                aligned text.
    """

    if(output_file == ""):
        output_file = file_path[:-4]
    file_path = file_path.encode("utf-8")
    output_file = output_file.encode("utf-8")

    cmd = ["tesseract", file_path, output_file, "-psm", "5", "-l", lang,
           config_file]
    output = exec_tess(cmd)

    if output != -1:
        text = read_txt_file(output_file)
    else:
        text = None
    return text



def get_text_single_character(file_path, output_file = "", lang = "eng",
                              config_file = ""):
    """
    :param file_path: input file path
    :param output_file: output file name
    :param lang: set of languages to use in OCR. To use multiple languages use
                lang = "eng + esp" as parameter.
    :param config_file: the name of the config file to use. A config is a
                        plaintext file which contains a list of variables and
                        their values, one per line, with a space separating
                        variable from value.
                        Interesting config files include:

                            hocr: output in hOCR format instead of as a text
                                    file.
    :return:
        if error: None
        else: returns the text of an image treating the image as a single
                character.
    """

    if(output_file == ""):
        output_file = file_path[:-4]
    file_path = file_path.encode("utf-8")
    output_file = output_file.encode("utf-8")

    cmd = ["tesseract", file_path, output_file, "-psm", "10", "-l", lang,
           config_file]
    output = exec_tess(cmd)

    if output != -1:
        text = read_txt_file(output_file)
    else:
        text = None
    return text



def get_text_single_column(file_path, output_file = "", lang = "eng",
                           config_file = ""):
    """
    :param file_path: input file path
    :param output_file: output file name
    :param lang: set of languages to use in OCR. To use multiple languages use
                lang = "eng + esp" as parameter.
    :param config_file: the name of the config file to use. A config is a
                        plaintext file which contains a list of variables and
                        their values, one per line, with a space separating
                        variable from value.
                        Interesting config files include:

                            hocr: output in hOCR format instead of as a text
                                    file.
    :return:
        if error: None
        else: returns the text of an image assuming a single column of text of
                variable sizes.
    """

    if(output_file == ""):
        output_file = file_path[:-4]
    file_path = file_path.encode("utf-8")
    output_file = output_file.encode("utf-8")

    cmd = ["tesseract", file_path, output_file, "-psm", "4", "-l", lang,
           config_file]
    output = exec_tess(cmd)

    if output != -1:
        text = read_txt_file(output_file)
    else:
        text = None
    return text



def get_text_single_line(file_path, output_file = "", lang = "eng",
                         config_file = ""):
    """
    :param file_path: input file path
    :param output_file: output file name
    :param lang: set of languages to use in OCR. To use multiple languages use
                lang = "eng + esp" as parameter.
    :param config_file: the name of the config file to use. A config is a
                        plaintext file which contains a list of variables and
                        their values, one per line, with a space separating
                        variable from value.
                        Interesting config files include:

                            hocr: output in hOCR format instead of as a text
                                    file.
    :return:
        if error: None
        else: returns the text of an image treating the image as a single text
                line.
    """

    if(output_file == ""):
        output_file = file_path[:-4]
    file_path = file_path.encode("utf-8")
    output_file = output_file.encode("utf-8")

    cmd = ["tesseract", file_path, output_file, "-psm", "7", "-l", lang,
           config_file]
    output = exec_tess(cmd)

    if output != -1:
        text = read_txt_file(output_file)
    else:
        text = None
    return text



def get_text_single_word(file_path, output_file = "", lang = "eng",
                         config_file = ""):
    """
    :param file_path: input file path
    :param output_file: output file name
    :param lang: set of languages to use in OCR. To use multiple languages use
                lang = "eng + esp" as parameter.
    :param config_file: the name of the config file to use. A config is a
                        plaintext file which contains a list of variables and
                        their values, one per line, with a space separating
                        variable from value.
                        Interesting config files include:

                            hocr: output in hOCR format instead of as a text
                                    file.
    :return:
        if error: None
        else: returns the text of an image treating the image as a single word.
    """

    if(output_file == ""):
        output_file = file_path[:-4]
    file_path = file_path.encode("utf-8")
    output_file = output_file.encode("utf-8")

    cmd = ["tesseract", file_path, output_file, "-psm", "8", "-l", lang,
            config_file]
    output = exec_tess(cmd)

    if output != -1:
        text = read_txt_file(output_file)
    else:
        text = None
    return text



def get_text_single_word_circle(file_path, output_file = "", lang = "eng",
                                    config_file = ""):
    """
    :param file_path: input file path
    :param output_file: output file name
    :param lang: set of languages to use in OCR. To use multiple languages use
                lang = "eng + esp" as parameter.
    :param config_file: the name of the config file to use. A config is a
                        plaintext file which contains a list of variables and
                        their values, one per line, with a space separating
                        variable from value.
                        Interesting config files include:

                            hocr: output in hOCR format instead of as a text
                                    file.
    :return:
        if error: None
        else: returns the text of an image treating the image as a single word
                in a circle.
    """

    if(output_file == ""):
        output_file = file_path[:-4]
    file_path = file_path.encode("utf-8")
    output_file = output_file.encode("utf-8")

    cmd = ["tesseract", file_path, output_file, "-psm", "9", "-l", lang,
           config_file]
    output = exec_tess(cmd)

    if output != -1:
        text = read_txt_file(output_file)
    else:
        text = None
    return text



def get_version():
    """
    :return:
        if error: -1
        else: returns tesseract --version output.
    """
    try:
        cmd = ["tesseract", "-v"]
        output = exec_tess(cmd)
    except:
        output = -1
    return output



def psm(file_path, output_file = "", option = 0, lang = "eng",
        config_file = ""):
    """
    :param file_path: input file path
    :param output_file: output file name
    :param option:
        Option values are the same that are specified in the manual:
            0 = Orientation and script detection (OSD) only.
            1 = Automatic page segmentation with OSD.
            2 = Automatic page segmentation, but no OSD, or OCR
            3 = Fully automatic page segmentation, but no OSD. (Default)
            4 = Assume a single column of text of variable sizes.
            5 = Assume a single uniform block of vertically aligned text.
            6 = Assume a single uniform block of text.
            7 = Treat the image as a single text line.
            8 = Treat the image as a single word.
            9 = Treat the image as a single word in a circle.
            10 = Treat the image as a single character.
    :param lang: set of languages to use in OCR. To use multiple languages use
                lang = "eng + esp" as parameter.
    :param config_file: the name of the config file to use. A config is a
                        plaintext file which contains a list of variables and
                        their values, one per line, with a space separating
                        variable from value.
                        Interesting config files include:

                            hocr: output in hOCR format instead of as a text
                                    file.

    :return:
        if error: -1
        else: returns terminal output of "tesseract input_img output -psm option"
    """

    info = ""
    error_msg = "Option values between 0 and 10. Use tesseract -h in a" \
                "terminal to see a list of available options."
    try:
        if(output_file == ""):
            output_file = file_path[:-4]
        file_path = file_path.encode("utf-8")
        output_file = output_file.encode("utf-8")

        cmd = ["tesseract", file_path, output_file, "-psm", str(option), "-l",
               lang, config_file]
        output = exec_tess(cmd)
    except :
        print error_msg
        info = -1
    return output



def read_txt_file(file_name):
    """
    :param file_name: input file path
    :return: returns the text of the txt file received by parameter
    """
    try:
        f = open(file_name + ".txt")
        text = f.read()
        f.close()
    except IOError:
        output = -1
        print "IOError error: " + sys.exc_info()[0]
    return text
