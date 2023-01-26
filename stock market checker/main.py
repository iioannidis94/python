import requests
import smtplib


MY_EMAIL = "mail"
MY_PASS = "pass"

STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"
NEWS_API_KEY = "973318177f1e49b3a63bc779c0222555"
STOCK_API_KEY = "H97IG4H8UPKWT10T"

STOCK_ENDPOINT = "https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol=TSLA&interval=5min&apikey=H97IG4H8UPKWT10T"

NEWS_ENDPOINT = "https://newsapi.org/v2/everything"# ?q=TSLA&apiKey=973318177f1e49b3a63bc779c0222555"

# parameters
stock_params = {
    "functions": "TIME_SERIES_INTRADAY",
    "symbol": STOCK_NAME,
    "apikey": STOCK_API_KEY,
}

# stock data json
response = requests.get(STOCK_ENDPOINT, params=stock_params)
data = response.json()["Time Series (5min)"]
data_list = [value for (key, value) in data.items()]
yesterday_data = data_list[0]
yesterday_closing_price = yesterday_data["4. close"]
print(yesterday_closing_price)

    ## STEP 1: Use https://www.alphavantage.co/documentation/#daily
# When stock price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").


day_before_yesterday_date = data_list[1]
day_before_yesterday_closing_price = day_before_yesterday_date["4. close"]
print(day_before_yesterday_closing_price)

difference = abs(float(yesterday_closing_price) - float(day_before_yesterday_closing_price))
print(difference)


dif_percent = (difference / float(yesterday_closing_price)) * 100
print(dif_percent)


if dif_percent > 0.03:
    news_params = {
        "apiKey": NEWS_API_KEY,
        "qInTitle": COMPANY_NAME,

    }
    news_response = requests.get(NEWS_ENDPOINT, params=news_params)
    articles = news_response.json()["articles"]
    three_articles = articles[:3]

    formatted_articles = [f"Headline: {article['title']}. \nBrief {article['description']}" for article in three_articles]

    for article in formatted_articles:
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=MY_EMAIL, password=MY_PASS)
            connection.sendmail(
                from_addr=MY_EMAIL,
                to_addrs=MY_EMAIL,
                msg=article
            )




