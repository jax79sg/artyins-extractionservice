import unittest

class TestModels(unittest.TestCase):

    def test_tikextractor(self):
        print("Running tikextractor")
        from extractors.tikextractor import TIKExtractor
        myextractor = TIKExtractor()
        
        results=myextractor.extract("test.pdf")
        print(results)

if __name__ == '__main__':
    unittest.main()
