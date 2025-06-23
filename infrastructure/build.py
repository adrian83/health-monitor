
import argparse

from scripts.aws_cloudformation import create_or_update_stack
from scripts.aws_ecr import get_auth_data, get_registry_url
from scripts.command import execute
from scripts.docker import docker_login, docker_logout, upload_images



IMAGES = {
    "health-monitor-mock-iot-events": "1.0.0-SNAPSHOT"
}

parser = argparse.ArgumentParser(description='Script for building AWS infrastructure for Health-Monitor app')
parser.add_argument('--email', type=str, required=True, help='Address that will receive SNS alerts')
args = parser.parse_args()

print("PARAMS")
print(f"EMAIL: {args.email}")

execute('sudo systemctl start docker')

#execute('mvn -Pnative spring-boot:build-image', dir='../health-monitor')

create_or_update_stack("health-monitor-alerts", "./cloudformation/100_alarms.yaml", params={"AlertEmail": args.email})
create_or_update_stack("health-monitor-ecr", "./cloudformation/120_ecr.yaml", params={})
create_or_update_stack("health-monitor-iot-core", "./cloudformation/150_iot_core.yaml", params={})

# (username, password, proxy_endpoint) = get_auth_data()
# docker_login(username, password, proxy_endpoint)
# registry_url = get_registry_url()

# for repo, tag in IMAGES.items():
#     print(f"pushing image: {repo}:{tag} into ECR repository")
#     upload_images(registry_url, repo, tag)

# docker_logout(proxy_endpoint)

#  TopicArn: !Sub "{{resolve:ssm:/alerting/sns/topicArn:1}}"

