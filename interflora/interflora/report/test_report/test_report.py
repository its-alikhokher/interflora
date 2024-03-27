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
            "fieldname":"order_request",
            "label":("Order Request"),
            "fieldtype": "Link",
            "options" : "Order Request",
           "width":250
        },
         {
            "fieldname":"price",
            "label":("Price"),
            "fieldtype": "currency",
           "width":100
        },
        {
            "fieldname":"email",
            "label":("Email"),
            "fieldtype": "currency",
           "width":150
        },
        {
            "fieldname":"phone",
            "label":("Phone"),
            "fieldtype": "currency",
           "width":150
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
    if filters.get("email"):
        my_filter['email'] = filters.get("email")
    if filters.get("phone"):
        my_filter['phone'] = filters.get("phone")
     
     
    # frappe.msgprint(f"{my_filter}")
    sales_order_docs = frappe.get_all("Sales Order", my_filter, ["*"])
    for row in sales_order_docs:
        data.append({"docname": row.name,
                     "order_request": row.order_request,
                     "price": row.price,
                     "email": row.email,
                     "phone": row.phone
                     })
    return data 