import os
import cv2 as cv
import pytest
import tesspy.tesspy as tp
from subprocess import CalledProcessError

class Test_TessPy:

        file_path = test_image = os.path.abspath(os.path.join(os.path.dirname(
                            "__file__"), "resources/", "test_image.png"))

    #Tests of exec_tess:

        #Everything works ok
        def test_exec_tess_good(self):
            cmd = ["tesseract", "-v"]
            assert tp.exec_tess(cmd) != ""

        #Error if wrong Tesseract command
        def test_exec_tess_wrong(self):
            cmd = ["tesseract", "-wrong", "command"]
            with pytest.raises(ValueError) as exc:
                tp.exec_tess(cmd)
            assert exc.value.message == "The command string is not correct. " \
                                        "Check the syntax."

        #Error if can't apply OCR due to too few characters
        def test_exec_tess_invalid(self):
            cmd = ["tesseract", self.file_path, "output_file", "-psm", "0"]
            with pytest.raises(CalledProcessError) as exc:
                tp.exec_tess(cmd)
            assert exc.value.message == "Can't apply OCR with Tesseract on " \
                                        "this document."
            assert

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

"""

    #Tests of get_info:

        #Everything works ok
        def test_get_info_good(self):
            assert tp.get_info(self.file_path) != ""

        #Error if file not exists
        def test_get_info_wrong(self):
            with pytest.raises(IOError) as exc:
                tp.get_info("fakeFile")
            assert exc.value.message == "Input file not found."



    #Tests of get_orientation:

        #Everything works ok
        def test_get_orientation_good(self):
            assert isinstance(tp.get_orientation(self.file_path), int) == True

"""