library(coinmarketcapr)

latest_marketcap <- get_global_marketcap('EUR')
all_coins <- get_marketcap_ticker_all()

get_crypto_listings('GBP', latest=F, start=1,
                    date=Sys.Date()-20, limit=10, sort="price", sort_dir="asc")
