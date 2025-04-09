import json

def person_id(wp_user_id):
    match wp_user_id:
        case 2991:
            return 903617
        case 31:
            return 900508
        case 1720:
            return 902139
        case 2427:
            return 902991
        case 98:
            return 900576
        case 4364:
            return 905035
        case 1715:
            return 902030
        case _:
            return 0
        
with open("wp_postmeta3.json") as log:
    data = json.load(log)

output_log = open("admin_log.json", "w", encoding="utf-8")
admins = []

for i in data:
    if "is_admin" in i:
        if i["is_admin"] == True:
            if i["wp_user_id"] not in admins:
                print(i["wp_user_id"])
                admins.append(i["wp_user_id"])
            record = {"event_date": i["create_date"], "person_id": person_id(i["wp_user_id"]), "product_id": i["product_id"], "new_stock_quantity": i["qty"], "event_type": "67edc94c76be1"}
            json.dump(record, output_log, ensure_ascii=False, indent=4)

output_log.close()

# admins_list = open("admin_list.txt", "w", encoding="utf-8")
# for a in admins:
#     admins_list.write(a)
# admins_list.close()