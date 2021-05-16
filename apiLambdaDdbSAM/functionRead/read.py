import json
import boto3
   
class Readprocess(object):
    def __init__(self,event):
        self.dynamodb = None
        self.outputMain = []
        self.event = event
        print(self.event)
        try:
            self.pagination = True
            self.limit = event['queryStringParameters']['limit']
            self.page = event['queryStringParameters']['page']
        except: 
            self.pagination = False

    def dbconnect(self):
        print("Inside DB connection")
        self.dynamodb = boto3.resource('dynamodb',
                           endpoint_url='http://192.168.0.149:8000',
                           region_name = 'dummy',
                           aws_secret_access_key = 'dummy',
                           aws_access_key_id = 'dummy')
        print("Done Client Creation")
    
    def process(self):
        print("Inside Processing")
        try:
            #Scan DynamoDB
            tableTemperature = self.dynamodb.Table('tabmine')
            scan = tableTemperature.scan(TableName = 'tabmine')
            print("scan")
            print(scan)
            output = scan['Items']
            print(output)
            for item in output:
                self.outputMain.append(item)
                print(item)
            if self.pagination :
                end = int(self.limit) * int(self.page)
                start = end - int(self.limit)
                print(end)
                print(start)
                self.outputMain = self.outputMain[start:end]
                if len(self.outputMain) == 0:
                    return self.errorhandling("Requested page doesnt exist",404)
                else:
                    response = {
                    'statusCode': 200,
                    'body': "Page-->{} & Limit-->{}".format(self.page,self.limit) + json.dumps(self.outputMain)
                    }
            else:
                response = {
                    'statusCode': 200,
                    'body': json.dumps(self.outputMain)
                    }            
            return response
        except Exception as error:
            self.errorhandling(error)
            
    def errorhandling(self,error,statusCode = 400):
        #Error Handing
        print('Closing lambda function')
        print(error)
        return {
                'statusCode': statusCode,
                'body': json.dumps('Error fetching the record due to -->{}'.format(error))
        } 
def handler(event, context):
    print("This is Read Function")
    #Connect DynamoDB
    read = Readprocess(event)
    read.dbconnect()
    response = read.process()
    return response