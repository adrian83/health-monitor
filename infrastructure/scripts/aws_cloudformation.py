
import json

import boto3
import botocore


cf = boto3.client('cloudformation')


def create_stack(name: str, template_path: str, params: dict[str, str]=None, tags: dict[str, str]=None):
    parameters = [{'ParameterKey': key, 'ParameterValue': value} for key, value in params.items()] if params else []
    tags = [{'Key': key, 'Value': value} for key, value in tags.items()] if tags else []

    with open(template_path, 'r') as f:
        template_body = f.read()

    response = cf.create_stack(
        StackName=name,
        TemplateBody=template_body,
        Parameters=parameters,
        Capabilities=['CAPABILITY_NAMED_IAM'],
        OnFailure='ROLLBACK',
        Tags=tags
    )

    print(f"Stack creation initiated: {response['StackId']}")

    waiter = cf.get_waiter('stack_create_complete')
    print(f"Waiting for stack {name} to finish creating...")
    waiter.wait(StackName=name)
    print(f"Stack {name} created successfully.")


def delete_stack(stack_name):
    cf.delete_stack(StackName=stack_name)

    waiter = cf.get_waiter('stack_delete_complete')
    print(f"Waiting for stack {stack_name} to be deleted...")
    waiter.wait(StackName=stack_name)
    print(f"Stack {stack_name} deleted successfully.")


def delete_stack_if_exists(stack_name):
    try:
        cf.describe_stacks(StackName=stack_name)
        delete_stack(stack_name)
    except botocore.exceptions.ClientError as error:
        if 'does not exist' in str(error):
            print(f"Stack {stack_name} nie istnieje, nic nie robię.")
        else:
            raise error
