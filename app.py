#!/usr/bin/env python3

from aws_cdk import core

from predict_attire_for_weather_using_fargate.predict_attire_for_weather_using_fargate_stack import PredictAttireForWeatherUsingFargateStack


app = core.App()
PredictAttireForWeatherUsingFargateStack(app, "predict-attire-for-weather-using-fargate")

app.synth()
