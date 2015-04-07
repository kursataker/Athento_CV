import os
import cv2 as cv
import pytest
from tesspy import tesspy as tp
from subprocess import CalledProcessError

class Test_TessPy:

        #This image has a white background and a black line, no text. Bad input
        #for tesseract, can't apply OCR.
        file_path = os.path.abspath(os.path.join(os.path.dirname(
                            "__file__"), "resources/", "test_white.png"))

        #Good image to apply OCR
        file_path_ocr = os.path.abspath(os.path.join(os.path.dirname(
                            "__file__"), "resources/", "test_image_good.png"))

        #Good image to apply OCR
        file_path_circle = os.path.abspath(os.path.join(os.path.dirname(
                            "__file__"), "resources/", "test_image.png"))

        #Sample txt file
        txt_file = os.path.abspath(os.path.join(os.path.dirname(
                            "__file__"), "resources/", "test_text"))


    #Tests of exec_tess:

        #Everything works ok
        def test_exec_tess_good(self):
            cmd = ["tesseract", "-v"]
            assert tp.exec_tess(cmd) != ""

        #Error if command is void
        def test_exec_tess_void(self):
            with pytest.raises(ValueError) as exc:
                tp.exec_tess("")
            assert exc.value.message == "The command string can't be ''."

        #Error if command is None
        def test_exec_tess_none(self):
            with pytest.raises(ValueError) as exc:
                tp.exec_tess(None)
            assert exc.value.message == "The command string can't be a None" \
                                        " object."

        #Error if can't apply OCR due to too few characters
        def test_exec_tess_invalid(self):
            cmd = ["tesseract", self.file_path, "output_file", "-psm", "0"]
            with pytest.raises(Exception) as exc:
                tp.exec_tess(cmd)
            assert exc.value.message == "Can't apply OCR with Tesseract on " \
                                        "this document."

        #Error if wrong tesseract command
        def test_exec_tess_wrong(self):
            cmd = ["tesseract", "--wrong"]
            with pytest.raises(Exception) as exc:
                tp.exec_tess(cmd)
            assert exc.value.message == "Can't apply OCR with Tesseract on " \
                                        "this document."


    #Tests of get_info:

        #Everything works ok
        def test_get_info_good(self):
            assert tp.get_info(self.file_path_ocr) != ""

        #Error if file not exists
        def test_get_info_io_error(self):
            with pytest.raises(IOError) as exc:
                tp.get_info("fakeFile")
            assert exc.value.message == "Input file not found."

        #Error executing tesseract
        def test_get_info_invalid(self):
            with pytest.raises(Exception) as exc:
                tp.get_info(self.file_path)
            assert exc.value.message == "Can't apply OCR with Tesseract on " \
                                        "this document."


    #Tests of get_orientation:

        #Everything works ok
        def test_get_orientation_good(self):
            assert tp.get_orientation(self.file_path_ocr) >= 0

        #Error if file not exists
        def test_get_orientation_io_error(self):
            with pytest.raises(IOError) as exc:
                tp.get_orientation("fakeFile")
            assert exc.value.message == "Input file not found."

        #Error executing tesseract
        def test_get_orientation_invalid(self):
            with pytest.raises(Exception) as exc:
                tp.get_orientation(self.file_path)
            assert exc.value.message == "Can't apply OCR with Tesseract on " \
                                        "this document."


    #Tests of get_orientation_confidence:

        #Everything works ok
        def test_get_orientation_confidence_good(self):
            assert tp.get_orientation(self.file_path_ocr) >= 0

        #Error if file not exists
        def test_get_orientation_confidence_io_error(self):
            with pytest.raises(IOError) as exc:
                tp.get_orientation("fakeFile")
            assert exc.value.message == "Input file not found."

        #Error executing tesseract
        def test_get_orientation_confidence_invalid(self):
            with pytest.raises(Exception) as exc:
                tp.get_orientation(self.file_path)
            assert exc.value.message == "Can't apply OCR with Tesseract on " \
                                        "this document."


    #Tests of get_orientation_degrees:

        #Everything works ok
        def test_get_orientation_degrees_good(self):
            assert tp.get_orientation_degrees(self.file_path_ocr) >= 0

        #Error if file not exists
        def test_get_orientation_degrees_io_error(self):
            with pytest.raises(IOError) as exc:
                tp.get_orientation_degrees("fakeFile")
            assert exc.value.message == "Input file not found."

        #Error executing tesseract
        def test_get_orientation_degrees_invalid(self):
            with pytest.raises(Exception) as exc:
                tp.get_orientation_degrees(self.file_path)
            assert exc.value.message == "Can't apply OCR with Tesseract on " \
                                        "this document."


    #Tests of get_script:

        #Everything works ok
        def test_get_script_good(self):
            assert tp.get_script(self.file_path_ocr) >= 0

        #Error if file not exists
        def test_get_script_io_error(self):
            with pytest.raises(IOError) as exc:
                tp.get_script("fakeFile")
            assert exc.value.message == "Input file not found."

        #Error executing tesseract
        def test_get_script_invalid(self):
            with pytest.raises(Exception) as exc:
                tp.get_script(self.file_path)
            assert exc.value.message == "Can't apply OCR with Tesseract on " \
                                        "this document."


    #Tests of get_script_confidence:

        #Everything works ok
        def test_get_script_confidence_good(self):
            assert tp.get_script_confidence(self.file_path_ocr) >= 0

        #Error if file not exists
        def test_get_script_confidence_io_error(self):
            with pytest.raises(IOError) as exc:
                tp.get_script_confidence("fakeFile")
            assert exc.value.message == "Input file not found."

        #Error executing tesseract
        def test_get_script_confidence_invalid(self):
            with pytest.raises(Exception) as exc:
                tp.get_script_confidence(self.file_path)
            assert exc.value.message == "Can't apply OCR with Tesseract on " \
                                        "this document."


    #Tests of get_text:

        #Everything works ok
        def test_get_text_good(self):
            assert tp.get_text(self.file_path_ocr) != ""

        #Error if file not exists
        def test_get_text_io_error(self):
            with pytest.raises(IOError) as exc:
                tp.get_text("fakeFile")
            assert exc.value.message == "Input file not found."

        #Error executing tesseract
        def test_get_text_invalid(self):
            with pytest.raises(Exception) as exc:
                tp.get_text(self.file_path)
            assert exc.value.message == "Can't apply OCR with Tesseract on " \
                                        "this document."


    #Tests of get_text_autops:

        #Everything works ok
        def test_get_text_autops_good(self):
            assert tp.get_text_autops(self.file_path_ocr) != ""

        #Error if file not exists
        def test_get_text_autops_io_error(self):
            with pytest.raises(IOError) as exc:
                tp.get_text_autops("fakeFile")
            assert exc.value.message == "Input file not found."

        #Error executing tesseract
        def test_get_text_autops_invalid(self):
            with pytest.raises(Exception) as exc:
                tp.get_text_autops(self.file_path)
            assert exc.value.message == "Can't apply OCR with Tesseract on " \
                                        "this document."


    #Tests of get_text_autops_full:

        #Everything works ok
        def test_get_text_autops_full_good(self):
            assert tp.get_text_autops_full(self.file_path_ocr) != ""

        #Error if file not exists
        def test_get_text_autops_full_io_error(self):
            with pytest.raises(IOError) as exc:
                tp.get_text_autops_full("fakeFile")
            assert exc.value.message == "Input file not found."

        #Error executing tesseract
        def test_get_text_autops_full_invalid(self):
            with pytest.raises(Exception) as exc:
                tp.get_text_autops_full(self.file_path)
            assert exc.value.message == "Can't apply OCR with Tesseract on " \
                                        "this document."


    #Tests of get_text_autops_osd:

        #Everything works ok
        def test_get_text_autops_osd_good(self):
            assert tp.get_text_autops_osd(self.file_path_ocr) != ""

        #Error if file not exists
        def test_get_text_autops_osd_io_error(self):
            with pytest.raises(IOError) as exc:
                tp.get_text_autops_osd("fakeFile")
            assert exc.value.message == "Input file not found."

        #Error executing tesseract
        def test_get_text_autops_osd_invalid(self):
            with pytest.raises(Exception) as exc:
                tp.get_text_autops_osd(self.file_path)
            assert exc.value.message == "Can't apply OCR with Tesseract on " \
                                        "this document."


    #Tests of get_text_single_block:

        #Everything works ok
        def test_get_text_single_block_good(self):
            assert tp.get_text_single_block(self.file_path_ocr) != ""

        #Error if file not exists
        def test_get_text_single_block_io_error(self):
            with pytest.raises(IOError) as exc:
                tp.get_text_single_block("fakeFile")
            assert exc.value.message == "Input file not found."

        #Error executing tesseract
        def test_get_text_single_block_invalid(self):
            with pytest.raises(Exception) as exc:
                tp.get_text_single_block(self.file_path)
            assert exc.value.message == "Can't apply OCR with Tesseract on " \
                                        "this document."


    #Tests of get_text_single_block_vertical:

        #Everything works ok
        def test_get_text_single_block_vertical_good(self):
            assert tp.get_text_single_block_vertical(self.file_path_ocr) != ""

        #Error if file not exists
        def test_get_text_single_block_vertical_io_error(self):
            with pytest.raises(IOError) as exc:
                tp.get_text_single_block_vertical("fakeFile")
            assert exc.value.message == "Input file not found."

        #Error executing tesseract
        def test_get_text_single_block_vertical_invalid(self):
            with pytest.raises(Exception) as exc:
                tp.get_text_single_block_vertical(self.file_path)
            assert exc.value.message == "Can't apply OCR with Tesseract on " \
                                        "this document."


    #Tests of get_text_single_character:

        #Everything works ok
        def test_get_text_single_character_good(self):
            assert tp.get_text_single_character(self.file_path_ocr) != ""

        #Error if file not exists
        def test_get_text_single_character_io_error(self):
            with pytest.raises(IOError) as exc:
                tp.get_text_single_character("fakeFile")
            assert exc.value.message == "Input file not found."

        #Error executing tesseract
        def test_get_text_single_character_invalid(self):
            with pytest.raises(Exception) as exc:
                tp.get_text_single_character(self.file_path)
            assert exc.value.message == "Can't apply OCR with Tesseract on " \
                                        "this document."


    #Tests of get_text_single_column:

        #Everything works ok
        def test_get_text_single_column_good(self):
            assert tp.get_text_single_column(self.file_path_ocr) != ""

        #Error if file not exists
        def test_get_text_single_column_io_error(self):
            with pytest.raises(IOError) as exc:
                tp.get_text_single_character("fakeFile")
            assert exc.value.message == "Input file not found."

        #Error executing tesseract
        def test_get_text_single_column_invalid(self):
            with pytest.raises(Exception) as exc:
                tp.get_text_single_column(self.file_path)
            assert exc.value.message == "Can't apply OCR with Tesseract on " \
                                        "this document."


    #Tests of get_text_single_line:

        #Everything works ok
        def test_get_text_single_line_good(self):
            assert tp.get_text_single_line(self.file_path_ocr) != ""

        #Error if file not exists
        def test_get_text_single_line_io_error(self):
            with pytest.raises(IOError) as exc:
                tp.get_text_single_line("fakeFile")
            assert exc.value.message == "Input file not found."

        #Error executing tesseract
        def test_get_text_single_line_invalid(self):
            with pytest.raises(Exception) as exc:
                tp.get_text_single_line(self.file_path)
            assert exc.value.message == "Can't apply OCR with Tesseract on " \
                                        "this document."


    #Tests of get_text_single_word:

        #Everything works ok
        def test_get_text_single_word_good(self):
            assert tp.get_text_single_word(self.file_path_ocr) != ""

        #Error if file not exists
        def test_get_text_single_word_io_error(self):
            with pytest.raises(IOError) as exc:
                tp.get_text_single_word("fakeFile")
            assert exc.value.message == "Input file not found."

        #Error executing tesseract
        def test_get_text_single_word_invalid(self):
            with pytest.raises(Exception) as exc:
                tp.get_text_single_word(self.file_path)
            assert exc.value.message == "Can't apply OCR with Tesseract on " \
                                        "this document."


    #Tests of get_text_single_word_circle:

        #Everything works ok
        def test_get_text_single_word_circle_good(self):
            assert tp.get_text_single_word_circle(self.file_path_circle) != ""

        #Error if file not exists
        def test_get_text_single_word_circle_io_error(self):
            with pytest.raises(IOError) as exc:
                tp.get_text_single_word_circle("fakeFile")
            assert exc.value.message == "Input file not found."

        #Error executing tesseract
        def test_get_text_single_word_circle_invalid(self):
            with pytest.raises(Exception) as exc:
                tp.get_text_single_word_circle(self.file_path)
            assert exc.value.message == "Can't apply OCR with Tesseract on " \
                                        "this document."

    #Tests of get_version:

        #OK
        def test_get_version_good(self):
            assert tp.get_version() != 0


    #Tests of psm:

        #Everything works ok
        def test_psm_good(self):
            assert tp.psm(self.file_path_ocr) != ""

        #Error if file not exists
        def test_psm_io_error(self):
            with pytest.raises(IOError) as exc:
                tp.psm("fakeFile")
            assert exc.value.message == "Input file not found."

        #Error executing tesseract
        def test_psm_invalid(self):
            with pytest.raises(Exception) as exc:
                tp.psm(self.file_path)
            assert exc.value.message == "Can't apply OCR with Tesseract on " \
                                        "this document."

        #Error if option < 0
        def test_psm_option_lower_0(self):
            with pytest.raises(Exception) as exc:
                tp.psm(self.file_path, -1)
            assert exc.value.message == "Option values between 0 and 10. " \
                                        "Use tesseract -h in a terminal " \
                                        "to see a list of available options."

        #Error if option < 0
        def test_psm_option_bigger_10(self):
            with pytest.raises(Exception) as exc:
                tp.psm(self.file_path, 11)
            assert exc.value.message == "Option values between 0 and 10. " \
                                        "Use tesseract -h in a terminal " \
                                        "to see a list of available options."


    #Tests of read_txt_file:

        #Everthing works ok
        def test_read_txt_file_good(self):
            aux = self.txt_file + ".txt"
            f = open(aux, "w")
            f.write("This is a sample txt file created to perform this test")
            f.close()
            assert tp.read_txt_file(self.txt_file) != ""

        #Error if File not Found
        def test_read_txt_file_io_error(self):
            with pytest.raises(IOError) as exc:
                tp.read_txt_file(self.txt_file)
            assert exc.value.message == "Input file not found."