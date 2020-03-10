import pickle

import pandas as pd



data_type = 'scna'
descriptor = 'scna'

actual_f = f'/Users/anna/PycharmProjects/protrack-hnsc/data/actual/{data_type}.pkl'
color_f = f'/Users/anna/PycharmProjects/protrack-hnsc/data/color/{data_type}.pkl'
actual = pickle.load(open(actual_f, 'rb'))
color = pickle.load(open(color_f, 'rb'))

if 'Data type' in actual.columns:
    actual = actual.fillna('NaN')
    actual['Data type'] = descriptor

    color.index = [f'{g} {descriptor}' for g in actual['Gene symbol']]
    actual.index = [f'{g} {descriptor}' for g in actual['Gene symbol']]

    columns = ['Data type', 'Gene symbol'] + list(actual.columns[:-2])

    actual = actual[columns]

    pickle.dump(actual, open(actual_f, 'wb'))
    pickle.dump(color, open(color_f, 'wb'))
    print(f'finished: {actual_f}')
    print(f'finished: {color_f}')
    print('EXIT EARLY')
else:
    actual = actual.fillna('NaN')
    actual['Gene symbol'] = list(actual.index)
    actual['Data type'] = descriptor

    color.index = [f'{g} {descriptor}' for g in actual['Gene symbol']]
    actual.index = [f'{g} {descriptor}' for g in actual['Gene symbol']]

    columns = ['Data type', 'Gene symbol'] + list(actual.columns[:-2])

    actual = actual[columns]

    pickle.dump(actual, open(actual_f, 'wb'))
    pickle.dump(color, open(color_f, 'wb'))
    print(f'finished: {actual_f}')
    print(f'finished: {color_f}')