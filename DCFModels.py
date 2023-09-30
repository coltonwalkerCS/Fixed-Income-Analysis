# Discounted cash flow models

def singlePeriodDCFModel(CF, discount_rate, time_period):
    discountedCF = CF / pow((1 + discount_rate), time_period)
    return round(discountedCF, 2)


def multiPeriodDCFModel(CF, discount_rate):
    discountedCF = 0
    for i in range(0, len(CF)):
        discountedCF += CF[i] / pow((1 + discount_rate), i + 1)
    return round(discountedCF, 2)
