{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 64,
   "id": "41663aab-956e-4b15-b041-7a0a9e373f0e",
   "metadata": {},
   "outputs": [],
   "source": [
    "#Step 1: import necessary packages\n",
    "import pandas as pd"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 65,
   "id": "89c002a9-2560-49f1-aaec-d5b20821407d",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "                     expense name       Date   cost Paid by  Lily  Bob  Emma  Anna\n",
      "0                     cooking oil 2025-07-04   1.70    Emma     0    0     1     1\n",
      "1                 concert tickets 2025-08-08  24.00    Emma     0    0     0     1\n",
      "2                     settle debt 2025-08-09  24.85    Anna     0    0     1     0\n",
      "3                       shoe rack 2025-09-07  18.00     Bob     0    1     1     1\n",
      "4           ikea kitchen supplies 2025-09-07  17.35    Emma     1    1     1     1\n",
      "5           toilet paper and soap 2025-09-10   7.00    Lily     1    1     1     1\n",
      "6                    house dinner 2025-09-16  20.00     Bob     1    1     1     1\n",
      "7                        kruidvat 2025-09-16   2.50    Lily     0    1     0     0\n",
      "8                    gyoza dinner 2025-09-22  17.60    Lily     1    1     1     1\n",
      "9                ikea shower rack 2025-09-30  15.00    Emma     0    1     1     1\n",
      "10      higher gas prices october 2025-09-30  13.21    Lily     1    1     1     1\n",
      "11            Sunday house dinner 2025-09-30  18.00    Emma     1    1     1     1\n",
      "12                 shepherd's pie 2025-10-07  22.30    Anna     1    1     1     1\n",
      "13                   paper towels 2025-10-08   3.00    Lily     1    1     1     1\n",
      "14                  toilet paper  2025-10-11   4.50    Lily     1    1     1     1\n",
      "15          pad thai board dinner 2025-10-23  29.80    Lily     1    1     1     1\n",
      "16                         coffee 2025-10-23   4.19    Lily     0    0     1     1\n",
      "17               snacks from home 2025-10-24  10.00    Emma     0    0     0     1\n",
      "18                      olive oil 2025-10-24   8.29    Emma     0    1     1     1\n",
      "19                           beer 2025-10-25  26.44     Bob     0    1     1     1\n",
      "20                    gold strike 2025-10-25  17.99    Anna     0    1     1     1\n",
      "21    paper towels and trash bags 2025-10-28   5.88    Anna     1    1     1     1\n",
      "22                    settle debt 2025-10-30  36.00    Anna     1    0     0     0\n",
      "23          tiramisu board dinner 2025-11-03  25.50    Emma     1    1     1     1\n",
      "24         batteries for doorbell 2025-11-11   7.80    Lily     1    1     1     1\n",
      "25  toilet paper and baking paper 2025-11-17   4.90    Emma     1    1     1     1\n",
      "26                   oil and salt 2025-11-17  10.29    Emma     0    1     1     1\n",
      "27                      groceries 2025-12-01   9.70    Lily     0    0     0     1\n",
      "28                  gulyas dinner 2025-12-01  13.00    Lily     1    1     1     1\n",
      "29                            KFC 2025-12-07  16.62     Bob     0    1     1     0\n",
      "30          toilet paper and soap 2025-12-18   5.30    Lily     1    1     1     1\n",
      "31                          pasta 2025-12-16   4.00    Lily     0    0     1     0\n",
      "32                        palinka 2025-12-30  13.00    Lily     0    0     0     1\n",
      "33   trash bags and kitchen paper 2025-01-02   8.50    Lily     1    1     1     1\n",
      "34                   house dinner 2025-01-09  21.43    Lily     1    1     1     1\n",
      "35            coffee and oat milk 2025-01-23   9.00    Anna     0    0     1     1\n",
      "36                 dinner with Fi 2025-01-25   5.50    Lily     0    0     0     1\n",
      "37                   toilet paper 2025-01-28   3.70    Lily     1    1     1     1\n"
     ]
    }
   ],
   "source": [
    "#Step 2: visualise expense list\n",
    "dataset = pd.read_excel('expenses_splitter_example_file.xlsx')\n",
    "pd.set_option('display.width', 200) #(line below as well) used to display all columns in one set\n",
    "pd.set_option('display.max_columns',8) \n",
    "print(dataset)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 66,
   "id": "d179582e-2af1-4cd1-ba44-f1524780b260",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "{'Emma': -3.7708333333333313, 'Anna': -47.82083333333334, 'Bob': -23.945833333333336, 'Lily': 75.53750000000001}\n"
     ]
    }
   ],
   "source": [
    "#Step 3: defining function that calculates the expenses\n",
    "def split_expenses(expenses_splitter_example_file):\n",
    "    split_expenses_dataset = pd.read_excel(expenses_splitter_example_file)\n",
    "\n",
    "    #Step 4: define payer and participant columns outside of loop\n",
    "    payer_column = split_expenses_dataset.columns[3] \n",
    "    participant_columns = split_expenses_dataset.columns[4:] \n",
    "\n",
    "    #Step 5: create dictionary that keep track of expenses\n",
    "    balances = {}\n",
    "\n",
    "    #Step 6: create a loop that calculates the expenses for each row and adds them all up. \n",
    "    for _, row in split_expenses_dataset.iterrows():\n",
    "        #Step 6b: define the content of the rows found in the dataset\n",
    "        cost = row[\"cost\"]\n",
    "        payer = row[\"Paid by\"]\n",
    "\n",
    "        #Step 7: define the number of people who take part in an expense\n",
    "        participant_shares = row[participant_columns]\n",
    "        involved_people = participant_shares[participant_shares == 1].index.tolist()\n",
    "        number_involved_people = len(involved_people) \n",
    "\n",
    "        #Step 8: define how the costs get shared\n",
    "        cost_share = cost/number_involved_people\n",
    "            \n",
    "        #Step 9: add total expense cost to the balance of the payer\n",
    "        balances[payer] = balances.get(payer, 0) + cost \n",
    "\n",
    "        #Step 10: subtract expense cost based on the cost share for participants in an expense\n",
    "        for participant in involved_people:\n",
    "            balances[participant] = balances.get(participant, 0) - cost_share\n",
    "        \n",
    "    #Step 11: finish function\n",
    "    return balances\n",
    "\n",
    "#Step 12: split the expenses and display final amounts\n",
    "final_balance = split_expenses('expenses_splitter_example_file.xlsx')\n",
    "print(final_balance)"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.12.7"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
