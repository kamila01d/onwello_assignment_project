SELECT
  sub.SubCategoryName,
  SUM(ord.LineTotal) AS LineTotal
FROM
  `PROJECT_ID.DATASET_ID.orders` ord
LEFT JOIN
  `PROJECT_ID.DATASET_ID.products` prod
ON
  ord.ProductID = prod.ProductID
LEFT JOIN
  `PROJECT_ID.DATASET_ID.productsubcategories` sub
ON
  prod.SubCategoryID = sub.SubCategoryID
GROUP BY
  sub.SubCategoryName