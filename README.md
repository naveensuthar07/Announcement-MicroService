# Announcement-MicroService
# Owner - Naveen Suthar
# github-path - https://github.com/naveensuthar07/Announcement-MicroService/tree/main/apiLambdaDdbSAM

1. Pre-requisite 
	AWS SAM
	Docker
	Python3.8
	Git
	Postman

2. This project creates a serverless microservice for Announcement Read and Write API's
3. To start this setup the local environment for DynamoDB table using docker at path\apiLambdaDdbSAM using command "Docker-compose up"
4. Build and Deploy SAM template(This will run AWS serverless components locally)
	sam build
	sam local start-api
5. Testing 
	Write:
		send the below details in post request at path "http://locahost:3000/writedb"
		{"title":"Title Details",
		 "description":"Title Description",
		 "date":"date of the Announcement"}
		 
		Response: It will return response code 200 with appropriate response message
	
	Read:
		Full table scan: 
			Request : send the post request at path "http://locahost:3000/readdb"	
			Response : It will return response code 200 with all Announcement details
		Pagination : 
			Request : send the post request at path "http://locahost:3000/readdb?limit=5&page=1" where 
					Limit : It is used to limit the number of response
					Page: To get the requsted page 

6. Error handling
	Write: 
		In case of error API will return error code 400 with all error details.
	Read :
		In case of error API will return error code 400 with all error details.If given page doesn't Exist it will return the error code 404.

