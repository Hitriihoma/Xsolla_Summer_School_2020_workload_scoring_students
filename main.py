from google.oauth2 import service_account
import lib_main

CREDENTIALS = 'put here'

DataFrame = lib_main.getFreshData(CREDENTIALS,'findcsystem')

print('enter insert_if_exists type: 1 for append, 2 for replace, 3 for fail')
ie = input()

if ie == 1:
    IfExists = 'append'
elif ie == 2:
    IfExists = 'replace'
elif ie == 3:
    IfExists = 'fail'
else:
    IfExists = 'fail'

DatePeriod = int(63)
DateSep = int(7)

try:
    a = lib_main.workloadAllAssignees(DataFrame,DatePeriod,DateSep)
    b = lib_main.workloadAllAssigneesStatusesChannelsTotal(DataFrame,DatePeriod,DateSep)
    c = lib_main.workloadAllAssigneesStatusesChannels(DataFrame,DatePeriod,DateSep)
except:
    print('Error: check credentials')


lib_main.insertScoreResultData(a,'findcsystem','xsolla_summer_school','score_result_status',IfExists)    
lib_main.insertScoreResultDataTotal(b,'findcsystem','xsolla_summer_school','score_result_total',IfExists)
lib_main.insertScoreResultDataStatusesAndChannels(c,'findcsystem','xsolla_summer_school','score_result_status_and_channels', IfExists)
