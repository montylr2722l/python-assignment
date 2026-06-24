# PySpark Sales DataFrame Application

## Overview

This project demonstrates the use of PySpark DataFrames to process sales data inside a Docker container.

The application performs the following operations:

1. Reads sales data from a CSV file.
2. Sorts all products by sales in descending order.
3. Displays the top 3 products with the highest sales.
4. Filters products with sales greater than 80,000.
5. Saves the filtered output as a CSV file.

---

## Project Structure

```text
pyspark-sales-app/
│
├── app.py
├── sales.csv
├── Dockerfile
├── requirements.txt
├── README.md
├── Screenshot.png
│
└── output/
    └── filtered_sales.csv
```

---

## Dataset

**sales.csv**

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

## Technologies Used

* Python 3.12
* PySpark 3.5.1
* Apache Spark
* Java (JDK)
* Docker

---

## Build Docker Image

Run the following command from the project directory:

```bash
docker build -t pyspark-sales-app .
```

---

## Run Docker Container

```bash
docker run --rm pyspark-sales-app
```

---

## Operations Performed

### 1. Sort Products by Sales (Descending)

Products are sorted in descending order based on sales values.

### 2. Display Top 3 Products

Top three highest-selling products are displayed on the console.

### 3. Filter Products with Sales Greater Than 80,000

Filtered products are saved in:

```text
output/filtered_sales.csv
```

---

## Filtered Output

```csv
product_id,product_name,category,sales
101,Laptop,Electronics,150000
102,Mobile,Electronics,95000
103,TV,Electronics,120000
108,Bed,Furniture,90000
```

---

## Sample Console Output

```text
===== Products Sorted By Sales =====

Laptop      150000
TV          120000
Mobile       95000
Bed          90000
Sofa         80000
Table        45000
Chair        30000
Headphones   25000

===== Top 3 Products =====

Laptop      150000
TV          120000
Mobile       95000

===== Products With Sales > 80000 =====

Laptop      150000
Mobile       95000
TV          120000
Bed          90000

Filtered sales saved successfully.
```

---

## Screenshot

Add the Docker execution screenshot here:

![Output Screenshot](Screenshot.png)

---

## Author

Vishnu
