from kubernetes import client, config

# Load the Kubernetes configuration
config.load_kube_config()

# Create an instance of the AppsV1Api
api_instance = client.AppsV1Api()

# Define the deployment configuration
deployment = client.V1Deployment(
    metadata=client.V1ObjectMeta(name="my-deployment"),
    spec=client.V1DeploymentSpec(
        replicas=3,
        selector=client.V1LabelSelector(
            match_labels={"app": "my-app"}
        ),
        template=client.V1PodTemplateSpec(
            metadata=client.V1ObjectMeta(
                labels={"app": "my-app"}
            ),
            spec=client.V1PodSpec(
                containers=[
                    client.V1Container(
                        name="my-container",
                        image="nginx:latest"
                    )
                ]
            )
        )
    )
)

# Create the deployment in the specified namespace
api_instance.create_namespaced_deployment(
    namespace="my-namespace",
    body=deployment
)
