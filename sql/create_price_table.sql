CREATE TABLE price_data.DailyPriceData(
  ticker STRING,
  price NUMERIC,
  _date DATE,

  PRIMARY KEY(ticker, price, _date) NOT ENFORCED
);