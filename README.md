# Algorithms Design & Analysis: Finding Duplicating Elements 🔍

## 📌 Project Overview
Developed as a core project for the **Algorithm Design and Analysis (CS315)** course, this study addresses a critical issue in university student database management: **Student ID duplication**. The project evaluates and compares two distinct algorithmic strategies to maintain data integrity and reporting reliability in academic records.

## 🧪 Theoretical & Empirical Analysis
The project provides a structured comparison between a brute-force approach and a hash-based optimized solution, evaluating them across both theoretical complexity and empirical performance.

### 1. Naive Algorithm (Brute Force)
* **Design:** Utilizes nested loops to compare each student ID with every subsequent element in the list.
* **Time Complexity:** $O(n^2)$ - The execution time grows quadratically, making it inefficient for large student databases.
* **Space Complexity:** $O(k)$ - Where $k$ is the number of duplicates found.

### 2. Optimized Algorithm (HashSet Approach)
* **Design:** Uses a **HashSet** to track unique IDs, allowing for duplicate detection in a single pass through the data.
* **Time Complexity:** $O(n)$ - Scales linearly, providing a much more efficient solution for large-scale datasets.
* **Space Complexity:** $O(n)$ - Proportional to the number of unique elements stored in the set.

## 📊 Empirical Performance Results
The algorithms were benchmarked using generated student ID lists ranging from 10 to 10,000 elements, demonstrating the practical impact of time complexity:

| Input Size (n) | Naive Algorithm (Time) | Optimized Algorithm (Time) |
| :--- | :--- | :--- |
| 10 | ~0.00001360s | ~0.0000056s |
| 100 | ~0.0001461s | ~0.0000128s |
| 1,000 | ~0.016564s | ~0.0000383s |
| 10,000 | ~1.6128s | ~0.0002195s |
*(Results based on empirical testing on Python runtime)*

## 🛠 Tech Stack
* **Language:** Python
* **Analytical Method:** Theoretical Complexity Analysis & Empirical Benchmarking
* **Data Structures:** Lists and HashSets

## 📂 Repository Structure
* **[📁 Source Code](./src):** Python implementation of the `find_duplicates_naive` and `find_duplicates_optimized` functions.
* **[Report.pdf](./Finding_duplicating_element.pdf):** Full report including problem identification, pseudocode, and mathematical justifications.

---
*Prepared by Lama Alghofaili (Team Leader) as part of the CS315 course requirements.*
