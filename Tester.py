import unittest
import returnIntegralsDev as retint
from returnIntegralsDev import workupODNP


class TestWorkupODNP(unittest.TestCase):

    def setUp(self):
        self.wo = workupODNP()
        self.wo.DataDir = "/Users/yanxlin/github/workupsoftware/test/in"
        self.wo.ODNPFile= "/Users/yanxlin/github/workupsoftware/test/in/" \
                          "180329_HttQ25_30R1_22C_ODNP_3"
        pass

    def tearDown(self):
        pass

    def test_determine_exp_type(self):
        self.wo.determine_exp_type()
        self.assertEqual(self.wo.setType, 'dnpExp')
        with self.assertRaises(ValueError):
            workupODNP().determine_exp_type()
        pass


if __name__ == '__main__':
    unittest.main()