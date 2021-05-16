import json
import boto3


print('Loading function')


def handler(event, context):
    print("THis is Write Function")
    event = event["body"]
    event = json.loads(event)
    print(event)
	#Hosted Dynamo db on local
    dynamodb = boto3.resource('dynamodb',
                           endpoint_url='http://192.168.0.149:8000',
                           region_name = 'dummy',
                           aws_secret_access_key = 'dummy',
                           aws_access_key_id = 'dummy')

    print("Done connection")
    tableTemperature = dynamodb.Table('tabmine')
    title = event['title']
    description = event['description']
    date = event['date']
    try:
        
        tableTemperature.put_item(
           Item={
                'Title': title,
                'description': description,
                'date': date
            }
        )
        
        return {
            'statusCode': 200,
            'body': json.dumps('Succesfully inserted record!')
        }
    except Exception as error:
        print('Closing lambda function')
        print(error)
        return {
                'statusCode': 400,
                'body': json.dumps('Error saving the record')
        }



    #print("Received event: " + json.dumps(event, indent=2))
    