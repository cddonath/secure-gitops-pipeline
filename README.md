# Secure GitOps Pipeline

A hands-on DevSecOps project that demonstrates how modern software is built, tested, secured, and prepared for deployment using GitHub Actions, Docker, and GitOps principles.

The goal of this project is not simply to learn individual tools, but to understand how they integrate into a secure software delivery pipeline that mirrors real-world engineering practices.

---

# Project Goals

- Build a containerized FastAPI application.
- Implement a Continuous Integration (CI) pipeline with GitHub Actions.
- Automatically execute unit tests on every push.
- Perform Static Application Security Testing (SAST) with Semgrep.
- Detect committed secrets using Gitleaks.
- Scan container images and application dependencies using Trivy.
- Fail the pipeline on High and Critical vulnerabilities.
- Deploy the application to Kubernetes using GitOps principles (Tier 2).

---

# Current Project Status

| Feature | Status |
|----------|:------:|
| Git Repository | ✅ |
| FastAPI Application | ✅ |
| Docker Containerization | ✅ |
| Container Hardening | ✅ |
| GitHub Actions CI | ✅ |
| Unit Testing (Pytest) | ✅ |
| Semgrep SAST | ✅ |
| Gitleaks Secrets Scan | ✅ |
| Trivy Container Scan | ✅ |
| Kubernetes Deployment | ⏳ Tier 2 |
| GitOps (ArgoCD) | ⏳ Tier 2 |

---

# Technology Stack

## Languages

- Python 3.11

## Frameworks

- FastAPI

## Containers

- Docker

## CI/CD

- GitHub Actions

## Testing

- Pytest

## Security

- Semgrep
- Gitleaks
- Trivy

---

# CI Pipeline

Every push to the `main` branch automatically performs the following checks:

1. Checkout repository
2. Install Python
3. Install project dependencies
4. Execute unit tests
5. Run Semgrep SAST scan
6. Run Gitleaks secrets scan
7. Build Docker image
8. Scan Docker image using Trivy

The pipeline intentionally fails whenever High or Critical vulnerabilities are detected.

---

# Pipeline Architecture

```text
                 Developer
                     │
                 git push
                     │
                     ▼
            GitHub Repository
                     │
                     ▼
          GitHub Actions Workflow
                     │
 ┌─────────────────────────────────────────────┐
 │ Checkout Repository                         │
 │ Install Python                              │
 │ Install Dependencies                        │
 │ Run Unit Tests (pytest)                     │
 │ Run Semgrep SAST                            │
 │ Run Gitleaks Secrets Scan                   │
 │ Build Docker Image                          │
 │ Scan Docker Image (Trivy)                   │
 └─────────────────────────────────────────────┘
                     │
            Pass / Fail Security Gate
                     │
                     ▼
        (Tier 2: Kubernetes + GitOps)
```

---

# Container Security

Current hardening practices include:

- Running the application as a non-root user
- Applying the Principle of Least Privilege
- Using `.dockerignore`
- Container vulnerability scanning with Trivy
- Automated security validation within CI

Future hardening goals:

- Multi-stage Docker builds
- Pinned image digests
- Read-only container filesystem
- Image signing with Cosign
- Software Bill of Materials (SBOM)

---

# Engineering Highlights

Throughout development, several real-world engineering issues were encountered and documented.

Examples include:

- Debugging GitHub Actions YAML syntax errors
- Resolving Python package import issues in CI
- Understanding differences between local development and clean CI environments
- Integrating multiple security tools into a single automated pipeline
- Learning why a failing security gate can represent a successful security control

A detailed engineering journal is maintained in **NOTES.md**.

---

# Lessons Learned

Some of the biggest takeaways from Tier 1 include:

- Small, focused Git commits simplify debugging.
- Validate changes locally before automating them.
- Clean CI environments expose assumptions hidden during local development.
- Security should be integrated into the development lifecycle rather than added later.
- A failing security pipeline can indicate that security controls are functioning correctly.

---

# Roadmap

## Tier 1 – Secure CI Pipeline ✅

- Git
- FastAPI
- Docker
- GitHub Actions
- Pytest
- Semgrep
- Gitleaks
- Trivy

---

## Tier 2 – GitOps

- Kubernetes
- kind
- Container Registry
- Kubernetes Manifests
- ArgoCD
- Automated GitOps Deployments

---

## Tier 3 – Enterprise DevSecOps

- Cosign Image Signing
- SBOM Generation
- Admission Controllers
- Policy as Code
- Supply Chain Security
- Monitoring & Observability

---

# Running the Project

Clone the repository:

```bash
git clone <repository-url>
cd secure-gitops-pipeline
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run locally:

```bash
uvicorn app.main:app --reload
```

Or run using Docker:

```bash
docker build -t secure-gitops-pipeline .

docker run -p 8000:8000 secure-gitops-pipeline
```

Application endpoints:

```
GET /
GET /health
```

---

# Why I Built This

This project was created to gain practical experience designing and implementing a modern DevSecOps pipeline rather than simply learning individual tools in isolation.

Each capability was implemented incrementally, tested, documented, and integrated into a Continuous Integration workflow to better understand how secure software delivery is performed in professional engineering environments.