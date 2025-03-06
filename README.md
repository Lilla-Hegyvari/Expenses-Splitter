# Expenses Splitter

**Project specifications:**

This is the documentation document for project "Expenses Splitter" for the AESB2122-24 course at the TU Delft, done by student L. Hegyvari nr5502926. The goal of this project is to let the user input a CVS file containing a list of expenses shared by a group of people. The expenses will then be split amongst the group as specified in the CVS file. The output will be a total amount that a person either owes to someone (- value) or that they are owed by someone (+ value). For format specifications needed in the CVS file, please see comment under "Dataset". 

**Code usage:**

You can use the code by inputting a CVS file that meets the criteria defined in the "Dataset" section below. The full .ipnyb file can be found in the repository. Then, the only places the code needs to be changed is the file name in the last few lines in step 12:

file_name = "expenses_splitter_example_file.xlsx" -> change the file name between the "..." to your file.
start_date = None -> change "None" to "YYYY-MM-DD" if you wish to filter the data.
end_date = None -> change "None" to "YYYY-MM-DD" if you wish to filter the data.
final_balance = split_expenses(file_name, start_date, end_date)
print(final_balance)

**Dataset:**

I started this project by taking a sample CVS file. This sample CVS file was created from the list of expenses made by my three roommates and I in the last few months. It is available to see in the repository. Names have been anonymised in this example file. The workings of the code for the project can be checked by seeing if the results match the numbers given by the expense splitter system currently used by us. If the numbers do not match, it will be clear that errors need to be fixed in the project's code. These numbers are:

![image](https://github.com/user-attachments/assets/7aff6f1b-5653-426b-aca8-a5eb98e20d5e)

Note that the format of the CVS file is important:
- Expenses should be listed below each other. Row 1 contains column titles and will not be factored into the calculations. Expense shares are rounded to two decimals.
- _Column 1_ contains the name of the expense. This ultimately will not affect the code, so it can contain any name the user wishes to use.
- _Column 2_ contains the date of the expense. Similarly to Row 1, it does not affect the code. Rows 1 and 2 are present in the CVS for the user's convenience for easier editing and review of the expense list.
- _Column 3_ contains the total cost of the expense. This is the amount that will be split between the group members according to the parts specified in columns 5+.
- _Column 4_ contains the name of the person who paid the expense.
- _Columns 5 and above_ will contain the parts that group members contribute to a given expense. This value is set to 0 if they did not participate. See examples below.

_Examples:_

1. Roommates Anna, Bob, Lily and Emma shared an expense of 20€. This will read as:

![image](https://github.com/user-attachments/assets/089356b2-5489-4909-ac96-2113d39f3848)

The output for this example will be a share of 1/4 for each person who contributed to the expense, in this case 1/4 * 20€ = 5€ 

2. If only three of the roommates join for dinner, the missing person's share should be set to 0:
 
   ![image](https://github.com/user-attachments/assets/f2313a16-4cb9-4ff4-b2c1-7edae904276a)

Since Emma did not participate in the expense, her share is 0€. The rest of the group pays 1/3 * 20€ = 6.67€

3. Now, Emma's friend Mark joins them for dinner. Emma's share should be set to 2. Lily, Bob and Anna's shares should be set to 1.

![image](https://github.com/user-attachments/assets/23e731c8-c549-4bb5-9ab0-4705ccd22c3f)

Emma pays for Mark's share. She will pay 2/5 * 20€ = 8€ The rest of the three roommates pay 1/5 * 20€ = 4€

**Code writing:**

The Python code for the expense splitter can be found in the repositiory under the name "....". The code was written in such a way that all the steps are explained within the file and the names of the defined functions are as self-explanatory as possible. This may make the names longer than stricty necessary, but I preferred to write a code with slightly more explanations and written out names without many abbreviations to make it user friendly.

The necessary steps in the code are as follows:
1. Import pandas to read the CVS file with the expense dataset.
1b. visualise dataset for easier access if so desired.
2. Define a function that filters the dataset 
3. Define a function for calculation of expenses. When reading the dataset, an if statement is use to be able to filter the data by a start and end date if the user wants to do so.
4. Define names for the column containing the information about who paid and the columns that store the information on who participated in an expense. Since we need to create a loop for calculating the expenses, it is easier/faster to first extract the names of the column so they get processed once and don't get rerun in the loop for each row. We can then just refer back to these columns.
5. Create a dictionary that keeps track of the expenses that someone owes or is owed. We could define the balances specifically for each person, but if we do that, then the user would need to modify a large amount of the code if the input file changes (number of people or names of participants).
6. We can create a loop for the dataset and define the content of the rows for this dataset.
7. We can define who participated in an expense.
8. Define how the costs are split for an expense and how many people participated in the expense. The latter by checking the length of the list created when looking at who participates in the expense, which is done in step 7. Cost splitting is done by dividing the total cost of an expense by the number of people that participated in an expense.
9. Add the total cost of an expense to the balance of the payer.
10. Subtract the share of an expense to anyone who participated in an expense (using the participant list created in step 7).
11. Calculate the final split expense costs.

Results so far: the code seems to work properly. The displayed outputs are consistent with the results given by the current expense calculator in use and changing start & end dates changes the outputs correctly.

All:

![image](https://github.com/user-attachments/assets/11f2b148-4299-4aca-aa4d-f3d8d635c8de)

First few expenses only:

![image](https://github.com/user-attachments/assets/412787ea-f93d-43f5-b389-37f3a22de85a)

