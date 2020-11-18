from decimal import Decimal, ROUND_HALF_UP

deg, dis = map(int, input().split())

def direction(deg):
    if 0 <= deg < 112.5:
        return 'N'
    elif deg < 337.5:
        return 'NNE'
    elif deg < 562.5:
        return 'NE'
    elif deg < 787.5:
        return 'ENE'
    elif deg < 1012.5:
        return 'E'
    elif deg < 1237.5:
        return 'ESE'
    elif deg < 1462.5:
        return 'SE'
    elif deg < 1687.5:
        return 'SSE'
    elif deg < 1912.5:
        return 'S'
    elif deg < 2137.5:
        return 'SSW'
    elif deg < 2362.5:
        return 'SW'
    elif deg < 2587.5:
        return 'WSW'
    elif deg < 2812.5:
        return 'W'
    elif deg < 3037.5:
        return 'WNW'
    elif deg < 3262.5:
        return 'NW'
    elif deg < 3487.5:
        return 'NNW'
    else:
        return 'N'

def wind(dis):
    if Decimal('0.0') <= dis <= Decimal('0.2'):
        return 0
    elif dis <= Decimal('1.5'):
        return 1
    elif dis <= Decimal('3.3'):
        return 2
    elif dis <= Decimal('5.4'):
        return 3
    elif dis <= Decimal('7.9'):
        return 4
    elif dis <= Decimal('10.7'):
        return 5
    elif dis <= Decimal('13.8'):
        return 6
    elif dis <= Decimal('17.1'):
        return 7
    elif dis <= Decimal('20.7'):
        return 8
    elif dis <= Decimal('24.4'):
        return 9
    elif dis <= Decimal('28.4'):
        return 10
    elif dis <= Decimal('32.6'):
        return 11
    elif dis >= Decimal('32.7'):
        return 12

dis = Decimal(str(dis))/Decimal('60')
dis = Decimal(dis.quantize(Decimal('0.1'), rounding=ROUND_HALF_UP))
dis = wind(dis)

if dis==0:
    print('C', dis)
else:
    print(direction(deg), dis)
