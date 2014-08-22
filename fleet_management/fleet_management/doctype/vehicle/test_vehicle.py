# Copyright (c) 2013, Dar Nazer Est. and Contributors
# See license.txt

import frappe
import unittest

test_records = frappe.get_test_records('Vehicle')

class TestVehicle(unittest.TestCase):
	pass
