import requests
import time
from datetime import datetime
import dropbox

app_key = 'INSERT_APP_KEY'
app_secret = 'INSERT_APP_SECRET'

flow = dropbox.client.DropboxOAuth2FlowNoRedirect(app_key, app_secret)
authorize_url = flow.start()
code = raw_input("Enter the authorization code here: ").strip()
access_token, user_id = flow.finish(code)

client = dropbox.client.DropboxClient(access_token)
print 'linked account: ', client.account_info()

while True:
    r= requests.get("http://www.nyc.gov/html/tlc/downloads/excel/nys_dmv_revoked_suspended_drivers_licenses.xls")
    filename = datetime.now().strftime("%Y%m%d")+"suspended.xls"
    with open(filename,"wb") as f:
        client.put_file(filename,f)
    print "uploaded:", filename
    time.sleep(86400)
