import unittest
import internship_password_generetor_2 as i

class TestStringMethods(unittest.TestCase):

#-----------------------------------------------------------------------------
    def test_1password_generator(self):
        self.assertTrue(i.password_generator())
    
    def test_2password_generator(self):
        self.assertTrue(i.password_generator())

    def test_3password_generator(self):
        self.assertTrue(i.password_generator())
#-----------------------------------------------------------------------------

    def test_1check_if_password_has_digit(self):
        assert i.check_item_digit('karamba666!') is True

    def test_2check_if_password_has_digit(self):
        assert i.check_item_digit('72btttttmxkPatrol') is True

    def test_3check_if_password_has_digit(self):
        assert i.check_item_digit('vytynanky') is False
    
    def test_4check_if_password_has_digit(self):
        assert i.check_item_digit('*j$Tlaksi963897') is True

#-------------------------------------------------------------------------------
    def test_1check_item_lowercase_and_uppercase(self):
        assert i.check_item_lowercase_and_uppercase('karamba666!') is False

    def test_2check_item_lowercase_and_uppercase(self):
        assert i.check_item_lowercase_and_uppercase('72btttttmxkPatrol') is True

    def test_3check_item_lowercase_and_uppercase(self):
        assert i.check_item_lowercase_and_uppercase('vytynanky') is False
    
    def test_4check_item_lowercase_and_uppercase(self):
        assert i.check_item_lowercase_and_uppercase('*j$Tlaksi963897') is True

#---------------------------------------------------------------------------------

    def test_1check_item_for_punctuation_mark(self):
        assert i.check_item_punctuation('karamba666!') is True

    def test_2check_item_for_punctuation_mark(self):
        assert i.check_item_punctuation('72btttttmxkPatrol') is False

    def test_3check_item_for_punctuation_mark(self):
        assert i.check_item_punctuation('vytynanky') is False
    
    def test_4check_item_for_punctuation_mark(self):
        assert i.check_item_punctuation('*j$Tlaksi963897') is True

#----------------------------------------------------------------------------------

    def test_1check_item_for_length(self):
        assert i.check_length('karamba666!') is False

    def test_2check_item_for_check_length(self):
        assert i.check_length('72btttttmxkPatrol') is True

    def test_3check_item_for_check_length(self):
        assert i.check_length('vytynanky') is False
    
    def test_4check_item_for_check_length(self):
        assert i.check_length('*j$Tlaksi963897') is True

#---------------------------------------------------------------------------------

    def test_1check_password(self):
        self.assertTrue(i.password_output())

    def test_2check_password(self):
        self.assertTrue(i.password_output())
        
    def test_2check_password(self):
        self.assertTrue(i.password_output())
if __name__ == '__main__':
    unittest.main()