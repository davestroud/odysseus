import boto3
import json

# Load the state machine definition
with open("step_functions/state_machine.json") as f:
    state_machine_definition = json.load(f)

stepfunctions_client = boto3.client("stepfunctions", region_name="us-east-1")

response = stepfunctions_client.create_state_machine(
    name='MySageMakerPipelineStateMachine',
    definition=json.dumps(state_machine_definition),
    roleArn='arn:aws:iam::123456789012:role/service-role/StepFunctions-ExecutionRole'
)

print(f"State Machine ARN: {response['stateMachineArn']}")
