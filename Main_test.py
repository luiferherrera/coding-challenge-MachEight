import unittest
from unittest import mock
from unittest.mock import patch

import Main as main

class test_Main(unittest.TestCase):

    def test_getData(self):
        self.assertIsInstance(main.getData(),list)
        self.assertEqual(len(main.getData()),435)
        for player in main.getData():
            self.assertIsInstance(player,dict)

    def test_validateNumber(self):
        self.assertEqual(main.validateNumber(139),139)
        self.assertEqual(main.validateNumber("139"),139)
        self.assertFalse(main.validateNumber("two"))
        self.assertFalse(main.validateNumber("1,39"))


    def test_algorithm(self):
        with mock.patch('sys.stdout') as fake_stdout:
            main.algorithm(main.getData(),2)
            fake_stdout.assert_has_calls([
                mock.call.write("No matches found"),
            ])

        with mock.patch('sys.stdout') as fake_stdout:
            main.algorithm(main.getData(),139)
            fake_stdout.assert_has_calls([
                mock.call.write("Brevin Knight         Nate Robinson"),
                mock.call.write('\n'),
                mock.call.write("Nate Robinson         Mike Wilks"),
                mock.call.write('\n'),
            ])

    def test_getData(self):
        with mock.patch('sys.stdout') as fake_stdout:
            main.getPairs(2)

        fake_stdout.assert_has_calls([
            mock.call.write("No matches found"),
        ])

        with mock.patch('sys.stdout') as fake_stdout:
            main.getPairs(139)

        fake_stdout.assert_has_calls([
            mock.call.write("Brevin Knight         Nate Robinson"),
            mock.call.write('\n'),
            mock.call.write("Nate Robinson         Mike Wilks"),
            mock.call.write('\n'),
        ])

if __name__=="__main__":
    unittest.main()