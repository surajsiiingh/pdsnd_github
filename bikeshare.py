import time
import pandas as pd
import numpy as np

CITY_DATA = {'chicago': 'chicago.csv',
             'new york city': 'new_york_city.csv',
             'washington': 'washington.csv'}


def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True:
        city = (str(input("Enter the name of city  "))).lower()
        if city == 'chicago' or city == 'new york city' or city == 'washington':
            break
        else:
            print("You entered the wrong city please enter the input again :")

    # TO DO: get user input for month (all, january, february, ... , june)
    months = ['january', 'february', 'march', 'april', 'may', 'june', 'july', 'agust', 'september', 'october', 'november', 'december','all']

    while True:
        month = (str(input("Enter the name of the month (january, february, ... , june) to filter by, or 'all' to apply no month filter\n"))).lower()
        if month in months:
            break
        else:
            print('You entered the wrong month please enter the input again :')
    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    days = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday', 'all']

    while True:
        day = (str(input("Enter the name of the day of week to filter by, or 'all' to apply no day filter\n")).lower())

        if day in days:
            break
        else:
            print('You entered the wrong day please enter the input again :')

    print('-' * 40)
    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    df = pd.read_csv(CITY_DATA[str(city)])

    df['Start Time'] = pd.to_datetime(df['Start Time'])

    df['month'] = df['Start Time'].dt.month

    df['day_of_week'] = df['Start Time'].dt.weekday_name
    if month != 'all':
        months = ['january', 'february', 'march', 'april', 'may', 'june', 'july', 'agust', 'september', 'october', 'november', 'december']
        month = months.index(month) + 1
        df = df[df['month'] == month]

    if day != 'all':
        df = df[df['day_of_week'] == day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()
    months = ['january', 'february', 'march', 'april', 'may', 'june', 'july', 'agust', 'september', 'october', 'november', 'december']

    # TO DO: display the most common month
    common_month = df['month'].value_counts().index[0]
    common_month = months[common_month - 1]
    print("Most common month ", common_month)
    # TO DO: display the most common day of week
    common_day = df['day_of_week'].value_counts().index[0]
    print("Most common day of week is ", common_day)
    # TO DO: display the most common start hour
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['hour'] = df['Start Time'].dt.hour

    common_hour = df['hour'].value_counts().index[0]
    print("Most common start hour is ", common_hour)
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    common_sstation = df['Start Station'].value_counts().index[0]
    print("Most commonly used start station is ", common_sstation)

    # TO DO: display most commonly used end station
    common_estation = df['End Station'].value_counts().index[0]
    print("Most commonly used end station is ", common_estation)
    # TO DO: display most frequent combination of start station and end station trip
    start_end = df[df['Start Station'] == df['End Station']]
    trip = start_end['Start Station'].value_counts().index[0]
    print("Most frequent combination of start station and end station trip is ", trip)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_time = df['Trip Duration'].sum()
    print("Total travel time is ", total_time)
    # TO DO: display mean travel time
    mean_time = df['Trip Duration'].mean()
    print("Average time is ", mean_time)
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()
    user_types = df['User Type'].value_counts()
    # TO DO: Display counts of user types
    print(user_types.index[0], user_types[0])
    print(user_types.index[1], user_types[1])

    # TO DO: Display counts of gender
    if 'Gender' in df.columns:
        gender = df['Gender'].value_counts()
        print(gender.index[0], gender[0])
        print(gender.index[1], gender[1])

        # TO DO: Display earliest, most recent, and most common year of birth
        birth_year = df['Birth Year'].value_counts()

        print("Most common year of birth is ", birth_year.index[0])

        earliest_birth = birth_year.sort_index(ascending=True).index[0]
        print("Earliest year of birth is ", earliest_birth)

        recent_birth = birth_year.sort_index().index[0]
        print("Most recent  year of birth is ", recent_birth)
    else:
        print("There is no Gender and Birth Year column in this data")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)


def raw_data(city):
    """display descriptive statistics on bikeshare data"""
    df = pd.read_csv(CITY_DATA[str(city)])
    print("Displaying descriptive statistics \n")
    print(df.describe())

    i=1
    j=5
    while True:
        response=(str(input("Dou want see the data one by one \n"))).lower()
        if response =='yes':
            while i<j:
                print(df.iloc[i])
                print('-'*50)
                i=i+1
        
            i=i
            j=j+5
        else :
            break


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        raw_data(city)
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
    main()
