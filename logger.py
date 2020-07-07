
import boto3
import datetime
import time
import argparse

from datetime import datetime

timestamp = int(round(time.time() * 1000))
client = boto3.client('logs')
#
# tok = client.describe_log_streams(
#     logGroupName='/aws/ec2/tonnyed',
#     orderBy='LastEventTime',
#     descending=True
# )
loggroup = "/aws/ec2/tonnyed"
logstream = 'testing'
# print(tok)

def get_token (loggroup):
    client = boto3.client('logs')
    token = client.describe_log_streams(logGroupName=loggroup)
    response = token['logStreams'][0]['uploadSequenceToken']

    return response




def put_log(log_group,log_stream,message):
    client = boto3.client('logs')
    response = client.put_log_events(
    logGroupName=log_group,
    logStreamName=log_stream,
    logEvents=[
        {
            'timestamp': timestamp,
            'message': message
        },
    ],
    sequenceToken=get_token(loggroup)
    )
    result = response['ResponseMetadata']['HTTPStatusCode']
    if result == 200:
        print(response)
        return True
    else:
        return False



#######################################################################
#############command line arg parcer for log group collector###########
#######################################################################

logger_parcer = argparse.ArgumentParser(description="logger parcer")

logger_parcer.add_argument("-msg", "--message", help="captured message")
logger_parcer.add_argument("-lg", "--loggroup", help="cloudwatch log group")
logger_parcer.add_argument("-ls", "--logstream", help="cloudwatch log stream")

args = logger_parcer.parse_args()


if not args.message:
    print("message needs to be set!")
    exit(1)
if not args.logstream:
    print("logstream needs to be set!")
    exit(1)
if not args.loggroup == None and args.logstream == None:
    print("loggroup needs to be set!")
    exit(1)
else:
    # fire = put_log(args.loggroup, args.logstream, args.message)
    # print(fire)
    print("fire down")



