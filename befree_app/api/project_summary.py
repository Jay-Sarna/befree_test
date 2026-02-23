import frappe

@frappe.whitelist(allow_guest=True)
def project_summary(proj):
    if proj:
        try:
            project_time = frappe.db.get_value('Project',proj,'actual_time')
            task_count = frappe.db.count('Task',{"project":proj})
            frappe.response.messege = f"Project Summary: Time taken so far:{project_time} , Task count {task_count}"
        except Exception as e:
            frappe.log_error('Project_summary_api_error',e)
            frappe.response.error=f"Project Not Found"