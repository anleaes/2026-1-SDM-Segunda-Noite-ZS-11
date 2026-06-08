from decimal import Decimal, InvalidOperation


def only_digits(value):
    if value is None:
        return ""

    return "".join(char for char in str(value) if char.isdigit())


def mask_cpf_cnpj(value):
    digits = only_digits(value)

    if len(digits) == 11:
        return f"{digits[:3]}.{digits[3:6]}.{digits[6:9]}-{digits[9:]}"

    if len(digits) == 14:
        return f"{digits[:2]}.{digits[2:5]}.{digits[5:8]}/{digits[8:12]}-{digits[12:]}"

    return value


def mask_phone(value):
    digits = only_digits(value)

    if len(digits) == 10:
        return f"({digits[:2]}) {digits[2:6]}-{digits[6:]}"

    if len(digits) == 11:
        return f"({digits[:2]}) {digits[2:7]}-{digits[7:]}"

    if len(digits) == 13 and digits.startswith("55"):
        return f"+{digits[:2]} ({digits[2:4]}) {digits[4:9]}-{digits[9:]}"

    return value


def format_currency(value):
    if value is None:
        return None

    try:
        amount = Decimal(value)
    except (InvalidOperation, TypeError, ValueError):
        return value

    formatted = f"{amount:,.2f}"
    formatted = formatted.replace(",", "X").replace(".", ",").replace("X", ".")
    return f"R$ {formatted}"


def format_date(value):
    if value is None:
        return None

    return value.strftime("%d/%m/%Y")
