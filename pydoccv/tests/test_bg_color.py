import pytest
import os
from pydoccv.bg_color import clean

class Test_BGC:

    test_image = os.path.abspath(os.path.join(os.path.dirname("__file__"),
                                              "resources/", "test_image.png"))


    #Everything works ok
    def test_bgc_good(self):
        assert clean(self.test_image, 200, 3) == 0

    #Error if input file is ''
    def test_bgc_input_void(self):
        with pytest.raises(IOError) as exc:
            clean('', 200, 3)
        assert exc.value.message == "Input file can't be ''."

    #Error if input file is None
    def test_bgc_input_void(self):
        with pytest.raises(IOError) as exc:
            clean(None, 200, 3)
        assert exc.value.message == "Input file can't be ''."

    #Error if input file is ''
    def test_bgc_input_void(self):
        with pytest.raises(IOError) as exc:
            clean('', 200, 3)
        assert exc.value.message == "Input file can't be ''."

    #Error if input file not found
    def test_bgc_input_not_found(self):
        with pytest.raises(IOError) as exc:
            clean("fakeRoute", 300, 3)
        assert exc.value.message == "Input file not found."