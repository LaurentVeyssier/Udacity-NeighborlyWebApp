# Udacity project - Azure Serverless Application with back-end Functions and Flask Webapp Front-end

This project is part of Udacity Cloud Developer on Azure Nanodegree.

It summarizes the third module dedicated to Azure Microservices. In this module, we cover Serverless functions (FunctionApps, WebApps,...), Logic Apps and Event Grid / Hub as well as Deployment (serverless, containerization with Docker and deployment to Kubernetes) plus security features. There are lots of hand-on practice culminating with this final project.

The purpose of the project is to deploy a Flask web application hosting both ads and posts. The app operates CRUD capabilities (Create, Read, Update, Delete) using a CosmosDB database and azure functions in the back-end. From this serverless architecture, the back-end functions are containerized and deployed to a Kubernetes cluster as an alternative.

Implemented Azure ressources in the project:
- Cosmos DB
- FunctionApp (http triggered functions)
- Webapp
- EventHub
- LogicApp with SendGrid
- Azure Container Registry for Docker images
- Kubernetes deployment

# Output

- Front-end webapp

![](screenshots/live_frontend_deployed.jpg)

- back-end live on Kubernetes cluster

![](screenshots/kubernetes_funcapp_deployment_confirmation.jpg)

- LogicApp triggered notice using SendGrid email service

![](screenshots/httpTrigger_emails.jpg)

- Some of the implemented resources

![](screenshots/ressource_group.jpg)
