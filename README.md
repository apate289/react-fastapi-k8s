# React + FastAPI + Kubernetes Starter

This scaffold contains a minimal **React frontend** and **FastAPI backend**, with Dockerfiles, docker-compose for local development, Kubernetes manifests (Deployments, Services, Ingress), a Helm chart, and a GitHub Actions CI/CD workflow that builds images and (optionally) deploys to Kubernetes.

Backend: FastAPI app (backend/app/main.py), requirements.txt, Dockerfile
Frontend: Minimal React app (frontend/src/*), package.json, Dockerfile, webpack dev config
docker-compose.yml for local development (backend on :8000, frontend on :3000)
Kubernetes manifests in k8s/ (Deployments, Services, Ingress)
Helm chart in helm-chart/ with templates and values.yaml
GitHub Actions workflow .github/workflows/ci-cd.yml (builds and pushes images, deploys manifests)
Makefile, .gitignore, and README with usage notes

> **Notes before running:** 
> - You need Docker, docker-compose, and kubectl installed locally.
> - For pushing images to Docker Hub, update the Docker Hub repo names in the GitHub Actions workflow (`DOCKERHUB_USERNAME` and `DOCKERHUB_REPO`).
> - The GitHub Actions workflow assumes you store `DOCKERHUB_USERNAME`, `DOCKERHUB_TOKEN`, and `KUBE_CONFIG_DATA` (base64-encoded kubeconfig) as secrets.
> - The Helm chart is parameterized; adjust values in `helm-chart/values.yaml`.

Structure:
```
/backend        - FastAPI app, Dockerfile
/frontend       - React app, Dockerfile
/docker-compose.yml
/k8s            - Kubernetes manifests (Deployment/Service/Ingress)
/helm-chart     - Helm chart templates + values
/.github/workflows/ci-cd.yml - GitHub Actions workflow
```

