# Step 1: import necessary packages. Importing again so that if user does not wish to see expense file the code can still run
import pandas as pd

# Step 2: create date filtering function

def filter_expenses_by_date(expenses, start_date, end_date):
    """
    Filters the expense data by a given range.

    Args:
        expenses (string): path to the Excel file containing the expense data.
        start_date (string or datetime-like): The start date for filtering (inclusive).
        end_date (string or datetime-like): The end date for filtering (inclusive).

    Returns:
        pandas.DataFrame: A DataFrame containing only the expenses within the specified date range.
    """
    split_expenses_dataset = pd.read_excel(expenses)
    filtered_dataset = split_expenses_dataset[
        (split_expenses_dataset['Date'] >= start_date) & 
        (split_expenses_dataset['Date'] <= end_date)
    ]
    return filtered_dataset    

# Step 3: defining function that calculates the expenses

def split_expenses(expenses, start_date=None, end_date=None):
    """
    Splits expenses among participants and calculates individual balances.

    If a date range is provided, only expenses within that range are considered.

    Args:
        expenses (string): Path to the Excel file containing the expense data.
        start_date (string or datetime-like, optional): The start date for filtering (inclusive).
        end_date (string or datetime-like, optional): The end date for filtering (inclusive).

    Returns:
        dict: each person's total balance. 
              Positive means they paid more than they owe, negative means they owe money.
    """
    if start_date and end_date:
        split_expenses_dataset = filter_expenses_by_date(expenses, start_date, end_date)
    else:
        split_expenses_dataset = pd.read_excel(expenses)

    payer_column = split_expenses_dataset.columns[3] 
    participant_columns = split_expenses_dataset.columns[4:]

    balances = {}

    for _, row in split_expenses_dataset.iterrows():
        cost = row["cost"]
        payer = row["Paid by"]
        participants = row[participant_columns]
        involved_people = participants[participants == 1].index.tolist()
        number_involved_people = len(involved_people)
        cost_share = cost / number_involved_people 

        balances[payer] = balances.get(payer, 0) + cost 
        for participant in involved_people:
            balances[participant] = balances.get(participant, 0) - cost_share

    rounded_balances = {person: round(amount, 2) for person, amount in balances.items()}
    return rounded_balances


# Step 12 & 13: only run this block if script is run directly, not when imported otherwise the test running gives an error
if __name__ == "__main__":
    # Change the file name, start date, and end date as needed
    file_name = "expenses_splitter_example_file.xlsx"
    start_date = "2024-07-01"
    end_date = "2024-08-21"
    final_balance = split_expenses(file_name, start_date, end_date)

    # Print the final rounded balances
    print(final_balance)
