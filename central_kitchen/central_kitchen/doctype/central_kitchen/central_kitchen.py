# Copyright (c) 2022, sammish and contributors
# For license information, please see license.txt

import frappe
import numpy as np
import time
from frappe.model.document import Document
from frappe.model.mapper import get_mapped_doc
class CentralKitchen(Document):
	@frappe.whitelist()
	def get_item(self):
		data=frappe.db.sql("""select * from `tabBOM Operation` where parent=%s """,self.bom,as_dict=1)
		if data:
			self.set('operations_items', [])
			for i in data:
				self.append('operations_items',{
					"operation":i.operation,
					"workstation":i.workstation
				})
