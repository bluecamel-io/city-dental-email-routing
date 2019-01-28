rm ./lambda.zip
zip -r9 ./lambda.zip ./emailRoutingLambda-venv/lib/python3.6/site-packages/ 
zip -g ./lambda.zip ./lambda.py
aws lambda update-function-code --region us-east-1 --function-name cityDentalEmailRoutingLambda --zip-file fileb://lambda.zip
