
$(document).bind('toolbar_setup', function() {
	frappe.app.name = "bdoop Erp";
	$('.navbar-home').html(frappe._('DIAS'));
	$('.navbar-home').attr("style", "color: white")

});
