# Student Data Analysis Walkthrough

We created a Python script `analysis.py` to analyze the student dataset using NumPy. Here are the results and how to run it.

## How to Run

1.  Ensure you have NumPy installed:
    ```bash
    pip install numpy
    ```
2.  Run the analysis script:
    ```bash
    python analysis.py
    ```

## Analysis Results

The script analyzes the `students.json` file and outputs the following insights:

### 1. Category Distribution
| Category | Count |
| :--- | :--- |
| GEN | 126 |
| OBC | 163 |
| SC | 33 |
| ST | 13 |
| UR | 2 |

### 2. Gender Distribution
- **Male**: 241
- **Female**: 96

### 3. Age Analysis
- **Average Age**: 23.13 years
- **Age Range**: 20 - 35 years
- **Most Common Age**: 22 years (102 students)

### 4. Birth Month Analysis
The most common birth months are:
1.  **December** (34 students)
2.  **May** (32 students)
3.  **August** (31 students)

## Code Highlights

We used NumPy for efficient data handling:
- **`np.unique()`**: To count occurrences of categories and genders.
- **`np.datetime64`**: To handle date calculations for age.
- **`np.mean`, `np.min`, `np.max`**: For age statistics.
