from collections import OrderedDict


DEFINED_DICT = dict()
DEFINED_DICT['SUCCESS_CODE'] = OrderedDict((('code', 200), ('message', 'success'), ('result', None)))
DEFINED_DICT['ERROR_CODE'] = OrderedDict((('code', 404), ('message', 'fail'), ('result', None)))