#!/bin/bash

#aws logs put-log-events --log-group-name "/aws/ec2/tonnyed" --log-stream-name testing --log-events "[{\"timestamp\":`date +%s%3N`, \"message\": \"Simple ElasticSearch Test\"}]"
python logger.py -msg=hello --loggroup=testing -ls=stream
python logger.py -msg=hello --loggroup=testing -ls=stream
python logger.py -msg=hello --loggroup=testing -ls=stream
