import os 
import csv 
import time
def add_expense(existing_list = None): 
    if existing_list is None: 
        existing_list = []
    date= str(input('PLEASE ENTER THE DATE OF EXPENSE (YYYY-MM-DD) :'))
    category = str(input('PLEASE ENTER THE RELATED CATEGORY :'))
    amt= float(input('ENTER THE AMOUNT SPENT in  :'))
    desc= str(input('ENTER THE BRIEF DESCRIPTION : '))
    # expense_value=[date, category, amt, desc]
    expense_dict = {'Date':date, 'Category':category,'Amount':amt,'Description':desc}
    existing_list.append(expense_dict)
    return existing_list

def view_expense(expense): 
    global expense_dict_keys 
    expense_dict_keys= ['Date','Category','Amount','Description']
    expense_len = len(expense)
    if expense_len ==0:
        return 'No entries added in this expenses'
    else:
        print(f'There are {expense_len} entries in this expense list. ')
        for i in range(expense_len): 
            if all(map(lambda x: x in expense_dict_keys, expense[i]))== True:
                print('-~'*40)
                print(f' ENTRY -- {i+1}')
                print('-~'*40) 
                if '' in expense[i].values():
                    print('-'*40)
                    print('Expense contains Missing Value, please update the records')
                    print('-'*40) 
            
                else : 
                    for key, value in expense[i].items(): 
                        print(f' {key}----> {value}')
            else: 
                print('Please update the record attributes')

def set_budget(budget=None): 
    if budget==0 or budget ==None: 
        budget = float(input('Please enter the budget for this month:'))
    return budget
    

def track_budget(budget, expense):
    total_spend = 0 
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
        writer = csv.DictWriter(f, fieldnames=expense_dict_keys)
        if not file_exists:
            writer.writeheader()
        writer.writerows(expense)
    return f'Expenses saved to {filename}'  

def load_expense(filename): 
    file_exists = os.path.isfile(filename)
    if not file_exists: 
        return 'Expense File doesnot exist'
    else: 
        with open(filename, 'r') as f: 
            reader = csv.DictReader(f)
            data= list(reader)
    print(data)

def main():
    while True:  
        print('~-'*40)
        print('-------PERSONAL TRACKER HOMEPAGE-------')
        print('~-'*40)
        print(' 1. ADD EXPENSE\n 2. VIEW EXPENSE\n, 3. TRACK BUDGET\n, 4. SAVE EXPENSES\n, 5. EXIT\n')
        choice = int(input('Please choose the options(1,2,3,4,5): '))
        
        if choice == 1 : 
            print('Executing Adding Expense--->')
            exp = add_expense()
            print('Expense successfully added')
        elif choice==2:
            print('Executing View Expenses--->')
            view_expense(expense=exp)
        elif choice ==3: 
            print('Executing Track Budget--->')
            bud = set_budget()
            track_budget(bud,exp)
        elif choice ==4:
            print('Executing Save Expenses--->')
            filename = input('Please enter the filename(add .csv also): ')

            save_expense(filename=filename, expense= exp)
            print('File Saved Successfully, Loading the data now...')
            time.sleep(2)
            load_expense(filename=filename)
        elif choice ==5: 
            print('Quitting !!!')
            time.sleep(2)
            break
        else: 
            print('Please enter the valid choice')
    

if __name__ == "__main__": 
    main()