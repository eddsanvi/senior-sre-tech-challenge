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
        +-----------+-----------+
        |                       |
        v                       v
       S3                  DynamoDB

Development:
Docker + LocalStack

Deployment:
Helm + Kubernetes

Infrastructure:
Terraform

CI/CD:
GitHub Actions
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
- IAM Policy
- IAM Role

Files:

```text
terraform/
├── main.tf
├── variables.tf
└── outputs.tf
```

---

## Local AWS Emulation

The project uses LocalStack Community Edition for local development.

Services emulated:

- S3
- DynamoDB

This allows validating AWS integrations without requiring an AWS account.

For production deployments, LocalStack endpoints would be replaced by native AWS endpoints.

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
- IRSA-ready ServiceAccount
- HorizontalPodAutoscaler
- PodDisruptionBudget

Install:

```bash
helm install user-api ./helm/user-api
```

---

## Reliability and Availability

The solution includes several reliability-focused features:

- Liveness probes
- Readiness probes
- Horizontal Pod Autoscaler (HPA)
- PodDisruptionBudget (PDB)
- ServiceAccount prepared for IRSA integration
- Infrastructure as Code with Terraform
- Automated CI validation
- Security scanning using Trivy

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
~72-75%
```
The test suite is automatically executed through GitHub Actions on every push and pull request.

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
