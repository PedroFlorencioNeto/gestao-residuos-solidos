import locale
import calendar
from datetime import datetime

# Definição de local para definição de datas em português
locale.setlocale(locale.LC_ALL, 'pt_BR.utf8')

def get_current_month():
    '''
    Function that gets the name of current month.
    Args: no args required
    Returns: current month: str
    '''
    current_month_number = datetime.now().month
    current_month_name = calendar.month_name[current_month_number]
    current_month_name = current_month_name.title()

    return current_month_name
