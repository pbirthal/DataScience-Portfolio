import os 
import csv 
import time

       
def existing_list(filename):
    if os.path.isfile(filename):
        with open(filename, 'r') as f:
            reader = csv.DictReader(f)
            data = list(reader)
        return data
def add_expense(filename):
    data = existing_list(filename)
    if data == None:
        data = [] 
    while True: 
        date= str(input('PLEASE ENTER THE DATE OF EXPENSE (YYYY-MM-DD) :'))
        category = str(input('PLEASE ENTER THE RELATED CATEGORY :'))
        amt= float(input('ENTER THE AMOUNT SPENT in  :'))
        desc= str(input('ENTER THE BRIEF DESCRIPTION : '))
        expense_dict = {'Date':date, 'Category':category,'Amount':amt,'Description':desc}
        data.append(expense_dict)
        print('Expense added successfully')
        choice = input('Do you want to add more expenses?(Y/N):')
        if choice == 'Y' or choice == 'y':
            continue
        elif choice == 'N' or choice == 'n':
            break
        else:
            print('Please enter the valid choice')
            break   
    
    print('~-'*40)
    return data

def view_expense(filename): 
    data = existing_list(filename)
    if data == None:
        print('No entries added in this expenses') 
        return 
    else:
        print(f'There are {len(data)} entries in this expense list.')
        expense_dict_keys = ['Date', 'Category', 'Amount', 'Description']
        for i in range(len(data)): 
            if all(map(lambda x: x in expense_dict_keys, data[i]))== True:
                print('-~'*40)
                print(f' ENTRY -- {i+1}')
                print('-~'*40) 
                if '' in data[i].values():
                    print('-'*40)
                    print('Expense contains Missing Value, please update the records')
                    print('-'*40) 
            
                else : 
                    for key, value in data[i].items(): 
                        print(f' {key}----> {value}')
            else: 
                print('Please update the record attributes')

def set_budget(budget=None): 
    if budget==0 or budget ==None: 
        budget = float(input('Please enter the budget for this month:'))
    return budget
    

def track_budget(budget, expense):
    total_spend = 0
    if expense == None:
        print('No entries added in this expenses, Budget is not tracked') 
        return 
    for i in expense: 
        total_spend += i['Amount']
    print(f'Total spend this month: {total_spend}\n')
    if budget>total_spend:
        print('~-'*40) 
        print(f'Amount remaining this month : {budget-total_spend}')
    elif budget<=total_spend: 
        print('WARNNG: ---> Budget exhausted, please avoid spending <---')

def save_expense(filename,expense): 
    file_exists = os.path.isfile(filename)
    with open(filename, 'a',newline='') as f: 
        writer = csv.DictWriter(f, fieldnames=['Date', 'Category', 'Amount', 'Description'])
        if not file_exists:
            writer.writeheader()
        writer.writerows(expense)
    return f'Expenses saved to {filename}'  

def load_expense(filename): 
    with open(filename, 'r') as f: 
        reader = csv.DictReader(f)
        data= list(reader)
        print('~-'*40)
        print('Loading the data now...')
        
    for i in range(len(data)):
        print('-~'*40)
        print(f' ENTRY -- {i+1}')
        print('-~'*40) 
        if '' in data[i].values():
            print('-'*40)
            print('Expense contains Missing Value, please update the records')
            print('-'*40) 
        else : 
            for key, value in data[i].items(): 
                print(f' {key}----> {value}')

def main():
    print('~-'*40)
    bud_choice = input('Do you want to change the budget?(Y/N):')
    if bud_choice == 'Y' or bud_choice == 'y':
        budget = set_budget(budget=0)
    else: 
        budget = set_budget(budget=5000)
    file_choice = input('Do you want to change the filename?(Y/N):')
    if file_choice == 'Y' or file_choice == 'y':
        filename =input('Please enter the filename(add .csv also): ')
    else:
        filename = 'expense.csv'
    expense = existing_list(filename=filename)
    while True:  
        print('~-'*40)
        print('================PERSONAL TRACKER HOMEPAGE===================\n')
        print(f'Note :Budget is {budget} for this month, file is {filename}\n')
        print('~-'*40)
        print(' 1. ADD EXPENSE\n 2. VIEW EXPENSE\n 3. TRACK BUDGET\n 4. SAVE EXPENSES\n 5. EXIT\n')
        choice = int(input('Please choose the options(1,2,3,4,5): '))
        
        print('~-'*40)
        if choice == 1 : 
            print('Adding Expense--->')
            exp = add_expense(filename)
            print('Adding Expense completed')
        elif choice==2:
            print('Viewing Expenses--->')
            view_expense(filename)
        elif choice ==3: 
            print('Tracking Budget--->')
            track_budget(budget,expense)
        elif choice ==4:
            print('Saving Expenses--->')
            save_expense(filename,exp)
            print('File Saved Successfully...')
            time.sleep(2)
            load_expense(filename)
        elif choice ==5: 
            print('Quitting !!!')
            time.sleep(2)
            break
        else: 
            print('Please enter the valid choice')
    

if __name__ == "__main__": 
    main()