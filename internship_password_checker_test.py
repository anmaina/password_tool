import unittest
import internship_password_checker as i
import string

class TestStringMethods(unittest.TestCase):

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
#-------------------------------------------------------------------
    def test_1check_password_for_rules(self):
        expected_result = ' - The password must be at least 14 characters long'
        actual_result = i.rule_checker([True, True, True, False])
        self.assertEqual(actual_result, expected_result)

    def test_2check_rule_cheker(self):
        expected_result = ' - The password must contain at least one punctuation character ({})'.format(string.punctuation)
        actual_result = i.rule_checker([True, True, False, True])
        self.assertEqual(actual_result, expected_result)
    
    def test_3check_rule_cheker(self):
        expected_result = ' - The password must contain both lowercase and uppercase characters'
        actual_result = i.rule_checker([True, False, True, True])
        self.assertEqual(actual_result, expected_result)
    
    def test_4check_rule_cheker(self):
        expected_result = ' - The password must contain at least one digit'
        actual_result = i.rule_checker([False, True, True, True])
        self.assertEqual(actual_result, expected_result)

    def test_5check_rule_cheker(self):
        expected_result = ' - The password must contain at least one digit' +'\n' + ' - The password must contain both lowercase and uppercase characters'
        actual_result = i.rule_checker([False, False, True, True])
        self.assertEqual(actual_result, expected_result)   
    
    def test_6check_rule_cheker(self):
        expected_result = ' - The password must contain at least one digit' +'\n' + ' - The password must contain both lowercase and uppercase characters'
        actual_result = i.rule_checker([False, False, False, False])
        self.assertNotEqual(actual_result, expected_result) 

#-----------------------------------------------------------------------------------------------
    # def test_2check_rule_cheker(self):
    #     expected_result = 'Strong password'
    #     list_of_function_call = [True, True, True, True]
    #     actual_result = i.rule_checker('kjKJjsidnfmncu***45yde98')
    #     self.assertEqual(actual_result, expected_result)
if __name__ == '__main__':
    unittest.main()