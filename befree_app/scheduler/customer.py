import frappe

def send_welcome_message_to_new_customer():
    customer_list = frappe.db.get_all('Customer',filters={'creation':['>',frappe.utils.today()]},fields=['name',"email_id"])    
    if customer_list:
        customer_without_email = []
        for customer in customer_list:
            if customer.get("email_id"):
                frappe.sendmail(subject='Welcome to our company',recipients=customer.email_id,
                                message=f"Hellow {customer.customer_name} welcome")
            else:
                customer_without_email.append(customer.customer_name)

        frappe.log_error("Welcome_email_failed",f" Email address for {customer_without_email} not found")