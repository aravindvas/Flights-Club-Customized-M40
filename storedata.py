import requests
import os

shtend2 = "https://api.sheety.co/7d4417383a6525d3548aa951e0fc7245/flightDeals/users"
uname = "aravindvas"
pasd = "mailme1997"

print("Welcome to Aravindvas's Flight Club.")
fn = input("What is your First name?: ")
ln = input("What is your Last name?: ")
em = input("What is your Email?: ")
if em != "":
  print("You're officially in the club!!")
  nw_dt = {
    "user":
      {
      "firstName": fn,
      "lastName": ln,
      "email": em
      }
  }
  rsp2 = requests.post(
            url=shtend2,
            auth=(
                uname,
                pasd,
            ),
            json=nw_dt
        )
        # Basic Authentication
  print(rsp2.text, rsp2.status_code)


