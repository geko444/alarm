from selenium import webdriver
from selenium.webdriver.support.ui import Select

def time_to_hhmm(time):
    if ':' in time:
        return [int(s) for s in time.split(':')]
    elif len(time) < 3:
        return [int(time), 0]
    else:
        return [int(time[:-2]), int(time[-2:])]

def hhmm_to_time(hhmm):
    return ':'.join([str(n) for n in hhmm])

def hhmm_to_mins(hhmm):
    return hhmm[0]*60 + hhmm[1]

def mins_to_hhmm(mins):
    return [mins//60, mins%60]

def time_to_mins(time):
    return hhmm_to_mins(time_to_hhmm(time))

def mins_to_time(mins):
    return hhmm_to_time(mins_to_hhmm(mins))

def hour_to_ampm(hour):
    assert hour < 24
    if hour == 0:
        return '12 AM'
    elif hour in range(1, 12):
        return str(hour) + ' AM'
    elif hour == 12:
        return '12 PM'
    else:
        return str(hour-12) + ' PM'

def mins_two_digits(mins):
    assert mins < 60
    if mins < 10:
        return '0' + str(mins)
    else:
        return str(mins)

def hhmm_to_ampm(hhmm):
    return [hour_to_ampm(hhmm[0]), mins_two_digits(hhmm[1])]

def mins_to_ampm(mins):
    return hhmm_to_ampm(mins_to_hhmm(mins))

def mins_range(start, end, step):
    return list(range(start, end, step)) + [end]

def time_range(start, end, step):
    mins = mins_range(time_to_mins(start), time_to_mins(end), step)
    return [mins_to_hhmm(min) for min in mins]

def load_clock():
    driver.execute_script("window.open('http://www.onlineclock.net');")
    window_after = driver.window_handles[-1]
    driver.switch_to.window(window_after)

def set_alarm(hhmm):
    hh, mm = [str(n) for n in hhmm]
    load_clock()
    hour = Select(driver.find_element_by_name('alarm_hour'))
    hour.select_by_value(hh)
    minute = Select(driver.find_element_by_name('alarm_minute'))
    minute.select_by_value(mm)

def set_alarms(start, end, step):
    for hhmm in time_range(start, end, step):
        set_alarm(hhmm)


def ask_user():
    start = input('Start? ')
    end = input('End? ')
    step = int(input('Step? '))
    return start, end, step

start, end, step = ask_user()

driver = webdriver.Chrome()
window = driver.window_handles[0]

set_alarms(start, end, step)
