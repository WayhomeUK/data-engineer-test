# Random Prices Datamart Test
This is the Data Engineer test. Take as long as you need or think is reasonable. You don't need to complete all the requirements, however your solution should give us enought code to confirm that you are a competent programmer.

You should use python and whatever tool/framework you are comfortable with.
Please do not make your solution publicly available, just compress this folder and send it back to us.

# Introduction
We are a new start up that plans to change the world through advanced analytics built on top of publicly available data. Nobody thought that before, so as pioneers we have a pretty good shot at making some big $$$s here. The only problem? We need your technical expertise to help us build a prototype that will bring in some investment cash.

The landscape here is pretty boring - there are only two publicly available data providers! But at least things are moving fast in our world. Quite literally - each day passes in only 60 seconds, so time to market is minutes.

We will be providing you with two API endpoints for all publicly available data. Each API produces daily numbers every 60 seconds, however it returns "normal" dates. Depending on when you are doing this test, your local time may be in the year 3030 - don't let that throw you off! Also keep in mind that each endpoint only returns latest set of numbers. Once they're gone - they're gone for good. It's a weird world that likes to lose memory of things!

# Objective
We want you to create a data pipeline that connects to two third-party APIs, collects data, and stores it in a database. The deliverable is code that will create this for us.

Make a reasonable choice what database makes most sense, and how to store the received data so it can be easily accessible in the future.
Acceptance criteria? Our boss doesn't know, but "he will know when he sees it" so at least anticipate that after a week he will want to query your datamart and see which city had most transactions by volume, and where prices are going up. That's our advanced analytics.

# Third-party APIs
There are two third-party APIs provided for you - please read carefuly how to access them, and what data they provide.

## Random Registry Prices
Random Registry is the local government agency that requires all property transactions to be reported. These transactions are then published twice a day - at 11:00 and 17:00. Each transaction can only be published once, so if a properterty is included in the morning batch it won't be included in the afternoon batch - unless it was sold again! Random Registry is a well-established organisation, dating back to the medievial days of computing - so they're using an old system that capitalises all strings. Keep that in mind when collating your data!

Data is available via `https://europe-west2-wayhome-data-engineer-test.cloudfunctions.net/rand-registry-prices`.

Random Registry returns a list of dictionaries that constitutes all transactions that were reported to its offices in the timeframe. The data is as follows:
| variable   | type    | description                                 | example                 |
|:-----------|:--------|:--------------------------------------------|:------------------------|
| address    | string  | Address of sold property                    | "1 YELLOW GIRAFFE ROAD" |
| city       | string  | City                                        | "MOS EISLEY"            |
| date       | string  | Reporting date and time, ISO 8601 formatted | "2000-12-29 11:00:00"   |
| price      | integer | Transaction price                           | 243913                  |

Example request to Random Registry Prices API:
```bash
$ curl https://europe-west2-wayhome-data-engineer-test.cloudfunctions.net/rand-registry-prices
{"results":[{"address":"7 GREEN GIRAFFE STREET","city":"BEDROCK","date":"2000-09-25 11:00:00","price":102576},{"address":"9 YELLOW BREAD SQUARE","city":"LIBERTY CITY","date":"2000-09-25 11:00:00","price":186012},{"address":"8 RED PALM TREE AVENUE","city":"HILL VALLEY","date":"2000-09-25 11:00:00","price":254430},{"address":"9 GREEN FRUIT AVENUE","city":"PAWNEE","date":"2000-09-25 11:00:00","price":208027},{"address":"3 PINK FRUIT STREET","city":"BEDROCK","date":"2000-09-25 11:00:00","price":103322}]}
```
and same request roughly 30 seconds later:
```bash
$ curl https://europe-west2-wayhome-data-engineer-test.cloudfunctions.net/rand-registry-prices
{"results":[{"address":"8 YELLOW GIRAFFE SQUARE","city":"ANKH-MORPORK","date":"2000-09-25 17:00:00","price":252584},{"address":"5 ORANGE BREAD PLACE","city":"HILL VALLEY","date":"2000-09-25 17:00:00","price":141183},{"address":"10 RED PALM TREE ROAD","city":"MOS EISLEY","date":"2000-09-25 17:00:00","price":142559},{"address":"1 BLUE BREAD STREET","city":"DUCKBURG","date":"2000-09-25 17:00:00","price":276101},{"address":"8 GREEN PALM TREE AVENUE","city":"DUCKBURG","date":"2000-09-25 17:00:00","price":258028}]}
```

## Office of Random Statistics
Office of Random Statistics (ORS) aggregates all transactions in the country and publishes a daily average for each city. They heard about standardising and sanitising data at ORS, so they're trying to avoid different spellings of each city. Instead they use their own internal codes, which are as follows:

| code   | name         |
|:-------|:-------------|
| S00    | Hill Valley  |
| S01    | Mos Eisley   |
| S02    | Pawnee       |
| S03    | Ankh-Morpork |
| S04    | Liberty City |
| S05    | Duckburg     |
| S06    | Bedrock      |

There are only 7 cities in the country, and their API service returns a list of values for each of them. Values returned should adhere to the following specification:
| variable | type    | description                               | example      |
|:---------|:--------|:------------------------------------------|:-------------|
| `city`   | string  | City code                                 | "S05"        |
| `date`   | string  | Date in ISO-8601 format                   | "2021-03-01" |
| `price`  | integer | Average price during the reporting period | 123000       |

Data is available via `https://europe-west2-wayhome-data-engineer-test.cloudfunctions.net/random-price-index`.

Example request to ORS:
```bash
$ curl https://europe-west2-wayhome-data-engineer-test.cloudfunctions.net/random-price-index
{"results":[{"city":"S00","date":"2000-10-23","price":114612},{"city":"S01","date":"2000-10-23","price":285624},{"city":"S02","date":"2000-10-23","price":174236},{"city":"S03","date":"2000-10-23","price":235761},{"city":"S04","date":"2000-10-23","price":226403},{"city":"S05","date":"2000-10-23","price":294082},{"city":"S06","date":"2000-10-23","price":185452}]}
```

# Things we would like to see
- Tests! We believe that code without tests is bad code, please include any instructions and/or dependencies that we will need in order to run your tests.
- Data sanitation! We believe taking external data as-is is just wrong so make sure you're not feeding your datamart with garbage.
- We work with [git](https://git-scm.com/) for version control, please include your `.git` folder when you compress this folder and send it back to us. You should feel free to commit at any point in the process.
- Since both third-party APIs publish data periodically, make sure you're sending a reasonable number of requests to those services.
- Your pipeline should run for 5 minutes without crashing.
- Store results in a local database. It's up to you how much data processing is handled by python and how much by SQL. We don't care whether you prefer SQL or No-SQL solutions - your choice should make sense for the requirements of this test.

# stretch goals
If you have time or want to go the extra mile, then try implementing the following features:
- Validate whether Office of Random Statistics daily averages reflect what's being reported by Rand Registry.
- Make exactly zero requests beyond what is strictly necessary to fetch data.
- Create a working docker configuration that handles both the pipeline and your database.
- Identify data discrepancies and make decisions how to handle them.
- Handle migrations and schema changes.
