import os

# Library of functions

def file_exists(input_file):
    """
    :param input_file: path to the input file
    :return: true or false wether the file exists or not.
    """
    return os.path.isfile(input_file)