from mpt.single_sums import get_future_value_sum_with_present_value, get_future_sum_with_payments


def test_get_future_value_present_sum():
    present_value = 100.00
    interest_rate = 0.03
    periods = 4
    compounding = 1
    
    actual_future_value = get_future_value_sum_with_present_value(present_value,
                                                                  interest_rate,
                                                                  periods,
                                                                  compounding)
    expect_future_value = 112.55
    assert (actual_future_value == expect_future_value)


def test_get_future_sum_with_payments():
    payment_amount = 2000.00
    interest_rate = 0.08
    periods = 18
    compounding = 1

    actual_future_sum_with_payments = get_future_sum_with_payments(payment_amount,
                                                                   interest_rate,
                                                                   periods,
                                                                   compounding)
    expect_future_sum_with_payments = 74900.49

    assert (actual_future_sum_with_payments == expect_future_sum_with_payments)
