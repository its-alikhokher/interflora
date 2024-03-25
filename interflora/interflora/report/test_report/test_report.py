import frappe


def execute(filters=None):
    columns, data = get_columns(filters), get_data(filters)
    return columns, data

def get_columns(filters):
    columns = [
        {
            "label": "Name",
            "fieldname": "name1",
            "fieldtype": "Data",
            "width": 250,
		},
        {
            "label": "Phone",
            "fieldname": "phone",
            "fieldtype": "Data",
            "width": 250,
		},
        {
            "label": "Email",
            "fieldname": "email",
            "fieldtype": "Data",
            "width": 250,
		},
	]
    return columns

def get_data(filters):
    data = []
    if filters.get('name'):
          filters['name1'] = filters.get('name')
    docs = frappe.get_all("Order Request",filters,"*")
    for row in docs:
        data.append({
            "name1":row.name1,
            "phone":row.phone, 
            "email":row.email,
        })
    return data 