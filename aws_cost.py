import boto3
from botocore.exceptions import NoCredentialsError, PartialCredentialsError, ClientError
from datetime import datetime
 
def get_cost_between_dates(start_date, end_date):
    try:
        print("Initializing boto3 client...")
        client = boto3.client('ce', region_name='us-east-1')
        print("Client initialized.")
 
        print(f"Requesting cost data from {start_date} to {end_date}...")
        response = client.get_cost_and_usage(
            TimePeriod={
                'Start': start_date,
                'End': end_date
            },
            Granularity='DAILY',
            Metrics=['BlendedCost']
        )
        print("Response received from AWS Cost Explorer.")
 
        for result in response['ResultsByTime']:
            time_period = result['TimePeriod']
            cost = result['Total']['BlendedCost']['Amount']
            print(f"From {time_period['Start']} to {time_period['End']}, the cost was ${cost}")
    except NoCredentialsError:
        print("Error: No AWS credentials found.")
    except PartialCredentialsError:
        print("Error: Incomplete AWS credentials found.")
    except ClientError as e:
        print(f"Client error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
 
if __name__ == "__main__":
    # Define the date range
    start_date = '2024-08-1'
    end_date = '2024-08-5'
 
    print("Script started")
    get_cost_between_dates(start_date, end_date)
    print("Script finished")
