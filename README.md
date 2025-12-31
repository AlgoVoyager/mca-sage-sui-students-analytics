# MCA SAGE SUI Student Data Analysis

This project performs data analysis on the MCA student dataset (`students.json`) using Python and **NumPy**. It extracts insights related to student demographics such as age, gender, and category distribution.

## 📊 Features

The `analysis.py` script calculates and displays:

-   **Category Analysis**: Distribution of students across different categories (GEN, OBC, SC, ST, etc.).
-   **Gender Analysis**: Count of male and female students.
-   **Age Analysis**:
    -   Average, Minimum, and Maximum age.
    -   Age distribution (count of students per age).
-   **Birth Month Analysis**: Identifies the months with the most birthdays.

## 🛠️ Prerequisites

-   Python 3.x
-   NumPy

## 🚀 Setup and Usage

1.  **Clone the repository** or download the files to your local machine.

2.  **Install dependencies**:
    ```bash
    pip install numpy
    ```

3.  **Run the analysis**:
    ```bash
    python analysis.py
    ```

## 📂 Project Structure

-   `students.json`: The source dataset containing student details.
-   `analysis.py`: The main Python script that loads the JSON data, processes it with NumPy, and prints the analysis.
-   `README.md`: This documentation file.

## 📝 Example Output

```text
--- Category Analysis ---
GEN: 126
OBC: 163
...

--- Age Analysis ---
Average Age: 23.13 years
Minimum Age: 20 years
Maximum Age: 35 years
...
```
