# Secure GitOps Pipeline

    This project demonstrates a secure DevSecOps pipeline that builds, scans, and deploys a containerized application to Kubernetes using GitOps principles.
    ## Project Objectives

- Build a small containerized application.
- Run automated security checks before deployment.
- Deploy the application to a local Kubernetes cluster.
- Document the system like it would be handed to an operations team.    

---

## Current Progress

| Milestone | Status |
|-----------|--------|
| Git Repository | ✅ Complete |
| FastAPI Application | ✅ Complete |
| Docker Image | ✅ Complete |
| Run Container Locally | ⏳ In Progress |
| GitHub Actions CI | ⏳ Planned |
| Security Scanning | ⏳ Planned |
| Local Kubernetes (kind) | ⏳ Planned |
| GitOps (ArgoCD) | ⏳ Planned |

---

## Engineering Journal

### Milestone 1 – Building the Foundation

#### Objective

Establish a repeatable local development environment and package the application into a portable Docker image.

#### Completed

- Initialized a Git repository and connected it to GitHub.
- Built a FastAPI REST API.
- Added root (`/`) and health (`/health`) endpoints.
- Managed Python dependencies using `requirements.txt`.
- Added a `.gitignore` to exclude generated Python artifacts.
- Created a Dockerfile from scratch.
- Built the project's first Docker image.

#### Key Concepts Learned

- Git staging vs committing
- Small, focused commits
- Why `.gitignore` is important
- Difference between a Docker image and a Docker container
- Purpose of Dockerfile instructions:
  - `FROM`
  - `WORKDIR`
  - `COPY`
  - `RUN`
  - `CMD`

#### Validation

- API successfully ran locally with Uvicorn.
- `/health` endpoint returned a successful response.
- Docker image successfully built.

#### Lessons Learned

One of the biggest lessons from this milestone was that engineering discipline matters as much as learning new tools. Reading `git status`, staging only intentional changes, verifying each step before moving forward, and keeping the repository in a working state made debugging significantly easier.