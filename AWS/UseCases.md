1.Deploy a Web Application to EC2 via CodePipeline
Source code in CodeCommit or GitHub
CodeBuild for build/test
CodeDeploy to roll out new versions to EC2 instances automatically

2.Deploy Static Website or Build Artifacts to S3
CodePipeline triggers on code changes
CodeBuild builds static assets (e.g., React, Angular)
Artifacts are uploaded to S3 for static website hosting or distribution

3.Deploy Dockerized Application to ECS (Fargate or EC2)
CodeCommit/CodeBuild for source and image build
Image pushed to ECR
CodePipeline updates ECS service with new image

4.Deploy Microservices to EKS (Kubernetes)
CodePipeline triggers on repo changes
CodeBuild builds and pushes Docker images to ECR
CodePipeline applies updated Kubernetes manifests to EKS

5.Deploy Serverless Application to Lambda
CodePipeline triggers on code changes
CodeBuild packages Lambda function
CodePipeline deploys new Lambda version (optionally with API Gateway)

