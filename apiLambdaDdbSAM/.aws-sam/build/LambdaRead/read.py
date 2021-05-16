import json
import boto3

print('Loading function')


def handler(event, context):
    print("THis is Read Function")
    event = event["body"]
    event = json.loads(event)
    print(event)
    dynamodb = boto3.resource('dynamodb',
                           endpoint_url='http://192.168.0.149:8000',
                           region_name = 'dummy',
                           aws_secret_access_key = 'dummy',
                           aws_access_key_id = 'dummy')

    print("Done connection")
    try:
        outputMain = []
        tableTemperature = dynamodb.Table('tabmine')
        scan = tableTemperature.scan(TableName = 'tabmine')
        output = scan['Items']
        print(output)
        for item in output:
            outputMain.append(item)
            print(item)
        return {
            'statusCode': 200,
            'body': json.dumps(outputMain)
        }
    except Exception as error:
        print('Closing lambda function')
        print(error)
        return {
                'statusCode': 400,
                'body': json.dumps('Error saving the record')
        }



    #print("Received event: " + json.dumps(event, indent=2))
    