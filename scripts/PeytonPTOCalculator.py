from datetime import datetime
from datetime import timedelta
from dateutil.relativedelta import relativedelta


def addHoliday(holidays, date):
    holidays.append(datetime.strptime(date, "%m-%d-%Y"))


def addVacation(vacationDates, date1, date2):
    vacationDates.append((datetime.strptime(date1, "%m-%d-%Y"), datetime.strptime(date2, "%m-%d-%Y")))


def main():
    # Setup variables
    accrualPerPeriod = 10
    startingPTO = 48  # MUST BE TOTAL AS OF THE WEEK BEFORE THE BEGIN DATE
    beginDate = datetime.strptime("02-18-2024", "%m-%d-%Y")  # NEEDS TO BE A PTO DAY
    endDate = datetime.strptime("01-18-2025", "%m-%d-%Y")    # NEEDS TO BE A PTO DAY
    canTakeVacation = True
    date1 = beginDate
    date2 = endDate
    totalPTO = startingPTO
    holidays = []
    vacationDates = []
    delta = timedelta(days=1)
    payPeriodDelta = relativedelta(months=1)

    # Setup holidays
    addHoliday(holidays, "05-27-2024")
    addHoliday(holidays, "07-04-2024")
    addHoliday(holidays, "07-05-2024")
    addHoliday(holidays, "09-02-2024")
    addHoliday(holidays, "11-28-2024")
    addHoliday(holidays, "11-29-2024")
    addHoliday(holidays, "12-23-2024")
    addHoliday(holidays, "12-24-2024")
    addHoliday(holidays, "12-25-2024")

    # Setup vacations
    addVacation(vacationDates, "03-09-2024", "03-16-2024")
    addVacation(vacationDates, "06-17-2024", "06-21-2024")
    addVacation(vacationDates, "09-06-2024", "09-09-2024")
    addVacation(vacationDates, "09-26-2024", "09-30-2024")
    addVacation(vacationDates, "11-27-2024", "12-02-2024")
    addVacation(vacationDates, "12-24-2024", "12-28-2024")

    # Get list of every day in between beginDate and endDate (inclusive)
    allDates = []
    while date1 <= date2:
        allDates.append(date1)
        date1 += delta

    # Get list of every vacation day (inclusive, no weekends)
    allVacationDates = []
    for x in vacationDates:
        date1 = x[0]
        date2 = x[1]
        while date1 <= date2:
            if date1.weekday() != 5 and date1.weekday() != 6:
                allVacationDates.append(date1)
            date1 += delta
    date1 = beginDate
    date2 = endDate

    # Analyze each pay period
    while date1 <= (date2 - delta):
        totalPTO += accrualPerPeriod
        beginIndex = allDates.index(date1)
        endIndex = allDates.index(date1 + payPeriodDelta)
        payPeriodDates = allDates[beginIndex:endIndex]

        # Calculate how many vacation days are taken this pay period
        vacationDayCount = 0
        for x in payPeriodDates:
            if (x in allVacationDates) and (x not in holidays):
                vacationDayCount += 1

        # Determine how much PTO remains
        totalPTO -= (vacationDayCount * 8)
        if totalPTO < 0:
            canTakeVacation = False

        # Print current status
        if vacationDayCount > 0:
            print(
                str(date1.date()) + " - " + str((date1 + payPeriodDelta - delta).date()) + ": " + str("{:.3f}".format(totalPTO)) + " hours - " + str(vacationDayCount) + " day(s) / " + str(vacationDayCount*8) + " hours off")
        else:
            print(str(date1.date()) + " - " + str((date1 + payPeriodDelta - delta).date()) + ": " + str("{:.3f}".format(totalPTO)) + " hours")
        date1 += payPeriodDelta

    # Print final result
    if canTakeVacation:
        print("You can take all your vacation days! :)")
    else:
        print("You cannot take all your vacation days. :(")


main()
