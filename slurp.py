import requests
import time
from datetime import datetime


while True:
    r= requests.get("http://www.nyc.gov/html/tlc/downloads/excel/nys_dmv_revoked_suspended_drivers_licenses.xls")
    with open(datetime.now().strftime("%Y%m%d")+"suspended.xls","wb") as f:
        f.write(r.content)
    time.sleep(86400)
