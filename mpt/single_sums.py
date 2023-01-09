

def get_future_value_sum_with_present_value(amount: float, interest_rate: float, periods: int, compounding=12, precision=2):
    return round(amount * (1 + interest_rate)**(periods * compounding), precision)


def get_future_sum_with_payments(payment_amount: float, interest_rate: float, periods: int, compounding=12, precision=2):
    return round(payment_amount * (((1 + interest_rate)**(periods * compounding) - 1) / interest_rate), precision)
