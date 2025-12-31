import json
import numpy as np
from datetime import datetime

def load_data(file_path):
    with open(file_path, 'r') as f:
        data = json.load(f)
    return data

def parse_date(date_str):
    try:
        # Format: "13-May-2003"
        return datetime.strptime(date_str, "%d-%b-%Y")
    except ValueError:
        return None

def main():
    file_path = 'students.json'
    print(f"Loading data from {file_path}...")
    data = load_data(file_path)
    
    # Extract columns
    print("Extracting data...")
    categories = []
    genders = []
    dobs = []
    
    for student in data:
        categories.append(student.get("Category", "Unknown"))
        genders.append(student.get("Gender", "Unknown"))
        
        dob_str = student.get("Date of Birth")
        if dob_str:
            dobs.append(parse_date(dob_str))
        else:
            dobs.append(None)

    # Convert to NumPy arrays
    np_categories = np.array(categories)
    np_genders = np.array(genders)
    
    # Filter valid dates for date analysis
    valid_dates = [d for d in dobs if d is not None]
    np_dobs = np.array(valid_dates, dtype='datetime64[D]')
    
    print(f"\nTotal Students: {len(data)}")
    
    # 1. Category Analysis
    print("\n--- Category Analysis ---")
    unique_cats, counts_cats = np.unique(np_categories, return_counts=True)
    for cat, count in zip(unique_cats, counts_cats):
        print(f"{cat}: {count}")
        
    # 2. Gender Analysis
    print("\n--- Gender Analysis ---")
    unique_genders, counts_genders = np.unique(np_genders, return_counts=True)
    for gender, count in zip(unique_genders, counts_genders):
        print(f"{gender}: {count}")
        
    # 3. Age Analysis
    print("\n--- Age Analysis ---")
    # Calculate age based on current date
    current_date = np.datetime64('today')
    
    # Age in years = (Current Date - DOB) / 365.25 days
    if len(np_dobs) > 0:
        ages_days = current_date - np_dobs
        ages_years = ages_days.astype('timedelta64[Y]').astype(int)
        
        print(f"Average Age: {np.mean(ages_years):.2f} years")
        print(f"Minimum Age: {np.min(ages_years)} years")
        print(f"Maximum Age: {np.max(ages_years)} years")
        
        # Age distribution
        unique_ages, counts_ages = np.unique(ages_years, return_counts=True)
        print("Age Distribution:")
        for age, count in zip(unique_ages, counts_ages):
            print(f"  {age} years: {count}")
    else:
        print("No valid dates found for age analysis.")

    # 4. Birth Month Analysis
    print("\n--- Birth Month Analysis ---")
    if len(np_dobs) > 0:
        # Extract month (1-12)
        months = np_dobs.astype('datetime64[M]').astype(int) % 12 + 1
        unique_months, counts_months = np.unique(months, return_counts=True)
        
        # Month names mapping
        month_names = ["", "Jan", "Feb", "Mar", "Apr", "May", "Jun", 
                       "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
        
        # Sort by count descending
        sorted_indices = np.argsort(counts_months)[::-1]
        
        print("Top Birth Months:")
        for i in range(min(12, len(sorted_indices))):
            idx = sorted_indices[i]
            month_num = unique_months[idx]
            count = counts_months[idx]
            print(f"  {month_names[month_num]}: {count}")

if __name__ == "__main__":
    main()
