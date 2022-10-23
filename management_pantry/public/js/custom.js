
$(document).bind('toolbar_setup', function() {
	frappe.app.name = "bdoop Erp";
	$('.navbar-home').html(frappe._('SIMAsset'));
	$('.navbar-home').attr("style", "color: white")

});
