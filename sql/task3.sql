WITH sales_per_category AS (
  SELECT
    cat.CategoryName,
    ord.*,
    ROW_NUMBER() OVER (PARTITION BY cat.CategoryName ORDER BY ord.LineTotal DESC) AS BiggestSalesOrder
  from
    `PROJECT_ID.DATASET_ID.orders` as ord
  left join
    `PROJECT_ID.DATASET_ID.products` as prd
  on
    ord.ProductID = prd.ProductID
  left join
    `PROJECT_ID.DATASET_ID.productsubcategories` as sub
  on
    prd.SubCategoryID = sub.SubCategoryID
  left join
    `PROJECT_ID.DATASET_ID.productcategories` cat
  ON
    cat.CategoryID = sub.CategoryID
)

SELECT * EXCEPT(BiggestSalesOrder) FROM sales_per_category
WHERE BiggestSalesOrder <= 5


