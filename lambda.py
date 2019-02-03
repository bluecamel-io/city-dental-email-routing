import email
import json
import logging

import boto3
from botocore.exceptions import ClientError


## constants

BLOOR_W_FLAG = 2
BLOOR_W_MAIL = 'admin@citydentalbloorwest.com'

YONGE_FLAG = 1
YONGE_MAIL = 'admin@citydentalonyonge.com'

BAY_FLAG = 2
BAY_MAIL = 'admin@citydentalonbay.com'


## configuration

s3 = boto3.client('s3')
ses = boto3.client('ses')

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

## lambda body

def find_destination(body):
    '''Parses the email content to determine which location to route the message to.'''
    pass

def lambda_handler(event, context):
    print('it worked')
    return

    record = event['Records'][0]
    assert record['eventSource'] == 'aws:ses'

    body = record['ses']['mail']['content']
    body = email.message_from_bytes(body)

    logger.info(body)

    ## extract final message destination
    #destination = xyz

    try:
        o = ses.send_raw_email(Destinations=[destination], RawMessage=dict(Data=msg_string))
        logger.info('Forwarded email for <{}> to <{}>. SendRawEmail response={}'.format(recipient, address, json.dumps(o)))
        
    except ClientError as e:
        logger.error('Client error while forwarding email for <{}> to <{}>: {}'.format(recipient, address, e))
