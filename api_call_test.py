from darksky import forecast
from datetime import date, timedelta

BOSTON = 42.3601, 71.0589

weekday = date.today()
with forecast('API_KEY', *BOSTON) as boston:
    print(boston.daily.summary, end='\n---\n')
    for day in boston.daily:
        day = dict(day = date.strftime(weekday, '%a'),
                   sum = day.summary,
                   tempMin = day.temperatureMin,
                   tempMax = day.temperatureMax
                   )
        print('{day}: {sum} Temp range: {tempMin} - {tempMax}'.format(**day))
        weekday += timedelta(days=1)
