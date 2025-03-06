# Expenses Splitter

**Project specifications:**

This is the documentation document for project "Expenses Splitter" for the AESB2122-24 course at the TU Delft, done by student L. Hegyvari nr5502926. The goal of this project is to let the user input a CVS file containing a list of expenses shared by a group of people. The expenses will then be split amongst the group as specified in the CVS file. The output will be a total amount that a person either owes to someone (- value) or that they are owed by someone (+ value). For format specifications needed in the CVS file, please see comment under "Dataset". 

**Dataset:**

I started this project by taking a sample CVS file. This sample CVS file was created from the list of expenses made by my three roommates and I in the last few months. It is available to see in the repository. Names have been anonymised in this example file. The workings of the code for the project can be checked by seeing if the results match the numbers given by the expense splitter system currently used by us. If the numbers do not match, it will be clear that errors need to be fixed in the project's code. These numbers are:
![image](https://github.com/user-attachments/assets/f8e16a83-84de-4261-a448-712b582e0493)

Note that the format of the CVS file is important:
- Expenses should be listed below each other. Row 1 contains column titles and will not be factored into the calculations. Expense shares are rounded to two decimals.
- _Column 1_ contains the name of the expense. This ultimately will not affect the code, so it can contain any name the user wishes to use.
- _Column 2_ contains the date of the expense. Similarly to Row 1, it does not affect the code. Rows 1 and 2 are present in the CVS for the user's convenience for easier editing and review of the expense list.
- _Column 3_ contains the total cost of the expense. This is the amount that will be split between the group members according to the parts specified in columns 5+.
- _Column 4_ contains the name of the person who paid the expense.
- _Columns 5 and above_ will contain the parts that group members contribute to a given expense. This value can be set either to 1 or 0. I means the person contributed to the expense, 0 means they did not.

_Examples:_

1. Roommates Anna, Bob, Lily and Emma shared an expense of 20€. This will read as:

    ![image](https://github.com/user-attachments/assets/f96aa77b-5a1b-439b-a761-e61efc729fe0)

The output for this example will be a share of 1/4 for each person who contributed to the expense, in this case 1/4 * 20€ = 5€ 

2. If only three of the roommates join for dinner, the missing person's share should be set to 0:
 
   ![image](https://github.com/user-attachments/assets/f2313a16-4cb9-4ff4-b2c1-7edae904276a)

Since Emma did not participate in the expense, her share is 0€. The rest of the group pays 1/3 * 20€ = 6.67€
