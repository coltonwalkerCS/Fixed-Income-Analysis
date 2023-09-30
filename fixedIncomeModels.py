# Fixed income models


def macaulayDuration(face_value, num_years, coupon_payment_percent, curr_interest_rate):
    """ Given the face value, number of years, coupon percent and current interest rate calculate
        the macaulay duration for a given fixed-income asset (assumes inputs are based in years) """
    # Initialize
    pv_val_sum = 0
    pv_weighted_val_sum = 0
    coupon_payment = face_value * coupon_payment_percent

    for time in range(1, num_years+1):
        # Final coupon payment includes face value
        pv_curr_val = ((coupon_payment + face_value) / pow((1 + curr_interest_rate), time) if time == num_years
                       else coupon_payment / pow((1 + curr_interest_rate), time))
        pv_val_sum += pv_curr_val
        pv_weighted_val_sum += pv_curr_val * time

    return round((pv_weighted_val_sum / pv_val_sum), 2)


def modifiedDuration(face_value, num_years, coupon_payment_percent, curr_interest_rate, compound_frequency):
    macD = macaulayDuration(face_value, num_years, coupon_payment_percent, curr_interest_rate)
    return round(macD / (1 + curr_interest_rate / compound_frequency), 2)
