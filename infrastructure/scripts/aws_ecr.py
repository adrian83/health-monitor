import base64
import sys

import boto3

from scripts.command import execute


ecr = boto3.client("ecr")


def get_auth_data():
    auth_data = ecr.get_authorization_token()["authorizationData"][0]
    token = base64.b64decode(auth_data["authorizationToken"]).decode()
    username, password = token.split(":")
    proxy_endpoint = auth_data["proxyEndpoint"]
    return (username, password, proxy_endpoint)



def get_registry_url():
    account_id = boto3.client("sts").get_caller_identity()["Account"]
    region = boto3.session.Session().region_name
    ecr_url = f"{account_id}.dkr.ecr.{region}.amazonaws.com"
    return ecr_url

