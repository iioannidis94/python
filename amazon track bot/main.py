from bs4 import BeautifulSoup
import smtplib
import requests as rq

BUY_PRICE = 100

my_email = "r.4z0r3583@gmail.com"
my_password = "whelbkqtsjqxejzu"

URL = "https://www.amazon.com/dp/B09TYVYRD9/ref=sbl_dpx_kitchen-electric-cookware_B08GC6PL3D_0"

header = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.125 Safari/537.36",
    "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8"
}

response = rq.get(URL, headers=header)

web_resp = response.text
soup = BeautifulSoup(web_resp, "html.parser")


price_search = soup.find(name="span", class_="a-offscreen")
title = soup.find(id="productTitle").get_text().strip()
price = float(price_search.getText().split("$")[1])

if price < BUY_PRICE:
    message = f"{title} is now {price}"

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=my_password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs=my_email,
            msg=f"{message}"
        )
