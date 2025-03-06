# Expenses Splitter

**Project specifications:**

This is the documentation document for project "Expenses Splitter" for the AESB2122-24 course at the TU Delft, done by student L. Hegyvari nr5502926. The goal of this project is to let the user input a CVS file containing a list of expenses shared by a group of people. The expenses will then be split amongst the group as specified in the CVS file. The output will be a total amount that a person either owes to someone (- value) or that they are owed by someone (+ value). For format specifications needed in the CVS file, please see comment under "Dataset". 

**Code usage:**

You can use the code by inputting a CVS file that meets the criteria defined in the "Dataset" section below. Then, the only places the code needs to be changed is the file name in the second to last line:
final_balance = split_expenses('expenses_splitter_example_file.xlsx') where instead of 'expenses_splitter_example_file.xlsx' you can change it to the name of your file.

**Dataset:**

I started this project by taking a sample CVS file. This sample CVS file was created from the list of expenses made by my three roommates and I in the last few months. It is available to see in the repository. Names have been anonymised in this example file. The workings of the code for the project can be checked by seeing if the results match the numbers given by the expense splitter system currently used by us. If the numbers do not match, it will be clear that errors need to be fixed in the project's code. These numbers are:
![image](https://github.com/user-attachments/assets/f8e16a83-84de-4261-a448-712b582e0493)

Note that the format of the CVS file is important:
- Expenses should be listed below each other. Row 1 contains column titles and will not be factored into the calculations. Expense shares are rounded to two decimals.
- _Column 1_ contains the name of the expense. This ultimately will not affect the code, so it can contain any name the user wishes to use.
- _Column 2_ contains the date of the expense. Similarly to Row 1, it does not affect the code. Rows 1 and 2 are present in the CVS for the user's convenience for easier editing and review of the expense list.
- _Column 3_ contains the total cost of the expense. This is the amount that will be split between the group members according to the parts specified in columns 5+.
- _Column 4_ contains the name of the person who paid the expense.
- _Columns 5 and above_ will contain the parts that group members contribute to a given expense. This value is set to 0 if they did not participate. See examples below.

_Examples:_

1. Roommates Anna, Bob, Lily and Emma shared an expense of 20€. This will read as:

    ![image](https://github.com/user-attachments/assets/f96aa77b-5a1b-439b-a761-e61efc729fe0)

The output for this example will be a share of 1/4 for each person who contributed to the expense, in this case 1/4 * 20€ = 5€ 

2. If only three of the roommates join for dinner, the missing person's share should be set to 0:
 
   ![image](https://github.com/user-attachments/assets/f2313a16-4cb9-4ff4-b2c1-7edae904276a)

Since Emma did not participate in the expense, her share is 0€. The rest of the group pays 1/3 * 20€ = 6.67€

3. Now, Emma's friend Mark joins them for dinner. Emma's share should be set to 2. Lily, Bob and Anna's shares should be set to 1.
 ![image](https://github.com/user-attachments/assets/bd96b529-d3a7-40a6-9423-47b758f1e34b)

Emma pays for Mark's share. She will pay 2/5 * 20€ = 8€

**Code writing:**

The Python code for the expense splitter can be found in the repositiory under the name "....". The code was written in such a way that all the steps are explained within the file and the names of the defined functions are as self-explanatory as possible. This may make the names longer than stricty necessary, but I preferred to write a code with slightly more explanations and written out names without many abbreviations to make it user friendly.

The necessary steps in the code are as follows:
1. Import pandas to read the CVS file with the expense dataset.
2. visualise dataset for easier access.
3. Define a function for calculation of expenses.
4. Define names for the column containing the information about who paid and the columns that store the information on who participated in an expense. Since we need to create a loop for calculating the expenses, it is easier/faster to first extract the names of the column so they get processed once and don't get rerun in the loop for each row. We can then just refer back to these columns. This is mostly important if the list of expenses is long.
5. Create a dictionary that keeps track of the expenses that someone owes or is owed. We could define the balances specifically for each person, but if we do that, then the user would need to modify a large amount of the code if the input file changes (number of people or names of participants).
6. We can create a loop for the dataset and define the content of the rows for this dataset.
7. We can define the number of people who take part in the expense.
8. Define how the costs are split for an expense. This is done by dividing the total cost of an expense by the number of people that participated in an expense. This number of people is what was defined in step 7.
9. Add the total cost of an expense to the balance of the payer.
10. Subtract the share of an expense to anyone who participated in an expense (using the participant lsit created in step 7).
11. Calculate the final split expense costs.

Results so far: the code seems to work properly. The displayed outputs are consistent with the results given by the current expense calculator in use. 

![image](https://github.com/user-attachments/assets/bee85517-2d52-4233-a5dd-ff91fb61d02a)

**Possible improvements:**
- optimise code. 
- make it possible to sort the expenses based on time intervals e.g. give the expenses for the month of March. This could serve as having a project that contains multiple functions.
- nicer result output. For the moment I couldn't figure out how to print out the result in with only 2 decimal places and in a better looking format.
