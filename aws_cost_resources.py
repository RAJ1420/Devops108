import boto3
from datetime import datetime, timedelta

# Initialize a session using Amazon Cost Explorer
client = boto3.client('ce')

# Function to get the cost for a specific day
def get_cost_for_day(start_date, end_date):
    response = client.get_cost_and_usage(
        TimePeriod={
            'Start': start_date,
            'End': end_date
        },
        Granularity='DAILY',
        Metrics=['UnblendedCost'],
        GroupBy=[
            {
                'Type': 'DIMENSION',
                'Key': 'SERVICE'
            },
        ]
    )
    return response

# Function to format the date
def format_date(date):
    return date.strftime('%Y-%m-%d')

# Set the date range
start_date = datetime(2024, 8, 1)
end_date = datetime(2024, 8, 8)

# Iterate over each day in the range
current_date = start_date
while current_date < end_date:
    next_date = current_date + timedelta(days=1)
    formatted_start_date = format_date(current_date)
    formatted_end_date = format_date(next_date)
    
    # Get the cost for the current day
    response = get_cost_for_day(formatted_start_date, formatted_end_date)
    
    # Print the cost for each resource
    print(f"Cost for {formatted_start_date}:")
    for result in response['ResultsByTime']:
        for group in result['Groups']:
            service = group['Keys'][0]
            cost = group['Metrics']['UnblendedCost']['Amount']
            print(f"  {service}: ${cost}")
    
    # Move to the next day
    current_date = next_date