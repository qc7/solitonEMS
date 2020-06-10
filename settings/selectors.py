from settings.models import Currency


def get_all_currencies():
    return Currency.objects.all()


def get_currency(currency_id):
    return Currency.objects.get(pk=currency_id)


def get_usd_currency():
    try:
        return Currency.objects.get(code="USD")
    except Currency.DoesNotExist:
        return None


def get_ugx_currency():
    try:
        return Currency.objects.get(code="UGX")
    except Currency.DoesNotExist:
        return None
