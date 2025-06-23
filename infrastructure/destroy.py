from scripts.aws_cloudformation import delete_stack_if_exists



delete_stack_if_exists("health-monitor-iot-core")
delete_stack_if_exists("health-monitor-ecr")
delete_stack_if_exists("health-monitor-alerts")
