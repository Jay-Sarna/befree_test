import frappe

def sales_invoice_validation(doc,method=None):
    if doc.grand_total > 50000:
        frappe.throw("Need Manager Approval for submitting invoice above 50000")