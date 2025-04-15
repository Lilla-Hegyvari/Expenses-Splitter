#Step 1: import necessary packages
import pandas as pd

#Step 2: visualise expense list
dataset = pd.read_excel('splitter_examples.xlsx')
pd.set_option('display.width', 200) #(line below as well) used to display all columns in one set
pd.set_option('display.max_columns',8) 
print(dataset)

#import necessary packages. Importing again so that if user does not wish to see expense file the code can still run
import pandas as pd

#Step 2: create date filtering function
"""
    Filters the expense data by a given range.

    Args:
        expenses (string): path to the Excel file containing the expense data.
        start_date (string or datetime-like): The start date for filtering (inclusive).
        end_date (string or datetime-like): The end date for filtering (inclusive).

    Returns:
        pandas.DataFrame: A DataFrame containing only the expenses within the specified date range.
"""
def filter_expenses_by_date(expenses, start_date, end_date):
    
    split_expenses_dataset = pd.read_excel(expenses)
    
    #this filters the dataset based on a given start and end date
    filtered_dataset = split_expenses_dataset[(split_expenses_dataset['Date'] >= start_date) & (split_expenses_dataset['Date'] <= end_date)]
    
    return filtered_dataset

#Step 3: defining function that calculates the expenses
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
def split_expenses(expenses, start_date = None, end_date = None):
    if start_date and end_date: #we need an "if" statement so that if there are dates given for filtering the data it uses the previous filter function
        split_expenses_dataset = filter_expenses_by_date(expenses, start_date, end_date)
    else: #if there are no start and end dates provided, then the code will run the expense calculation on the entire dataset
        split_expenses_dataset = pd.read_excel(expenses)
        
    #Step 4: define payer and participant columns outside of loop
    payer_column = split_expenses_dataset.columns[3] 
    participant_columns = split_expenses_dataset.columns[4:] 

    #Step 5: create dictionary that keeps track of expenses
    balances = {}

    #Step 6: create a loop that calculates the expenses for each row and adds them all up 
    for _, row in split_expenses_dataset.iterrows():
        #Step 6b: define the content of the rows found in the dataset
        cost = row["cost"]
        payer = row["Paid by"]

        #Step 7: this reads who participated in an expense
        #line below: extracts the value from the row that corresponds to the participant_columns, previously defined as columns 5+ in the excel
        participants = row[participant_columns]
        #line below: we only select the participants (as defined above) so we don't run through all columns. 
        #Then it filters through to the columns where the value is 1 (e.g. the person participated in the expense)
        #Then the indextolist reads the names of the participating people out of the top row
        involved_people = participants[participants == 1].index.tolist()

        #Step 8: define how the costs get shared
        number_involved_people = len(involved_people) #counts the amount of people who contributed to the expense
        cost_share = cost/number_involved_people 
            
        #Step 9: add total expense cost to the balance of the payer
        balances[payer] = balances.get(payer, 0) + cost 

        #Step 10: subtract expense cost based on the cost share for participants in an expense
        for participant in involved_people:
            balances[participant] = balances.get(participant, 0) - cost_share
    rounded_balances = {person: round(amount, 2) for person, amount in balances.items()}
    return rounded_balances
        
    #Step 11: finish the function
    return balances

#Step 12: calculate split expenses and display final amounts. Here, change the file name, start and end dates if using a different dataset.
file_name = "splitter_examples.xlsx"
start_date = None
end_date = None
final_balance = split_expenses(file_name, start_date, end_date)
print(final_balance)