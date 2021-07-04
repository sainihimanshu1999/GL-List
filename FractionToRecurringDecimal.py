'''It's little tricky question but can be solved using divmod'''


def recurringDecimal(numerator,denominator):
    quo,rem = divmod(abs(numerator),abs(denominator))
    sign = '-' if numerator*denominator<0 else ''
    remainders = {}
    result = [sign+str(quo),'.']

    while rem>0 and rem not in remainders:
        remainders[rem] = len(result)
        quo,rem = divmod(abs(rem)*10,abs(denominator))
        result.append(quo)


    if rem in remainders:
        index = remainders[rem]
        result.insert(index,'(')
        result.append(')')

    return ''.join(result).rstrip('.')