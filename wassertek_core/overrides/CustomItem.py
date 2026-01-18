# custom_app/overrides/item.py
from erpnext.stock.doctype.item.item import Item # type: ignore
import frappe # type: ignore

class CustomItem(Item):
	def autoname(self):
		# Your custom logic here
		# Example: Setting name based on a custom field 'custom_item_prefix'

		company_name = frappe.get_all(
			"Company",
			order_by="creation asc",
			limit=1
		)[0].name
		company_doc = frappe.get_doc("Company", company_name)
		company_abbr = company_doc.name[:3].upper()


		item_group_abbr = frappe.db.get_value(
			"Item Group",
			self.item_group,
			"abbr"
		)

		item_group_abbr = frappe.db.get_value(
			"Item Type",
			self.custom_item_type,
			"abbr"
		)

		item_code = company_abbr + "-" + item_group_abbr + "-" + item_group_abbr + "-" + self.custom_specification

		if item_code:
			self.name = item_code
		else:
			super().autoname()
