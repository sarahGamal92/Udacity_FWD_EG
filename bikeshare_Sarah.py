from datetime import datetime
import time
import pandas as pd
import numpy as np

city = ""
day = ""
month = ""

CITY_DATA = {'chicago': 'chicago.csv',
             'new york': 'new_york_city.csv',
             'washington': 'washington.csv'}

days = ["saturday", "sunday", "monday",
        "tuesday", "wednesday", "thursday", "friday"]
months = ['january', 'february', 'march', 'april', 'may', 'june']

print('Hello! Let\'s explore some US bikeshare data!')


def get_filters(city, month, day):

    # get user input for city (chicago, new york city, washington)
    while True:
        user_city = input(
            'Please specify the city name you want to explore. You can choose from the following 3 options:\n1. Chicago \n2. New York\n3. Washington\n ')
        city = user_city.lower()
        print(city)
        if city in CITY_DATA.keys():
            break
        else:
            print("Your input doesn't match any of the suggested cities.")
            continue

    while True:
        day_or_month = input(
            'Do you want to filter by day, month, both or none?\n')
        day_or_month = day_or_month.lower()

        # get user input for month (from January to June)
        if day_or_month == 'month':
            # filter by month if applicable
            while True:
                month = input(
                    'Could you specify the month? Choose Between January & June:\n')
                if month.lower() not in months:
                    print('This does\'t seem to be correct input.')
                    continue
                else:
                    break
            day = "all"

        elif day_or_month == 'day':
            # filter by day if applicable
            while True:
                day = input(
                    'Could you specify the day?')
                if day.lower() not in days:
                    print('This does\'t seem to be correct input.')
                    continue
                else:
                    print(day)
                    break
            month = 'all'

        elif day_or_month == 'none':
            month = 'all'
            day = 'all'
            break

        elif day_or_month == 'both':
            while True:
                month = input(
                    'Could you specify the month? Choose Between January & June:\n')
                if month.lower() not in months:
                    print('This does\'t seem to be correct input.')
                    continue
                else:
                    break
            while True:
                day = input(
                    'Could you specify the day?')
                if day.lower() not in days:
                    print('This does\'t seem to be correct input.')
                    continue
                else:
                    print(day)
                    break

        else:
            print('This does\'t seem to be correct input.')
            continue

        break

    print('-'*40)
    return city, month, day


def load_data(city, month, day):

    # load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])

    # convert the Start Time column to datetime
    time_df = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = time_df.dt.month
    df['day_of_week'] = time_df.dt.day_name()

    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        month = months.index(month) + 1

        # filter by month to create the new dataframe with only the specified month
        df = df[df['month'] == month]

        # filter by day of week if applicable
    if day != 'all':
        df = df[(df['day_of_week']).str.lower() == day.lower()]

    print(df)
    # filter by day of week to create the new dataframe
    return df


def time_stats(df):

    start_time = time.time()
    """Displays statistics on the most frequent times of travel."""
    print('\n The Most Frequent Times of Travel (Based on your input)...\n')

    # TO DO: display the most common month
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['Month'] = df['Start Time'].dt.month
    popular_month = str(df['Month'].mode()[0])

    # Extract month name from integer
    datetime_object = datetime.strptime(popular_month, "%m")
    popular_month = datetime_object.strftime("%B")
    print("The most popular month is " + popular_month)

    # TO DO: display the most common day of week
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['Day of Week'] = df['Start Time'].dt.day_name()
    popular_day = df['Day of Week'].mode()[0]
    print("The most popular day of the week is " + str(popular_day))

    # TO DO: display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    popular_hour = df['hour'].mode()[0]
    print("The most popular hour is " + str(popular_hour)+":00")
    print("\nThis took %s seconds." % (time.time() - start_time))


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    common_start = df['Start Station'].mode()[0]
    print('The most common start station is ' + common_start)

    # TO DO: display most commonly used end station
    common_end = df['End Station'].mode()[0]
    print('The most common end station is ' + common_end)

    # TO DO: display most frequent combination of start station and end station trip
    stations_combined = df['Start Station'] + ' - ' + df['End Station']
    print('The most common trip is between: ' + stations_combined.mode()[0])

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_trip_duration = df['Trip Duration'].sum()

    # Convert seconds into days, hours, minutes
    day_ = total_trip_duration // (24 * 3600)
    total_trip_duration = total_trip_duration % (24 * 3600)
    hour = total_trip_duration // 3600
    total_trip_duration %= 3600
    minutes = total_trip_duration // 60
    total_trip_duration %= 60
    seconds = total_trip_duration

    print("Total trip duration is: %d days %d hrs %d mins %d secs" %
          (day_, hour, minutes, seconds))

    # TO DO: display mean travel time
    mean_trip_duration = df['Trip Duration'].mean()
    print("Mean trip duration is: " + str(mean_trip_duration) + " seconds")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_Types = df['User Type'].value_counts()
    print("User Types are:\n" + str(user_Types))
    
    # TO DO: Display counts of gender
    if 'Gender' in df:
        gender= df['Gender'].value_counts()

        print("Gender Distribution is:\n" + str(gender))
    
    # TO DO: Display earliest, most recent, and most common year of birth

    print("\nThis took %s seconds." % (time.time() - start_time))


def main():
    city = ""
    day = ""
    month = ""
    while True:
        city, month, day = get_filters(city, month, day)
        df = load_data(city, month, day)

        #time_stats(df)
        #station_stats(df)
        #trip_duration_stats(df)
        user_stats(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
    main()
