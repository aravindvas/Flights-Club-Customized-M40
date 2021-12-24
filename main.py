from dmanager import DataManager
from flightsearch import Flight
from datetime import datetime, timedelta
from notify import Notification

dmgr = DataManager()
sht = dmgr.get_des_data()
fs = Flight()
notmgr = Notification()

org_city = "CCU"

if sht[0]["iataCode"] == "":
    for ct in sht:
        ct["iataCode"] = fs.get_des_code(ct["city"])
    dmgr.des_data = sht
    dmgr.upd_des_codes()
    # print(sht)

# tmr = datetime.now() + timedelta(days=34)
tmr = datetime(year=2021, month=7, day=14)
# sixmo = datetime.now() + timedelta(days=43)
sixmo = datetime(year=2021, month=7, day=18)

for des in sht:
    fl = fs.checkf(
        org_city_cd=org_city,
        des_city_cd=des["iataCode"],
        frm_tm=tmr,
        to_tm=sixmo
    )
    if fl is None:
        continue
    if fl.fprice < des["lowestPrice"]:
        usr = dmgr.get_cust_emails()
        email_s = [i["email"] for i in usr]
        nms = [j["firstName"] for j in usr]

        if fl.fstp_ovrs == 0:
            msg2 = f"✈️\nLow Price Alert!! 🔻 \nOnly ₹ {fl.fprice} 🤑 \nto fly From {fl.forigin_city}-{fl.forigin_port} 🛫 To {fl.fdes_city}-{fl.fdes_port} 🛬\nOn {fl.fout_date} at {fl.fout_tm} "
            link = f"https://www.google.com/travel/flights/search?hl=en#flt={fl.forigin_port}.{fl.fdes_port}.{fl.fout_date}"
        else:
            msg2 = f"✈️\nLow Price Alert!! 🔻 \nOnly ₹ {fl.fprice} 🤑 \nto fly From {fl.forigin_city}-{fl.forigin_port} 🛫 To {fl.fdes_city}-{fl.fdes_port} 🛬\non {fl.fout_date} at {fl.fout_tm}\nand From {fl.forigin_city2}-{fl.forigin_port2} 🛫 To {fl.fdes_city2}-{fl.fdes_port2} 🛬\nOn {fl.fout_date2} at {fl.fout_tm2}."
            link = f"https://www.google.com/travel/flights/search?hl=en#flt={fl.forigin_port}.{fl.fdes_port2}.{fl.fout_date}"

        # notmgr.sms(msg2, link)
        notmgr.snd_email(nms, email_s, msg2, link)