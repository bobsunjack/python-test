import pandas as pd
import pytz as lc

stamp=pd.Timestamp('2012-09-09 12:12')
stamp_utc=stamp.tz_localize('utc')

stamp_utc.tz_convert('America/New_York')
print(stamp_utc)

now=pd.Timestamp.now()
print(now)
print(lc.common_timezones)