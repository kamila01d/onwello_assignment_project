SELECT
  EXTRACT(YEAR FROM PARSE_DATE('%m/%d/%Y', OrderDate)) AS year,
  EXTRACT(MONTH FROM PARSE_DATE('%m/%d/%Y', OrderDate)) AS month,
  COUNT(OrderDate) as NumberOfSalesOrders,
  SUM(LineTotal) AS SumOfSalesProfit
FROM
  `PROJECT_ID.DATASET_ID.orders`
GROUP BY year, month
ORDER BY year, month