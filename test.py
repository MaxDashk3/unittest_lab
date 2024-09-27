import unittest
import lab as app


class Tests(unittest.TestCase):
    def setUp(self):
        self.app=app
        self.data ={ ('8-A','Soroka I.I.'):{'Math':[12, 10, 8, 9],
                                 'Ukr literature':[9, 7],
                                 'Chemistry':[6, 8, 7],
                                 'Physics':[11, 12, 11, 12],
                                 'PE':[10, 10, 10, 10]
                                 },
                ('8-A','Nikson A.V.'):{'Math':[12, 11, 10, 7],
                                 'Ukr literature':[10, 11],
                                 'Chemistry':[9, 8, 10],
                                 'Physics':[10, 10, 7, 6],
                                 'PE':[7, 8, 9, 10]
                                 },
               ('5-C','Kozak A.S.'):{'Math':[9, 10, 10, 10],
                                 'Ukr literature':[9, 10],
                                 'History':[6, 10, 11, 8],
                                 'English':[5, 12, 10, 11],
                                 'PE':[9, 8, 6, 4]
                                 },
               ('5-B','Moliga T.P.'):{'Math':[11, 11, 11, 10],
                                 'Ukr literature':[12, 10, 11],
                                 'History':[10, 10, 11, 12],
                                 'English':[11, 10, 12, 10, 11],
                                 'PE':[10, 10, 10, 10]
                                 },
               ('5-C','Vinnichenko D.R.'):{'Math':[10, 10, 10, 10],
                                 'Ukr literature':[11, 10],
                                 'History':[9, 10, 11, 12],
                                 'English':[11, 12, 7, 9, 10],
                                 'PE':[5, 5, 8, 9]
                                 }
        }

    def test_children_list(self):
        expected_data = ['Soroka I.I.','Nikson A.V.']
        retrieved_data = app.children_list(self.data, "8-A")
        self.assertEqual(retrieved_data, expected_data)

        self.assertEqual(app.children_list(self.data,"Some class"), [])


    def test_subject_best_children(self):
        expected_data = {'8': ['Soroka I.I.', 'Nikson A.V.'], '5': ['Moliga T.P.']}
        retrieved_data = app.subject_best_children(self.data, "Math")
        self.assertEqual(retrieved_data, expected_data)

        expected_data = {'8': ['Nikson A.V.']}
        retrieved_data = app.subject_best_children(self.data, "Chemistry")
        self.assertEqual(retrieved_data, expected_data)

        expected_data = {'8': ['Soroka I.I.','Nikson A.V.'], '5': ['Moliga T.P.']}
        retrieved_data = app.subject_best_children(self.data, "PE")
        self.assertEqual(retrieved_data, expected_data)

        self.assertEqual(app.subject_best_children(self.data, "Empty"), {})


if __name__ == '__main__':
    unittest.main()
