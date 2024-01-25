from datetime import datetime, date, timedelta
from decimal import Decimal
goods = {'Хлеб': [
        {'amount': Decimal('1'), 'expiration_date': None},
        {'amount': Decimal('1'), 'expiration_date': date(2024, 1, 22)}
    ],
    'Яйца': [
        {'amount': Decimal('2'), 'expiration_date': date(2024, 1, 24)},
        {'amount': Decimal('3'), 'expiration_date': date(2024, 1, 25)}
    ],
    'Вода': [{'amount': Decimal('100'), 'expiration_date': None}]}
DATE_FORMAT = '%Y-%m-%d'
def add(items, title, amount, expiration_date=None):
    new_prd = list()
    if expiration_date is not None:
        expiration_date = datetime.strptime(expiration_date, DATE_FORMAT)
        if title not in items:
            items[title] = new_prd
            sm_info = {'amount': amount, 'expiration_date': datetime.date(expiration_date)}
            list.append(new_prd, sm_info)
            goods[title] = new_prd
        else:
            items[title].append({'amount': Decimal(amount), 'expiration_date': datetime.date(expiration_date)})
    else:
        if title not in items:
            items[title] = new_prd
            sm_info = {'amount': amount, 'expiration_date': None}
            list.append(new_prd, sm_info)
            goods[title] = new_prd
        else:
            items[title].append({'amount': Decimal(amount), 'expiration_date': None})

def add_by_note(items, note):
    nts = str.split(note, ' ')
    if '-' in nts[-1]:
        ddate = nts[-1]
        dec = nts[-2]
        name_part = nts[:-2]
        name = ' '.join(name_part)
        add(items, name, dec, ddate)
    else:
        dec = nts[-1]
        name_part = nts[:-1]
        name = ' '.join(name_part)
        add(items, name, dec)

def find(items, needle):
    low = str.lower(needle)
    result = list()
    for kkey in items:
        low_kkey = str.lower(kkey)
        if low in low_kkey:
            list.append(result, kkey)
        elif low == kkey:
            list.append(result, kkey)
    return result

def amount(items, needle):
    total = Decimal(0)
    list_of_prd = find(items, needle)
    for keyy in list_of_prd:
        if keyy in items:
            f = items[keyy]
            for e in f:
                total += e['amount']
        else:
            total = Decimal(0)
    return total

def expire(items, in_advance_days=0):
    date_today = date.today()
    exp_date = date_today + timedelta(days=in_advance_days)
    final = list()
    for key in items:
        total = Decimal(0)
        for sub_list in items[key]:
            if sub_list['expiration_date'] is None:
                continue
            if exp_date >= sub_list['expiration_date']:
                total += sub_list['amount']
        if total > 0:
            final.append((key, total))
    return final




