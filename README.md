# Project: Introduction to DevOps - Terraform, Docker, Kubernetes

## Overview

This project provides a foundational introduction to essential DevOps tools and practices, focusing on Terraform, Docker, and Kubernetes. Through hands-on tasks, you'll gain experience in infrastructure automation, containerization, and container orchestration.

## Tasks

### 1. EC2 Instance Creation

This task involves provisioning an EC2 instance on AWS and automatically installing Docker on it. This setup enables the deployment of containerized applications.

*   **Key Components:**
    *   AWS Template: Defines the infrastructure as code using Terraform.
    *   Docker Installation: Automated script to install Docker on the instance.
*   **Purpose:**
    *   Provision an EC2 instance.
    *   Install Docker for containerized deployments.

### 2. SQS Creation

This task focuses on creating an SQS (Simple Queue Service) queue within your AWS environment.

*   **Key Components:**
    *   SQS Queue: A message queue service for communication between applications.
*   **Purpose:**
    *   Establish a message queue for potential future integrations.

### 3. Role Creation

This task involves creating an IAM role designed for AWS Lambda functions.

*   **Key Components:**
    *   IAM Role: Defines permissions and access for Lambda functions.
*   **Purpose:**
    *   Set up a role to control Lambda function permissions.

### 4. Lambda Function

This task involves creating an AWS Lambda function to process messages and write data to a DynamoDB table.

*   **Key Components:**
    *   Lambda Function: Serverless compute service for running code.
    *   DynamoDB Interaction: Writing processed data to a DynamoDB table.
*   **Purpose:**
    *   Process messages.
    *   Store data in DynamoDB.

### 5. Sending Data from the UI

This task involves sending data to an SQS queue.

*   **Key Components:**
    *   SQS Client: Interacts with the SQS service.
    *   Message Data: Defines the content of the message.
*   **Purpose:**
    *   Send messages to the SQS queue.

## Additional Notes

*   **Snapshots:** The document includes snapshots of the SQS, Lambda function, IAM role, DynamoDB table, and CloudFormation stack.
*   **GitHub Repo:** The complete code for this project is available in the GitHub repository.
