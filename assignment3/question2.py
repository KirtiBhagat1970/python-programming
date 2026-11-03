
lines = [
    ' asha VERMA ; ASHA.V@Example.COM ; +91 98765-43210 ;pune ',
    'ravi kumar;ravi@@corp.in;9123456780;Mumbai',
    'meera;meera@mail;9123456780;Delhi',
    'john doe; john@x.org ;12345; Goa',
    'Neha Rao;neha.rao@firm.co.in;919876501234;nashik',
    'amit;amit@site.com;9876543210'
]


def clean_customer(raw):
    column_info = raw.split(';')

    if len(column_info) != 4:
        return None

    name = column_info[0].strip()
    email = column_info[1].strip().lower()
    phone = column_info[2].strip()
    city = column_info[3].strip()

    # Validate name
    if name == "":
        return None

    words = name.split()

    for word in words:
        if not word.isalpha():
            return None

    name = name.title()

    # Validate city
    if city == "":
        return None

    city = city.title()

    # Validate email
    if email.count('@') != 1:
        return None

    user, domain = email.split('@')

    if user == "":
        return None

    if '.' not in domain:
        return None

    if domain.startswith('.') or domain.endswith('.'):
        return None

    # Validate phone
    phone = phone.replace(" ", "")
    phone = phone.replace("-", "")

    if phone.startswith("+91"):
        phone = phone[3:]

    elif len(phone) == 12 and phone.startswith("91"):
        phone = phone[2:]

    if len(phone) != 10:
        return None

    if not phone.isdigit():
        return None

    if phone[0] not in "6789":
        return None

    # Return cleaned customer details
    return {
        "name": name,
        "email": email,
        "phone": phone,
        "city": city
    }


# Process all records
rejected = 0

for record in lines:
    customer = clean_customer(record)

    if customer:
        print(customer)
    else:
        rejected += 1

print("Rejected:", rejected)
