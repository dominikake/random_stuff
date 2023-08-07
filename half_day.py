from datetime import datetime, timedelta

def calculate_midpoint(start_hour, end_hour):
    # Convert input strings to datetime objects
    start_time = datetime.strptime(start_hour, '%I:%M %p')
    end_time = datetime.strptime(end_hour, '%I:%M %p')
    
    # Define lunch break duration
    lunch_break = timedelta(hours=1)
    
    # Calculate the duration of the work period (excluding lunch)
    work_duration = end_time - start_time + lunch_break
    
    # Calculate the midpoint by adding half of the work duration to the start time
    midpoint = start_time + work_duration / 2
    
    return midpoint.strftime('%I:%M %p')

# Define start and end hours
start_hour = '9:00 AM'
end_hour = '7:00 PM'

# Calculate and print the midpoint
midpoint = calculate_midpoint(start_hour, end_hour)
print(f"The midpoint between {start_hour} and {end_hour} is {midpoint}.")
