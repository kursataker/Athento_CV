import pytest
import os
from pydoccv.salt_pepper import clean

class Test_SP:

    test_image = os.path.abspath(os.path.join(os.path.dirname("__file__"),
                                              "resources/", "test_image.png"))

    #Everything works great
    def test_sp_good(self):
        assert clean(self.test_image, 250, 3, 3) == 0


    #Error if threshold value is negative (only values between 0 and 255)
    def test_sp_negative_thresh(self):
        with pytest.raises(ValueError) as exc:
            clean(self.test_image, -20, 3, 3)
        assert exc.value.message == "All threshold values must be between 0 and 255"

    #Error if threshold value is over 255 (only values between 0 and 255)
    def test_sp_over_thresh(self):
        with pytest.raises(ValueError) as exc:
            clean(self.test_image, 256, 3, 3)
        assert exc.value.message == "All threshold values must be between 0 and 255"

    #Error if window_size < 0 (only positive odd values admited)
    def test_sp_negative_window(self):
        with pytest.raises(ValueError) as exc:
            clean(self.test_image, 250, -1, 3)
        assert exc.value.message == "Window size value must be positive and odd."


    #Error if kernel_size < 0  (only positive odd values admited)
    def test_sp_negative_kernel(self):
        with pytest.raises(ValueError) as exc:
            clean(self.test_image, 250, 3, -1)
        assert exc.value.message == "Kernel size value must be positive and odd."


    #Error if window_size has a even value (only positive odd values admited)
    def test_sp_even_window(self):
        with pytest.raises(ValueError) as exc:
            clean(self.test_image, 250, 2, 3)
        assert exc.value.message == "Window size value must be positive and odd."


    #Error if kernel_size has a even value (only positive odd values admited)
    def test_sp_even_kernel(self):
        with pytest.raises(ValueError) as exc:
            clean(self.test_image, 250, 3, 2)
        assert exc.value.message == "Kernel size value must be positive and odd."

    #Error input image not found
    def test_sp_img_not_found(self):
        with pytest.raises(IOError) as exc:
            clean("", 250, 3, 3)
        assert exc.value.message == "Input file not found"

    #Unexpected error
    def test_sp_io(self):
        with pytest.raises(Exception) as exc:
            clean(self.test_image, 250, 3, 3)
        assert exc.value.message != ""