import unittest
import returnIntegralsDev as retint
from returnIntegralsDev import workupODNP
from os import getcwd
from pyspecdata.nmr import *
from helper import *


class TestNMR(unittest.TestCase):
    """test cases for nmr.py"""
    def setUp(self):
        self.filename = getcwd()+"/test/in/180329_HttQ25_30R1_22C_ODNP_3/1"

    def tearDown(self):
        pass

    def test_det_type(self):
        filetype, twod = det_type(self.filename)
        self.assertEqual(filetype, 'bruker')
        self.assertFalse(twod)

    def test_bruker_det_phcorr(self):
        v = read_obj_from_json(getcwd()+"/test/in/v.json")
        arr = bruker_det_phcorr(v)
        self.assertEqual(len(arr), 1)
        self.assertEqual(arr[0], 44)


class TestWorkupODNP(unittest.TestCase):

    def setUp(self):
        cwd = getcwd()
        self.wo = workupODNP()
        self.wo.DataDir = cwd + "/test/in"
        self.wo.ODNPFile= cwd + "/test/in/180329_HttQ25_30R1_22C_ODNP_3"

    def tearDown(self):
        pass

    def disabled_test_determine_exp_type(self):
        self.wo.determine_exp_type()
        self.assertEqual(self.wo.setType, 'dnpExp')
        with self.assertRaises(ValueError):
            workupODNP().determine_exp_type()

    def disabled_test_return_exp_numbers(self):
        self.wo.determine_exp_type()
        exp_titles, dnp_exp_nums, t1_exp_nums = self.wo.return_exp_numbers()
        self.assertNotEqual(dnp_exp_nums, [])
        self.assertNotEqual(t1_exp_nums, [])

    def disabled_test_return_exp_params_dict(self):
        self.wo.determine_exp_type()
        self.wo.set_exp_numbers()
        self.wo.returnExpParamsDict()

    def disabled_test_returnExpTimes(self):
        self.disabled_test_return_exp_params_dict()
        exp_times, exp_time_min, abs_time = returnExpTimes(
            self.wo.expPath, self.wo.dnpExps, dnpExp=True,
            operatingSys=self.wo.systemOpt)


if __name__ == '__main__':
    unittest.main()