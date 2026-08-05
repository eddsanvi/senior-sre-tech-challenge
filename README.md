# Senior SRE Tech Challenge

## Overview

This project implements a Python-based REST API using FastAPI that allows:

- Creating users with avatar image uploads
- Storing avatars in S3
- Persisting user records in DynamoDB
- Running locally with Docker and LocalStack
- Deploying to Kubernetes using Helm
- Provisioning infrastructure with Terraform

## Architecture

```text
FastAPI
   |
   +--> S3 (Avatar Storage)
   |
   +--> DynamoDB (User Metadata)
```

## Features

### API Endpoints

#### GET /users

Returns all stored users.

Example response:

```json
[
  {
    "name": "Eduard",
    "email": "eduardsv81@gmail.com",
    "avatar_url": "http://localhost:4566/prima-tech-challenge/avatar.png"
  }
]
```

#### POST /user

Creates a new user and uploads an avatar image.

Accepted form parameters:

- name
- email
- avatar

---

## Local Development

### Prerequisites

- Docker Desktop
- WSL2
- Python 3
- Terraform
- AWS CLI

### Start LocalStack

```bash
docker compose up -d
```

### Provision Infrastructure

```bash
cd terraform

terraform init

terraform apply -auto-approve
```

### Run the API

```bash
source .venv/bin/activate

uvicorn app.main:app --reload
```

Swagger UI:

```text
http://localhost:8000/docs
```

---

## Infrastructure as Code

Terraform provisions:

- S3 Bucket
- DynamoDB Table

Files:

```text
terraform/
├── main.tf
├── variables.tf
└── outputs.tf
```

---

## Kubernetes

Helm chart location:

```text
helm/user-api
```

Components included:

- Deployment
- Service
- ServiceAccount
- HorizontalPodAutoscaler
- PodDisruptionBudget

Install:

```bash
helm install user-api ./helm/user-api
```

---

## Reliability Features

### Health Checks

Liveness probe:

```text
/health/live
```

Readiness probe:

```text
/health/ready
```

### Horizontal Pod Autoscaler

Automatically scales based on CPU usage.

### PodDisruptionBudget

Ensures service availability during node maintenance.

### ServiceAccount

Prepared for IAM Roles for Service Accounts (IRSA).

---

## Testing

Run tests:

```bash
pytest
```

Coverage:

```bash
pytest --cov=app
```

Current coverage:

```text
~75%
```

---

## CI/CD

GitHub Actions workflows included:

```text
.github/workflows/
├── ci.yml
└── security.yml
```

### CI Pipeline

- Install dependencies
- Run tests
- Build Docker image

### Security Pipeline

- Trivy filesystem scan

---

## Production Considerations

The following improvements would be implemented in a production environment:

- AWS Secrets Manager
- Externalized configuration
- Network Policies
- Ingress controller
- TLS certificates
- Integration tests
- Canary deployments
- Monitoring and alerting
- Structured logging
- Distributed tracing

---

## Repository Structure

```text
app/
├── api/
├── config/
├── models/
└── services/

terraform/

helm/

tests/

.github/workflows/
```
