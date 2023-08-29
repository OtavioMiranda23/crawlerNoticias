from datetime import datetime, timedelta


def convertStringToDate(date, formatModel):

    parseDate = datetime.strptime(date, formatModel)
    return parseDate

def differenceCurrentDate(past):
    today = datetime.today()
    return today - past

a = convertStringToDate("2023-08-28", "%Y-%m-%d")
print(differenceCurrentDate(a) > timedelta(days=2))
    