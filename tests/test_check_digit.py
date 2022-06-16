import sys
sys.path.insert(0,"../jp_prefecture")

from jp_prefecture.checkdigit import validate_checkdigit, calc_checkdigit

class TestClass:
    def test_validate_checkdigit(self):
        assert ( validate_checkdigit(261009)
                 == 26100 )

    def test_validate_checkdigit_false(self):
        assert ( validate_checkdigit(261008)
                 == None )

    def test_validate_checkdigit_as_str(self):
        assert ( validate_checkdigit("261009")
                 == "26100" )

    def test_validate_checkdigit_as_str_false(self):
        assert ( validate_checkdigit("261008")
                 == None )

    def test_validate_checkdigit_as_str_no_checkdigit(self):
        assert ( validate_checkdigit("26100", 5)
                 == "26100" )

    def test_validate_checkdigit_as_int_no_checkdigit(self):
        assert ( validate_checkdigit(26100, 5)
                 == 26100 )

    def test_validate_checkdigit_as_int_no_checkdigit_short(self):
        assert ( validate_checkdigit(1100, 5)
                 == 1100 )

    def test_validate_checkdigit_as_str_no_checkdigit_short(self):
        assert ( validate_checkdigit("1100", 5)
                 == "01100" )

    def test_validate_checkdigit_as_str_short(self):
        assert ( validate_checkdigit("2610", 5)
                 == None )

    def test_validate_checkdigit_short(self):
        assert ( validate_checkdigit("2610", 5)
                 == None )

    def test_validate_checkdigith_num_digits(self):
        assert ( validate_checkdigit(261009, 5)
                 == 26100 )

    def test_validate_checkdigit_num_digits_as_str(self):
        assert ( validate_checkdigit("261009", 5)
                 == "26100" )

    def test_validate_checkdigit_with_weights(self):
        assert ( validate_checkdigit(261009, weights=[6,5,4,3,2])
                 == 26100 )

    def test_cacl_checkdig(self):
        assert ( calc_checkdigit(26100)
                 == 261009 )

    def test_cacl_checkdig_str(self):
        assert ( calc_checkdigit("26100")
                 == "261009" )

    def test_cacl_checkdig_only_digit(self):
        assert ( calc_checkdigit(26100, only_checkdigit=True)
                 == 9 )

    def test_cacl_checkdig_str_only_digit(self):
        assert ( calc_checkdigit("26100", only_checkdigit=True)
                 == "9" )

    def test_cacl_checkdig_str_only_digit(self):
        assert ( calc_checkdigit("26100",  weights=[6,5,4,3,2])
                 == "261009" )

    def test_validate_isdb10(self):
        assert( validate_checkdigit(4900900672) == 490090067)

    def test_validate_isdb10_str(self):
        assert( validate_checkdigit("4900900672") == "490090067")

    def test_validate_isdb13_str(self):
        assert( validate_checkdigit("978-4-906649-006") == "978490664900")
