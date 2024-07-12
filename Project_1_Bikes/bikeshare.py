import time
import pandas as pd
import numpy as np
import math

CITY_DATA = { 'chicago': 'C:/My Python/all-project-files/chicago.csv',
              'new york city': 'C:/My Python/all-project-files/new_york_city.csv',
              'washington': 'C:/My Python/all-project-files/washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True: 
        print('--'*30)
        city = input('Please enter the city you would like to anayze:').strip().lower()
        
        if city in CITY_DATA:
            print('--'*30)
            print('You have selected {}'.format(city.title()))
            break
        else : 
            print('Please type valid city name like chicago , new york city, washington')
    # get user input for month (all, january, february, ... , june)
 
    while True : 
        x = list(range(1,7))
        months = list(map(str, x))
        months_name = ['Janaury', 'Febraury', 'March', 'April', 'May', 'June','All'] 
        print('--'*30)  
        x = input('Enter any one of the first 6 months or enter All to select all 6 months :').title()
        if x in months:
            print('--'*30)
            print('You have selected {} st/nd/rd/th month'.format(x))
            month = x
            break
        elif x in months_name:
            print('--'*30)
            print('You have selected {} st/nd/rd/th month'.format(x))
            month = months_name.index(x) + 1
            break
        else : 
            short_month = [i[:3] for i in months_name ]
            if x in short_month:
                print('--'*30)
                print('You have selected {} st/nd/rd/th month'.format(x))
                month = short_month.index(x) +1
                break
            else:
                print('--'*30)
                print('Please type the valid month as shown in below: ')
                print(months, months_name)

    # get user input for day of week (all, monday, tuesday, ... sunday)
    while True: 
        days= {'Wed':'Wednesday','Sat':'Saturday', 'Tue':'Tuesday','Sun':'Sunday','Mon':'Monday','Fri':'Friday','Thu':'Thursday','All':'All'}
        print('--'*30)
        day =input('Please enter the day name you want to filter, else write all :').title()
        
        if day in days.values():
            print('--'*30)
            print('You have selected :{} day/days'.format(day.title()))
            break
        elif day in days.keys():
            day = days[day]
            print('--'*30)
            print('You have selected :{} day/days'.format(day.title()))
            break
        else :
            print('Please type valid day name: ')
    

    print('-'*40)
    return city, month, day


def load_data(city,month,day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    citypath = CITY_DATA[city]
    df = pd.read_csv(citypath)
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['Month'] = pd.DatetimeIndex(df['Start Time']).month
    df['Day of Week'] = df['Start Time'].dt.day_name()
    df['Start Hour'] = df['Start Time'].dt.hour
    if month !='All' and day !='All':
        df = df[(df['Month']==int(month)) & (df['Day of Week']==day.title())]   
    elif month =='All' and day != 'All':
        df['Month'] =df['Month']
        df = df[df['Day of Week']==day]
    elif month != 'All' and day =='All':
        df['Day of Week'] = df['Day of Week']

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""
    while True: 
        print('--'*30)
        show_stats = input("Do you want to see statistics on time stats? (yes/no): ").strip().lower()
        if show_stats == 'yes':
            print('\nCalculating The Most Frequent Times of Travel...\n')
            start_time = time.time()

            # display the most common month
            month = df['Month'].mode()[0]
            print('The most common month is : {} th'.format(month))
            # display the most common day of week
            day = df['Day of Week'].mode()[0]
            print('The most common day is : {}'.format(day))
            # display the most common start hour
            hour = df['Start Hour'].mode()[0]
            print('The most common start hour is : {} th '.format(hour))
            print("\nThis took %s seconds." % (time.time() - start_time))
            print('-'*40)
            break
        elif show_stats == 'no':
            # Exit the function
            return
        else:
            # Handle invalid input
            print("Invalid input. Please enter 'yes' or 'no'.")
        


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""
    while True:
        print('--'*30)
        show_stats = input("Do you want to see statistics on station stats? (yes/no): ").strip().lower()

        if show_stats == 'yes':
            print('\nCalculating The Most Popular Stations and Trip...\n')
            start_time = time.time()

            # display most commonly used start station
            Station_start = df['Start Station'].mode()[0]
            print('The most common start station is : {}'.format(Station_start))
            # display most commonly used end station
            Station_end = df['End Station'].mode()[0]
            print('The most common end station is : {}'.format(Station_end))
            # display most frequent combination of start station and end station trip
            Station_common = (df['Start Station'] + ' TO ' + df['End Station']).mode()[0]
            print('The most common commuting station is : {}'.format(Station_common))
            
            print("\nThis took %s seconds." % (time.time() - start_time))
            print('-'*40)
            break
        elif show_stats == 'no':
            # Exit the function
            return
        else:
            # Handle invalid input
            print("Invalid input. Please enter 'yes' or 'no'.")

def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""
    while True:
        print('--'*30)
        show_stats = input("Do you want to see statistics on trip duration? (yes/no): ").strip().lower()
        if show_stats == 'yes':
            print('\nCalculating Trip Duration...\n')
            start_time = time.time()

            # display total travel time
            Total_travel =  math.ceil(df['Trip Duration'].sum() /3600)
            print('The total travel time is : {} hours'.format(Total_travel))
            # display mean travel time
            Mean_travel =df['Trip Duration'].mean() 
            print('The mean travel time is : {} seconds'.format(Mean_travel))
            
            print("\nThis took %s seconds." % (time.time() - start_time))
            print('-'*40)
            break
        elif show_stats == 'no':
            # Exit the function
            return
        else:
            # Handle invalid input
            print("Invalid input. Please enter 'yes' or 'no'.")

def user_stats(df):
    """Displays statistics on bikeshare users."""
    print('--'*30)
    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    usercount = df['User Type'].value_counts()
    print('Here are user types and their counts : {}'.format(usercount))
    # Display counts of gender
    try:
        gen_count = df['Gender'].value_counts()
        print('Here are the gender counts : {}'.format(gen_count))
         # Display earliest, most recent, and most common year of birth
        earliest = df['Birth Year'].min()
        most_rescent = df['Birth Year'].max()
        most_common = df['Birth Year'].mode()[0]
        print('--'*40)
        print('The oldest to travel is {:.0f} born , youngest is {:.0f} born, most common is {:.0f} born'.format(earliest, most_rescent,most_common))
        print('--'*40)
    except KeyError: 
        print("The gender and birth year column is not in this file")
        print("\nThis took %s seconds." % (time.time() - start_time))
        print('-'*40)
        


def display_raw_data(df):
    #Displays the raw data of bikeshare
    row=0
    pd.set_option('display.max_columns',200)
    print('--'*30)
    raw = input('Do you want to see the raw data, please proceed with (yes/no) :').strip().lower()
    while True : 
        if raw =='no': 
            break
        elif raw =='yes':
            end = row+5
            for i in range(row,end): 
                print(df.iloc[i])
                print('--'*25)
        raw_again = input('Do you want to see next 5 rows (yes/no):').strip().lower()
        if raw_again !='yes': 
            break 
        row+=5

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        display_raw_data(df)
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
