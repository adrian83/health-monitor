
import argparse

from scripts.aws_cloudformation import create_stack



parser = argparse.ArgumentParser(description='Script for building AWS infrastructure for Health-Monitor app')

parser.add_argument('--email', type=str, required=True, help='Address that will receive SNS alerts')

args = parser.parse_args()

print("PARAMS")
print(f"EMAIL: {args.email}")


create_stack("health-monitor-alerts", "./100_alarms.yaml", params={"AlertEmail": args.email})


#  TopicArn: !Sub "{{resolve:ssm:/alerting/sns/topicArn:1}}"