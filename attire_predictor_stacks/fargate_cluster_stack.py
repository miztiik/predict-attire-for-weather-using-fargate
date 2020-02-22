from aws_cdk import aws_ecs_patterns as _ecs_patterns
from aws_cdk import aws_ec2 as _ec2
from aws_cdk import aws_ecs as _ecs
from aws_cdk import core


class AttirePredictorStack(core.Stack):

    def __init__(self, scope: core.Construct, id: str, custom_vpc, ** kwargs) -> None:
        super().__init__(scope, id, **kwargs)

        # The code that defines your stack goes here
        fargate_cluster = _ecs.Cluster(self,
                                       "fargateClusterId",
                                       vpc=custom_vpc)

        # Export resource name. You can import in another stack if required
        core.CfnOutput(self, "ClusterNameOutput",
                       value=f"{fargate_cluster.cluster_name}", export_name="ClusterName")

        weather_svc_task_def = _ecs.FargateTaskDefinition(
            self, "weatherTaskDefId")

        weather_container = weather_svc_task_def.add_container("weatherContainer",
                                                               environment={
                                                                   'PLATFORM': 'Mystikal Fargate World :-)'
                                                               },
                                                               image=_ecs.ContainerImage.from_registry(
                                                                   "mystique/predict-attire-for-weather"),
                                                               memory_limit_mib=256,
                                                               cpu=256,
                                                               entry_point=["gunicorn", "--bind", "0.0.0.0:80", "--bind", "0.0.0.0:443", "wsgi:application",
                                                                            "--access-logfile", "-", "--error-logfile", "-", "--capture-output", "--enable-stdio-inheritance"],
                                                               logging=_ecs.LogDrivers.aws_logs(
                                                                   stream_prefix="Mystique")
                                                               )

        weather_container.add_port_mappings(
            _ecs.PortMapping(container_port=80)
        )
        weather_container.add_port_mappings(
            _ecs.PortMapping(container_port=443)
        )

        weather_service = _ecs_patterns.ApplicationLoadBalancedFargateService(
            self, "weatherServiceId",
            cluster=fargate_cluster,
            task_definition=weather_svc_task_def,
            assign_public_ip=False,
            public_load_balancer=True,
            listener_port=80,
            desired_count=2,
            cpu=256,
            memory_limit_mib=512,
            service_name="weatherService",
        )

        # Export resource name. You can import in another stack if required
        core.CfnOutput(
            self, "WeatherServiceUrl", value=f"http://{weather_service.load_balancer.load_balancer_dns_name}")

        """
        Service running plain old nginx

        nginx_task_def = _ecs.FargateTaskDefinition(self, "nginxTaskDef")

        nginx_container = nginx_task_def.add_container("nginxContainer",
                                                       environment={
                                                           'PLATFORM': 'Mystikal Fargate World :-)'
                                                       },
                                                       image=_ecs.ContainerImage.from_registry(
                                                           "nginx:latest"),
                                                       memory_limit_mib=256,
                                                       cpu=256,
                                                       logging=_ecs.LogDrivers.aws_logs(
                                                           stream_prefix="Mystique")
                                                       )

        nginx_container.add_port_mappings(
            _ecs.PortMapping(container_port=80, protocol=_ecs.Protocol.TCP)
        )

        nginx_service = _ecs_patterns.ApplicationLoadBalancedFargateService(
            self, "nginxServiceId",
            cluster=fargate_cluster,
            task_definition=nginx_task_def,
            assign_public_ip=False,
            public_load_balancer=True,
            listener_port=80,
            desired_count=1,
            cpu=256,
            memory_limit_mib=512,
            service_name="nginxService",
        )
        """
