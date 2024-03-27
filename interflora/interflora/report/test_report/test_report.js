// Copyright (c) 2024, nextash and contributors
// For license information, please see license.txt
/* eslint-disable */

frappe.query_reports["Test Report"] = {
	"filters": [
		{
			"fieldname":"from_date",
			"label": __("From Date"),
			"fieldtype": "Date"
		},
		{
			"fieldname":"to_date",
			"label": __("To Date"),
			"fieldtype": "Date"
		},
		{
			"fieldname":"urgent",
			"label": __("Urgent Delivery"),
			"fieldtype": "Check"
		},
		{
			"fieldname":"type",
			"label": __("Gift Type"),
			"fieldtype": "Select",
			"options" : "\nBox\nPacket"
		},
		{
			"fieldname":"btype",
			"label": __("Bouquet Type"),
			"fieldtype": "Select",
			"options" : "\nRed\nGreen"
		},
		{
			"fieldname":"email",
			"label": __("Email"),
			"fieldtype": "Data"
		},
		{
			"fieldname":"phone",
			"label": __("Phone"),
			"fieldtype": "Data"
		},
	]
};
