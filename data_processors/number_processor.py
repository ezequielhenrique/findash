def format_num(num):
    if num >= 1000000000:
        return f'{round(num / 1000000000, 1)} B'
    elif num >= 1000000:
        return f'{round(num / 1000000, 1)} M'
    else:
        return f'{num:,.1f}'
