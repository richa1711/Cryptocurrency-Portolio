# Cryptocurrency-Portolio Applications:


In this project you can extract current crypto market trends using the CoinMarketCap API. With this you can monitor and watch the crypto market.

- Read the official [API documentation](https://coinmarketcap.com/api/documentation/v1/)
- For the pro version, get an API Key on the [Developper Portal](https://coinmarketcap.com/api/)
- Be sure to replace the API Key in sample code with your own.


### CoinMarketCapAPI

__Synopsis__

```
CoinMarketCapAPI(api_key=None, [debug=False, logger=None, sandbox=False, version='v1'])
```

- `debug`: set verbosity.
- `sandbox`: In case of default sandbox API key changes, see [Issue #1](https://github.com/rsz44/python-coinmarketcap/issues/1).
- `logger`: you can give a custom logger.
- `version`: set the version in the URL, for futures version.

__Methods__

You have to pass to the following methods the parameters detailed in the [official documentation](https://coinmarketcap.com/api/documentation/v1/).

| Methods and documentation | Endpoint (version) |
|-|-|
| [📄 __cryptocurrency_map__](https://coinmarketcap.com/api/documentation/v1/#operation/getV1CryptocurrencyMap) | /cryptocurrency/map |
| [📄 __cryptocurrency_info__](https://coinmarketcap.com/api/documentation/v1/#operation/getV2CryptocurrencyInfo) | /cryptocurrency/info (v2) |
| [📄 __cryptocurrency_listings_latest__](https://coinmarketcap.com/api/documentation/v1/#operation/getV1CryptocurrencyListingsLatest) | /cryptocurrency/listings/latest |
| [📄 __cryptocurrency_listings_historical__](https://coinmarketcap.com/api/documentation/v1/#operation/getV1CryptocurrencyListingsHistorical) | /cryptocurrency/listings/historical |
| [📄 __cryptocurrency_quotes_latest__](https://coinmarketcap.com/api/documentation/v1/#operation/getV2CryptocurrencyQuotesLatest) | /cryptocurrency/quotes/latest (v2) |
| [📄 __cryptocurrency_quotes_historical__](https://coinmarketcap.com/api/documentation/v1/#operation/getV2CryptocurrencyQuotesHistorical) | /cryptocurrency/quotes/historical (v2) |
| [📄 __cryptocurrency_marketpairs_latest__](https://coinmarketcap.com/api/documentation/v1/#operation/getV2CryptocurrencyMarketpairsLatest) | /cryptocurrency/market-pairs/latest (v2) |
| [📄 __cryptocurrency_ohlcv_latest__](https://coinmarketcap.com/api/documentation/v1/#operation/getV2CryptocurrencyOhlcvLatest) | /cryptocurrency/ohlcv/latest (v2) |
| [📄 __cryptocurrency_ohlcv_historical__](https://coinmarketcap.com/api/documentation/v1/#operation/getV2CryptocurrencyOhlcvHistorical) | /cryptocurrency/ohlcv/historical (v2) |
| [📄 __cryptocurrency_priceperformancestats_latest__](https://coinmarketcap.com/api/documentation/v1/#operation/getV2CryptocurrencyPriceperformancestatsLatest) | /cryptocurrency/price-performance-stats/latest (v2) |
| [📄 __cryptocurrency_categories__](https://coinmarketcap.com/api/documentation/v1/#operation/getV1CryptocurrencyCategories) | /cryptocurrency/categories |
| [📄 __cryptocurrency_category__](https://coinmarketcap.com/api/documentation/v1/#operation/getV1CryptocurrencyCategory) | /cryptocurrency/category |
| [📄 __cryptocurrency_airdrops__](https://coinmarketcap.com/api/documentation/v1/#operation/getV1CryptocurrencyAirdrops) | /cryptocurrency/airdrops |
| [📄 __cryptocurrency_airdrop__](https://coinmarketcap.com/api/documentation/v1/#operation/getV1CryptocurrencyAirdrop) | /cryptocurrency/airdrop |
| [📄 __cryptocurrency_trending_latest__](https://coinmarketcap.com/api/documentation/v1/#operation/getV1CryptocurrencyTrendingLatest) | /cryptocurrency/trending/latest |
| [📄 __cryptocurrency_trending_mostvisited__](https://coinmarketcap.com/api/documentation/v1/#operation/getV1CryptocurrencyTrendingMostvisited) | /cryptocurrency/trending/most-visited |
| [📄 __cryptocurrency_trending_gainerslosers__](https://coinmarketcap.com/api/documentation/v1/#operation/getV1CryptocurrencyTrendingGainerslosers) | /cryptocurrency/trending/gainers-losers |
| [📄 __exchange_map__](https://coinmarketcap.com/api/documentation/v1/#operation/getV1ExchangeMap) | /exchange/map |
| [📄 __exchange_info__](https://coinmarketcap.com/api/documentation/v1/#operation/getV1ExchangeInfo) | /exchange/info |
| [📄 __exchange_listings_latest__](https://coinmarketcap.com/api/documentation/v1/#operation/getV1ExchangeListingsLatest) | /exchange/listings/latest |
| [📄 __exchange_listings_historical__](https://coinmarketcap.com/api/documentation/v1/#operation/getV1ExchangeListingsHistorical) | /exchange/listings/historical |
| [📄 __exchange_quotes_latest__](https://coinmarketcap.com/api/documentation/v1/#operation/getV1ExchangeQuotesLatest) | /exchange/quotes/latest |
| [📄 __exchange_quotes_historical__](https://coinmarketcap.com/api/documentation/v1/#operation/getV1ExchangeQuotesHistorical) | /exchange/quotes/historical |
| [📄 __exchange_marketpairs_latest__](https://coinmarketcap.com/api/documentation/v1/#operation/getV1ExchangeMarketpairsLatest) | /exchange/market-pairs/latest |
| [📄 __globalmetrics_quotes_latest__](https://coinmarketcap.com/api/documentation/v1/#operation/getV1GlobalmetricsQuotesLatest) | /global-metrics/quotes/latest |
| [📄 __globalmetrics_quotes_historical__](https://coinmarketcap.com/api/documentation/v1/#operation/getV1GlobalmetricsQuotesHistorical) | /global-metrics/quotes/historical |
| [📄 __tools_priceconversion__](https://coinmarketcap.com/api/documentation/v1/#operation/getV2ToolsPriceconversion) | /tools/price-conversion (v2) |
| [📄 __tools_postman__](https://coinmarketcap.com/api/documentation/v1/#operation/getV1ToolsPostman) | /tools/postman |
| [📄 __blockchain_statistics_latest__](https://coinmarketcap.com/api/documentation/v1/#operation/getV1BlockchainStatisticsLatest) | /blockchain/statistics/latest |
| [📄 __fiat_map__](https://coinmarketcap.com/api/documentation/v1/#operation/getV1FiatMap) | /fiat/map |
| [📄 __partners_flipsidecrypto_fcas_listings_latest__](https://coinmarketcap.com/api/documentation/v1/#operation/getV1PartnersFlipsidecryptoFcasListingsLatest) | /partners/flipside-crypto/fcas/listings/latest |
| [📄 __partners_flipsidecrypto_fcas_quotes_latest__](https://coinmarketcap.com/api/documentation/v1/#operation/getV1PartnersFlipsidecryptoFcasQuotesLatest) | /partners/flipside-crypto/fcas/quotes/latest |
| [📄 __key_info__](https://coinmarketcap.com/api/documentation/v1/#operation/getV1KeyInfo) | /key/info |
| [📄 __content_posts_top__](https://coinmarketcap.com/api/documentation/v1/#operation/getV1ContentPostsTop) | /content/posts/top |
| [📄 __content_posts_latest__](https://coinmarketcap.com/api/documentation/v1/#operation/getV1ContentPostsLatest) | /content/posts/latest |
| [📄 __content_posts_comments__](https://coinmarketcap.com/api/documentation/v1/#operation/getV1ContentPostsComments) | /content/posts/comments |
| [📄 __content_latest__](https://coinmarketcap.com/api/documentation/v1/#operation/getV1ContentLatest) | /content/latest |

__Additionnal Parameters__

- `api_version` (str): if given, will fetch the given version of the endpoint (default is equal to the given version in the CoinMarketCapAPI instance wich is actually `v1`). As mentioned in the list above, some endpoints are "v2" by default.

---
##CoinMarketCap API personal portfolio :

Assuming you want to get informations about bitcoin. First, read the [documentation]((https://coinmarketcap.com/api/documentation/v1/#operation/getV1CryptocurrencyInfo)) of the corresponding __cryptocurrency_info__ endpoint. Then on your pc you can run the following python code to successfully make an api call and fetch the data via json.

```python
local_currency = 'RUP'
local_symbol = '₹'
api_key = '______your___api__key___here_______'

headers = {'X-CMC_PRO_API_KEY': api_key}

base_url = 'https://pro-api.coinmarketcap.com'
global_url = base_url + '/v1/global-metrics/quotes/latest?convert=' + local_currency

request = requests.get(global_url, headers=headers)
results = request.json()
```

For printing the json stucture :

```python
print(json.dumps(results, sort_keys=True, indent=4))
````

This will produce this output :

```
{
    "data": {
        "SHIB": {
            "circulating_supply": 549063278876301.94,
            "cmc_rank": 16,
            "date_added": "2020-08-01T00:00:00.000Z",
            "id": 5994,
            "is_active": 1,
            "is_fiat": 0,
            "last_updated": "2023-01-15T10:52:00.000Z",
            "max_supply": null,
            "name": "Shiba Inu",
            "num_market_pairs": 479,
            "platform": {
                "id": 1027,
                "name": "Ethereum",
                "slug": "ethereum",
                "symbol": "ETH",
                "token_address": "0x95ad61b0a150d79219dcf64e1e6cc01f0b64c4ce"
            },
            "quote": {
                "RUP": {
                    "fully_diluted_market_cap": 28475394314906.74,
                    "last_updated": "2023-01-15T10:53:00.000Z",
                    "market_cap": 26511556145837.676,
                    "market_cap_dominance": 0.5659,
                    "percent_change_1h": 0.16446258,
                    "percent_change_24h": -3.15290793,
                    "percent_change_30d": 5.22237647,
                    "percent_change_60d": 21.2201861,
                    "percent_change_7d": 6.67880658,
                    "percent_change_90d": 26.61817229,
                    "price": 0.048285065065898254,
                    "tvl": null,
                    "volume_24h": 1694991883075.3687,
                    "volume_change_24h": -44.0629
                }
            },
            "self_reported_circulating_supply": null,
            "self_reported_market_cap": null,
            "slug": "shiba-inu",
            "symbol": "SHIB",
            "tags": [
                "memes",
                "ethereum-ecosystem",
                "doggone-doggerel"
            ],
            "total_supply": 589735030408322.8,
            "tvl_ratio": null
        }
    },
    "status": {
        "credit_count": 1,
        "elapsed": 26,
        "error_code": 0,
        "error_message": null,
        "notice": null,
        "timestamp": "2023-01-15T10:53:38.837Z"
    }
}
```

you will finally your personal cryptocurrency portfolio by maintaining the csv file containing the ticker symbol and amount of the cryptocurrencies owned by you. In my `Cryptocurrency_Portfolio` directory there is `my_portfolio.csv` file. with python you can read the data from csv and can get the required information of cryptos through json structure. 

The final result will look like :

![Alt text](https://github.com/richa1711/Cryptocurrency-Portolio/blob/main/Output_img/Screenshot%202023-01-15%20at%204.48.06%20PM.png)

---
## Cryptocurrency Alert System

Apart from that,  we can also generate the alert, as per the limit set by the user via maintaing csv file. The required code and its description is in `Cryto_Alert_System` folder. 

---

## Top 100 Crypto Ranker system

We can also list top 100 cryptocurrencies and sort them in three ways:
- Top 100 sorted by market cap
- Top 100 sorted by 24 hour percent change
- Top 100 sorted by 24 hour volume

Here we have used the listings endpoint of the API. 

The result is below:

![Alt text](https://github.com/richa1711/Cryptocurrency-Portolio/blob/main/Output_img/Screenshot%202023-01-10%20at%2010.40.08%20PM.png)

## ChangeLog

- 4 nov 2022: Version 0.5
  - Changing the default API version to `v2` for some endpoints :
    + /v2/cryptocurrency/info
    + /v2/cryptocurrency/quotes/latest
    + /v2/cryptocurrency/quotes/historical
    + /v2/cryptocurrency/market-pairs/latest
    + /v2/cryptocurrency/ohlcv/latest
    + /v2/cryptocurrency/ohlcv/historical
    + /v2/cryptocurrency/price-performance-stats/latest
    + /v2/tools/price-conversion
 
 
