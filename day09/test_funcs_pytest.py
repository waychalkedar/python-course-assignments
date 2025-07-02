import funcs

class TestFuncs():
    def test_funcs1(self):
        assert funcs.hhmm_to_minutes('01:30') == 90
    def test_funcs2(self):
        assert funcs.hhmm_to_minutes('16:15') == 975