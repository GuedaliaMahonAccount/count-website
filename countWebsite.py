import pandas as pd

# Load the Excel files
file1 = 'Suspected.xlsx'
file2 = 'Diagnosed.xlsx'
file3 = 'Normal1.xlsx'
file4 = 'Normal2.xlsx'

# Read the Excel files into DataFrames
df1 = pd.read_excel(file1, engine='openpyxl')
df2 = pd.read_excel(file2, engine='openpyxl')
df3 = pd.read_excel(file3, engine='openpyxl')
df4 = pd.read_excel(file4, engine='openpyxl')


# Function to standardize website names
def standardize_website(name):
    name = str(name).lower()
    if 'face' in name:
        return 'facebook'
    if 'red' in name:
        return 'reddit'
    if 'r/' in name:
        return 'reddit'

    # Add more standardizations as needed
    return name


# Function to analyze the DataFrames
def analyze_websites(df):
    # Standardize website names
    df['standardized_website'] = df['website'].apply(standardize_website)

    # Count the number of unique websites in the "standardized_website" column
    unique_websites = df['standardized_website'].nunique()

    # Find the top 6 most frequent websites and how many times they appear
    top_26_sites = df['standardized_website'].value_counts().head(26)

    # Display the results
    print(f"Number of different websites: {unique_websites}")
    print("Names of different websites:")
    print(df['standardized_website'].unique())
    print("The top 6 most frequent websites and their occurrences are:")
    print(top_26_sites)
    print("\n")


# Analyze the first file
print("Analysis of Suspected.xlsx:")
analyze_websites(df1)

# Analyze the second file
print("Analysis of Diagnosed.xlsx:")
analyze_websites(df2)

# Analyze the third file
print("Analysis of Normal1.xlsx:")
analyze_websites(df3)

# Analyze the for file
print("Analysis of Normal2.xlsx:")
analyze_websites(df4)
