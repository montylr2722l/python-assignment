# PySpark Sales DataFrame Application

## Objective

This project demonstrates DataFrame operations using PySpark and Docker.

### Operations

1. Sort products by sales descending
2. Display top 3 products by sales
3. Filter products with sales > 80000
4. Save filtered results to CSV

---

## Dataset

sales.csv

```csv
product_id,product_name,category,sales
101,Laptop,Electronics,150000
102,Mobile,Electronics,95000
103,TV,Electronics,120000
104,Chair,Furniture,30000
105,Table,Furniture,45000
106,Sofa,Furniture,80000
107,Headphones,Electronics,25000
108,Bed,Furniture,90000
```

---

## Build Docker Image

```bash
docker build -t pyspark-sales-app .
```

## Run Docker Container

```bash
docker run --rm pyspark-sales-app
```

---

## Output

### Sorted Products

Displays all products sorted by sales in descending order.

### Top 3 Products

Displays the highest-selling three products.

### Filtered Products

Products with sales greater than 80000 are saved to:

```text
output/filtered_sales/
```

---

## Technologies

- Python 3.12
- PySpark 3.5.1
- Apache Spark
- Java
- Docker

---

## Author

Vishnu