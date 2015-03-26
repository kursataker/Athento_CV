import pytest
import os
from pydoccv.threshold import apply
import cv2 as cv

class Test_TH:

    test_image = cv.imread(os.path.abspath(os.path.join(os.path.dirname(
                            "__file__"), "resources/", "test_image.png")))


    #Single threshold value, everything works ok
    def test_th_single_th(self):
        assert apply(self.test_image, "test_image_output", 150) == 0

    #Multi threshold values, everything works ok
    def test_th_multi_th(self):
        assert apply(self.test_image, "test_image_output", [220, 230, 250]) == 0

    #Error if input image is None
    def test_th_img_none(self):
        with pytest.raises(IOError) as exc:
            apply(None, "output", 150)
        assert exc.value.message == "Input image is None"

    #Error if output name is None object
    def test_th_out_none(self):
        with pytest.raises(ValueError) as exc:
            apply(self.test_image, None, 150)
        assert exc.value.message == "The output name can't be a None object."

    #Error if output name is ''
    def test_th_out_void(self):
        with pytest.raises(ValueError) as exc:
            apply(self.test_image, '', 150)
        assert exc.value.message == "The value of the output name can't be ''."


    #Error if threshold value is negative (only values between 0 and 255)
    def test_th_negative_thresh(self):
        with pytest.raises(ValueError) as exc:
            apply(self.test_image, "test_image_output", -230)
        assert exc.value.message == "All threshold values must be between 0 and 255"

    #Error if threshold value is over 255 (only values between 0 and 255)
    def test_th_over_thresh(self):
        with pytest.raises(ValueError) as exc:
            apply(self.test_image, "test_image_output", 270)
        assert exc.value.message == "All threshold values must be between 0 and 255"
