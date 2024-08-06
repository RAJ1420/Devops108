
import boto3
from datetime import datetime
 
# Initialize a session using Amazon Cost Explorer
client = boto3.client('ce')
 
# Define the time period for the cost report
start_date = '2024-08-01'
end_date = '2024-08-05'
 
# Get cost and usage for the specified period
response = client.get_cost_and_usage(
    TimePeriod={
        'Start': start_date,
        'End': end_date
    },
    Granularity='DAILY',
    Metrics=['UnblendedCost']
)
 
# Parse and display the results
costs = response['ResultsByTime']
 
total_cost = 0.0
for day in costs:
    date = day['TimePeriod']['Start']
    amount = float(day['Total']['UnblendedCost']['Amount'])
    total_cost += amount
    print(f"Date: {date}, Cost: ${amount:.2f}")
 
print(f"\nTotal cost from {start_date} to {end_date}: ${total_cost:.2f}")
 
