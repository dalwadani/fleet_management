# Copyright (c) 2013, Dar Nazer Est. and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.model.document import Document

class VehicleOdometerLog(Document):
        def on_submit(self):
                last_reading = frappe.get_list("Vehicle",
                                               fields=["odometer_reading", "reading_time"],
                                               filters = {
                                                       "name": self.vehicle
                                               })
                if (self.reading_time >= last_reading[0].reading_time):
                        frappe.set_value("Vehicle",self.vehicle,"odometer_reading", self.odometer_reading)
                        frappe.set_value("Vehicle",self.vehicle,"reading_time", self.reading_time)
