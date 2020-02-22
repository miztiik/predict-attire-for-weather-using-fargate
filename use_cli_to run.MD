# AWS Fargate Weather Prediction App

1. ## Create a Cluster

    ```bash
    aws ecs create-cluster --cluster-name fargate-cluster
    ```

1. ## Register Task Definition

    Use the file given in the `configs` directory

    ```bash
    aws ecs register-task-definition \
      --cli-input-json file://configs/task_definition.json \
      --cluster-name fargate-cluster
    ```

1. ## List Task Definitions

    ```bash
    aws ecs list-task-definitions
    ```

    Output,

    ```json
    {
        "taskDefinitionArns": [
            "arn:aws:ecs:region:aws_account_id:task-definition/sample-fargate:1",
            "arn:aws:ecs:region:aws_account_id:task-definition/sample-fargate:2"
        ]
    }
    ```

    **NOTE:** Copy the latest verion number, as it is important for setting up the service in the following steps

1. ## Create a Service

    - Use the latest version obtained from the _List Task Definitions_ step.
    - Update the Subnet & Security Group for your cluster VPC
        - Remember to update your security group to allow port 80 traffic

    ```bash
    aws ecs create-service --cluster fargate-cluster \
        --service-name fargate-service \
        --task-definition sample-fargate:2 \
        --desired-count 2 \
        --launch-type "FARGATE" \
        --network-configuration "awsvpcConfiguration={subnets=[subnet-abcd1234],securityGroups=[sg-abcd1234]}"
    ```
