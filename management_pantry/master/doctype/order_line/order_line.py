# Copyright (c) 2022, Prabunesia Teknologi and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document

class OrderLine(Document):
    def before_save(self):
        self.sub_total = self.quantity * self.price

