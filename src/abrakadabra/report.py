from datetime import date, datetime


def report():
    week = date.isocalender(datetime.now())
    print("Weekly report %s" % week)
