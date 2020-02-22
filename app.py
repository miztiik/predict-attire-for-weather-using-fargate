#!/usr/bin/env python3

from aws_cdk import core


from attire_predictor_stacks.vpc_stack import CustomVpcStack
from attire_predictor_stacks.fargate_cluster_stack import AttirePredictorStack

app = core.App()

env_US = core.Environment(account=app.node.try_get_context('envs')['dev']['account'],
                          region=app.node.try_get_context('envs')['dev']['region'])

vpc_stack = CustomVpcStack(
    app, "mystique-attire-predictor-vpc-stack", env=env_US, add_nat_to_vpc=True)

attire_predictor_stack = AttirePredictorStack(
    app, "mystique-attire-predictor", env=env_US, custom_vpc=vpc_stack.custom_vpc)


app.synth()
