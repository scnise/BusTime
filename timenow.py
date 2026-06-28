from datetime import datetime
def now():
    now = datetime.now()
    time_date = now.strftime("%H:%M:%S %d.%m.%Y")
    return time_date