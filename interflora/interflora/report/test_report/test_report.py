import frappe


def execute(filters=None):
    columns, data = get_columns(filters), get_data(filters)
    return columns, data

def get_columns(filters):
    columns = [
        {
            "fieldname":"docname",
            "label":("Sales"),
            "fieldtype": "Link",
            "options" : "Sales Order",
           "width":250
        },
         {
            "fieldname":"docname",
            "label":("Sales"),
            "fieldtype": "Link",
            "options" : "Order Request",
           "width":250
        },
      
	]
    return columns

def get_data(filters):
    data = []
    my_filter = {}
    if filters.get("from_date") and filters.get("to_date"):
        my_filter['creation']=['between', [filters.get("from_date"),filters.get("to_date")]]
    if filters.get("urgent"):
        my_filter['urgent_delivery'] = filters.get("urgent") 
    if filters.get("type"):
        my_filter['gift_wrapping'] = filters.get("type") 
    if filters.get("btype"):
        my_filter['bouquet_type'] = filters.get("btype") 
    # frappe.msgprint(f"{my_filter}")
    docs = frappe.get_all("Sales Order",my_filter)
    for row in docs:
        data.append({
            "docname":row.name,   
        })
        # frappe.msgprint(f"{data}")


    return data   

def get_data(filters):
    data1 = []
    my_filter = {}
    if filters.get("from_date") and filters.get("to_date"):
        my_filter['creation']=['between', [filters.get("from_date"),filters.get("to_date")]]
    if filters.get("urgent"):
        my_filter['urgent_delivery'] = filters.get("urgent") 
    if filters.get("type"):
        my_filter['gift_wrapping'] = filters.get("type") 
    if filters.get("btype"):
        my_filter['bouquet_type'] = filters.get("btype") 
    # frappe.msgprint(f"{my_filter}")
    docs = frappe.get_all("Order Request",my_filter)
    for row in docs:
        data1.append({
            "docname":row.name,   
        })
        # frappe.msgprint(f"{data}")
    return data1  