# Expenses Splitter

**Project specifications:**

This is the documentation document for project "Expenses Splitter" for the AESB2122-24 course at the TU Delft, done by student L. Hegyvari nr5502926. The goal of this project is to let the user input a CVS file containing a list of expenses shared by a group of people. The expenses will then be split amongst the group as specified in the CVS file and simplified as to minimise the number of needed money transfers. For format specifications needed in the CVS file, please see comment under "Dataset".

**Dataset:**

I started this project by taking a sample CVS file. This sample CVS file was created from the list of expenses made by my three roommates and I in the last few months. It is available to see in the repository.
Note that names have been anonymised in this example file. 

Note that the format of the CVS file is important:
- Expenses should be listed below each other. Row 1 contains column titles and will not be factored into the calculations.
- Column 1 contains the name of the expense. This ultimately will not affect the code, so it can contain any name the user wishes to use.
- Column 2 contains the date of the expense. Similarly to Row 1, it does not affect the code. Rows 1 and 2 are present in the CVS for the user's convenience for easier editing and review of the expense list.
- Column 3 contains the total cost of the expense. This is the amount that will be split between the group members according to the parts specified on the following rows.
- Columns 4 and above will contain the parts that group members contribute to a given expense.

For example: Roommates Anna, Bob, Lily and Emma shared an expense of 20€. This will read as:

---|Anna|Bob|Lily|Emma|
|1|1|1|1|


So the CVS file should contain 1 under everyone's name. Now, Anna's friend Abby also joins. Anna pays for her friend, so the columns should read 
