import json
import boto3


class Writeprocess(object):
    def __init__(self,event):
        self.dynamodb = None
        self.event = event
        self.tableCurrent = None
        self.event = self.event["body"]
        self.event = json.loads(self.event)

    def dbconnect(self):
        print("Inside DB connection")
        self.dynamodb = boto3.resource('dynamodb',
                           endpoint_url='http://192.168.0.149:8000',
                           region_name = 'dummy',
                           aws_secret_access_key = 'dummy',
                           aws_access_key_id = 'dummy')
        print("Done Client Creation")
        self.tableCurrent = self.dynamodb.Table('tabmine')
    
    def process(self):
        print("Inside Processing")
        #Fetch data from request
        
        title = self.event['title']
        description = self.event['description']
        date = self.event['date']
        try:
            self.tableCurrent.put_item(
            Item={
                    'Title': title,
                    'description': description,
                    'date': date
                }
            )
            
            return {
                'statusCode': 200,
                'body': json.dumps('Succesfully inserted record for Announcement Title --> {}'.format(title))
            }
        except Exception as error:
            print('Closing lambda function')
            print(error)
            return {
                    'statusCode': 400,
                    'body': json.dumps('Error saving the record due to --> {}'.format(error))
            }      

def handler(event, context):
    print("This is Write Function")
    #Connect DynamoDB
    read = Writeprocess(event)
    read.dbconnect()
    response = read.process()
    return response

    


    