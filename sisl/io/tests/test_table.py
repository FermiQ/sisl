from __future__ import print_function, division

import pytest

import os
import numpy as np

from sisl.io.table import *


import common as tc

_C = type('Temporary', (object, ), {})

join = os.path.join


def setup_module(module):
    tc.setup(module._C)


def teardown_module(module):
    tc.teardown(module._C)


@pytest.mark.io
class TestTable(object):

    def test_tbl1(self):
        dat0 = np.arange(2)
        dat1 = np.arange(2) + 1

        io0 = TableSile(join(_C.d, 't0.dat'), 'w')
        io1 = TableSile(join(_C.d, 't1.dat'), 'w')
        io0.write_data(dat0, dat1)
        io1.write_data((dat0, dat1))

        F0 = open(io0.file).readlines()
        F1 = open(io1.file).readlines()
        assert all([l0 == l1 for l0, l1 in zip(F0, F1)])

        os.remove(io0.file)
        os.remove(io1.file)

    def test_tbl2(self):
        dat0 = np.arange(8).reshape(2, 2, 2)
        dat1 = np.arange(8).reshape(2, 2, 2) + 1

        io0 = TableSile(join(_C.d, 't0.dat'), 'w')
        io1 = TableSile(join(_C.d, 't1.dat'), 'w')
        io0.write_data(dat0, dat1)
        io1.write_data((dat0, dat1))

        F0 = open(io0.file).readlines()
        F1 = open(io1.file).readlines()
        assert all([l0 == l1 for l0, l1 in zip(F0, F1)])

        os.remove(io0.file)
        os.remove(io1.file)
