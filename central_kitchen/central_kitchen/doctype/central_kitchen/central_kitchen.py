# Copyright (c) 2022, sammish and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document
from frappe.model.mapper import get_mapped_doc
class CentralKitchen(Document):
	@frappe.whitelist()
	def get_item(self):
		data=frappe.db.sql("""select * from `tabBOM Operation` where parent=%s """,self.bom,as_dict=1)
		if data:
			self.set('operations', [])
			for raw in data:
				self.append('operations',{
					"operation":raw.operation,
					"workstation":raw.workstation,
					"time_in_mins":raw.time_in_mins,
					"operating_cost":raw.operating_cost,
					"fixed_time":raw.fixed_time
				})
		f_good_data=data=frappe.db.sql("""select * from `tabBOM` where name=%s """,self.bom,as_dict=1)
		if f_good_data:
			self.set('finished_goods', [])
			for i in f_good_data:
				self.append('finished_goods',{
					"item_name":i.item_name,
					"uom":i.uom,
					"production_qty":i.quantity
				})
		r_good_data=data=frappe.db.sql("""select * from `tabBOM Explosion Item` where parent=%s """,self.bom,as_dict=1)
		if r_good_data:
			self.set('bom_materials', [])
			for i in r_good_data:
				self.append('bom_materials',{
					"item_code":i.item_code,
					"qty":i.stock_qty,
					"uom":i.stock_uom,
					"rate":i.rate,
					"amount":i.amount
				})

	
