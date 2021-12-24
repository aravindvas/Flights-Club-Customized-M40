import requests
from flightdata import FlightData
import os

teqep = "https://tequila-api.kiwi.com"
teqkey = "yb077nNUa6cncl5oV5B71HSDD21mMahJ"

class Flight():

    def get_des_code(self, cn):
        loc_ep = f"{teqep}/locations/query"
        headers = {"apikey": teqkey}
        qry = {"term": cn, "location_types": "city"}
        rsp3 = requests.get(url=loc_ep, headers=headers, params=qry)
        rslt = rsp3.json()["locations"]
        cd = rslt[0]["code"]
        return cd

    def checkf(self, org_city_cd, des_city_cd, frm_tm, to_tm):
        srh_ep = f"{teqep}/v2/search"
        headers2 = {"apikey": teqkey}
        qry2 = {
            "fly_from": org_city_cd,
            "fly_to": des_city_cd,
            "date_from": frm_tm.strftime("%d/%m/%Y"),
            "date_to": to_tm.strftime("%d/%m/%Y"),
            # "nights_in_dst_from": 1,
            # "nights_in_dst_to": 7,
            "flight_type": "oneway",
            "one_for_city": 1,
            # "one_per_date": 1,
            "max_stopovers": 0,
            "curr": "INR"
        }
        rsp4 = requests.get(
            url=srh_ep,
            headers=headers2,
            params=qry2
        )

        try:
            dat = rsp4.json()["data"][0]
            # print(dat)
        except IndexError:
          qry2["max_stopovers"] = 1
          rsp4 = requests.get(
          url=srh_ep,
          headers=headers2,
          params=qry2)
          try:
            dat = rsp4.json()["data"][0]
            # pprint(dat)
            fdat = FlightData(
                price=dat["price"],
                origin_city=dat["route"][0]["cityFrom"],
                origin_city2=dat["route"][1]["cityFrom"],
                origin_port=dat["route"][0]["flyFrom"],
                origin_port2=dat["route"][1]["flyFrom"],
                des_city=dat["route"][0]["cityTo"],
                des_city2=dat["route"][1]["cityTo"],
                des_port=dat["route"][0]["flyTo"],
                des_port2=dat["route"][1]["flyTo"],
                out_date=dat["route"][0]["local_departure"].split("T")[0],
                out_tm=dat["route"][0]["local_departure"].split("T")[1][:5],
                out_date2=dat["route"][1]["local_departure"].split("T")[0],
                out_tm2=dat["route"][1]["local_departure"].split("T")[1][:5],
                stp_ovrs=1
            )
            print(f"From {fdat.forigin_city} To {fdat.fdes_city} on {fdat.fout_date} at {fdat.fout_tm}"
                  f" and From {fdat.forigin_city2} To {fdat.fdes_city2} on {fdat.fout_date2} at {fdat.fout_tm2}: ₹{fdat.fprice}")
            return fdat
          except IndexError:
            print(f"No Flights found for {fdat.fdes_city2} from {fdat.forigin_city}.")
            return None
        else:
          fdat = FlightData(
              price=dat["price"],
              origin_city=dat["route"][0]["cityFrom"],
              origin_city2=None,
              origin_port=dat["route"][0]["flyFrom"],
              origin_port2=None,
              des_city=dat["route"][0]["cityTo"],
              des_city2=None,
              des_port=dat["route"][0]["flyTo"],
              des_port2=None,
              out_date=dat["route"][0]["local_departure"].split("T")[0],
              out_tm=dat["route"][0]["local_departure"].split("T")[1][:5],
              out_date2=None,
              out_tm2=None
          )
          print(f"From {fdat.forigin_city} To {fdat.fdes_city}: ₹{fdat.fprice} on {fdat.fout_date} at {fdat.fout_tm}")
          return fdat
