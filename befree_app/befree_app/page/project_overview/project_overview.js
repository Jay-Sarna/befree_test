frappe.pages['project-overview'].on_page_load = function(wrapper) {
	var page = frappe.ui.make_app_page({
		parent: wrapper,
		title: 'Project overview',
		single_column: true
	});
	page.add_field({
		fieldname:'project',
		label:'project',
		options:'Project',
		fieldtype:'Link'
	})
	console.log()
}