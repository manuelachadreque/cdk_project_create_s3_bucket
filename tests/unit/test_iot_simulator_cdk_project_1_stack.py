import aws_cdk as core
import aws_cdk.assertions as assertions

from iot_simulator_cdk_project_1.iot_simulator_cdk_project_1_stack import IotSimulatorCdkProject1Stack

# example tests. To run these tests, uncomment this file along with the example
# resource in iot_simulator_cdk_project_1/iot_simulator_cdk_project_1_stack.py
def test_sqs_queue_created():
    app = core.App()
    stack = IotSimulatorCdkProject1Stack(app, "iot-simulator-cdk-project-1")
    template = assertions.Template.from_stack(stack)

#     template.has_resource_properties("AWS::SQS::Queue", {
#         "VisibilityTimeout": 300
#     })
