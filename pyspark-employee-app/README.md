# PySpark Employee RDD Application

## Overview

This project demonstrates PySpark RDD operations using Docker.

Operations performed:

1. Sort employees by salary descending
2. Calculate department-wise salary totals
3. Find top 3 highest paid employees
4. Save top 3 employees to file

---

## Dataset

employees.csv

```csv
id,name,department,salary
1,Amit,IT,55000
2,Rahul,HR,40000
3,Neha,IT,65000
4,Priya,Finance,70000
5,Karan,IT,50000
6,Simran,HR,45000
7,Rohit,Finance,60000
```

---

## Build Docker Image

```bash
docker build -t pyspark-employee-app .
```

## Run Docker Container

```bash
docker run --rm pyspark-employee-app
```

---

## Output

### Sorted Employees

Sorted in descending salary order.

### Department Salary Totals

IT = 170000

HR = 85000

Finance = 130000

### Top 3 Employees

Saved to:

```text
top3_employees.txt
```

---

## Technologies Used

- Python 3.12
- Apache Spark (PySpark)
- Docker
- Java 17

---

## Author

Vishnu