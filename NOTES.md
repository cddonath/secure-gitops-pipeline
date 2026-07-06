# Secure GitOps Pipeline Notes

---

# Table of Contents

- Git
- Docker
- GitHub Actions
- DevSecOps Tools
- Container Hardening
- Troubleshooting Log
- CI/CD Pipeline Evolution
- Engineering Principles
- Lessons Learned
- Interview Talking Points
- Questions to Research

---

# Git

## git status

Purpose

- Shows the current state of the working directory and staging area.

Key Lessons

- Run before staging.
- Run after staging.
- Run after committing.
- Verify changes before making a commit.

---

## git add

Purpose

Moves files into the staging area.

Key Lessons

- Stage intentionally.
- `git add .` is acceptable after verifying the working tree with `git status`.
- Always verify the staging area before committing.

---

## git commit

Purpose

Creates a snapshot of the staged changes.

Key Lessons

- `git commit -m` creates a one-line commit.
- `git commit` opens the configured editor (Vim on my machine).
- Keep commits small and focused around one logical change.

---

## Git Workflow

Typical workflow

1. Save files.
2. Run `git status`.
3. Stage changes.
4. Verify staging with `git status`.
5. Commit.
6. Verify clean working tree.
7. Push.

---

# Docker

## Image vs Container

### Image

- Blueprint
- Immutable
- Contains:
  - Application
  - Runtime
  - Dependencies
  - Configuration

### Container

- Running instance of an image
- Contains:
  - Running processes
  - Memory
  - Networking
  - Logs

Containers are ephemeral.

---

## Docker Commands

### docker ps

Shows running containers.

### docker ps -a

Shows all containers including stopped containers.

Exit Code 0

Application exited successfully.

---

## Dockerfile Instructions

### FROM

Selects the base image.

### WORKDIR

Sets the default working directory.

### COPY

Copies files into the image.

### RUN

Executes commands during image creation.

### CMD

Specifies the default command when the container starts.

---

## Docker Layer Caching

Purpose

Reduce image build time.

Key Lessons

Docker builds from the top of the Dockerfile downward.

If one layer changes, every layer below it must be rebuilt.

Best Practice

Keep frequently changing files near the bottom of the Dockerfile.

---

# GitHub Actions

## Purpose

Automatically validate code on every push.

Current Pipeline

- Checkout Repository
- Install Python
- Install Dependencies
- Run Unit Tests
- Run Semgrep SAST Scan
- Run Gitleaks Secrets Scan
- Build Docker Image
- Scan Docker Image with Trivy

Key Lesson

CI should answer:

- Does the application work?
- Does it build?
- Is the code secure?
- Were secrets committed?
- Is the deployment artifact vulnerable?

---

# DevSecOps Tools

## Pytest

Purpose

Automated unit testing.

Current Test

- Verify `/health`
- Expect HTTP 200
- Expect JSON:

```json
{
    "status": "ok"
}
```

Key Lesson

Always validate locally before adding tests to CI.

---

## Semgrep

Purpose

Static Application Security Testing (SAST)

Scans source code without executing it.

Implementation

- GitHub Action
- Python ruleset (`p/python`)

Result

- 151 Python security rules
- 0 blocking findings

Key Lesson

Semgrep analyzes application source code for insecure coding patterns.

---

## Gitleaks

Purpose

Detect secrets committed to Git.

Examples

- API Keys
- GitHub Tokens
- AWS Credentials
- Passwords

Key Lesson

Secrets should never enter source control.

---

## Trivy

Purpose

Scans

- Container Images
- Operating System Packages
- Application Dependencies

Pipeline Behavior

Fail workflow on

- HIGH
- CRITICAL

Key Lesson

A failed Trivy scan does not necessarily indicate a broken pipeline.

It may indicate the security gate correctly detected vulnerabilities.

---

# Container Hardening

## Run as non-root user

Practice

Create a dedicated application user.

Run the application as that user.

Dockerfile

```dockerfile
RUN useradd -m appuser
RUN chown -R appuser:appuser /app
USER appuser
```

Why

- Principle of Least Privilege
- Reduce impact of compromise
- Meet container security best practices

---

## Hardening Checklist

- [x] Run as non-root user
- [x] Use least privilege for ownership (`chown`)
- [x] Scan image for vulnerabilities
- [ ] Pin base image digest
- [ ] Minimize image size
- [ ] Multi-stage build
- [ ] Read-only filesystem
- [ ] Avoid embedding secrets

---

# Troubleshooting Log

## GitHub Actions workflow failed before creating a job

Problem

Workflow graph would not generate.

No build job appeared.

Cause

YAML indentation error.

Fix

Corrected workflow indentation.

Validation

Workflow executed successfully.

Interview Talking Point

Identified that the failure occurred before any jobs were created, indicating a workflow parsing issue rather than an application issue.

---

## Unit tests failed in GitHub Actions

Problem

```
ModuleNotFoundError: No module named 'app'
```

Cause

Python package resolution differed between local development and the GitHub Actions runner.

Fix

Added

```
app/__init__.py
```

Follow-up

Still failed.

Verified tracked files using

```bash
git ls-files app
```

Updated CI command

```bash
PYTHONPATH=. pytest
```

Validation

Unit tests passed.

Pipeline advanced to Trivy.

Interview Talking Point

The issue demonstrated differences between local development and clean CI environments.

---

## Trivy Failure

Problem

Pipeline failed during Trivy scan.

Cause

Expected.

HIGH and CRITICAL vulnerabilities were detected.

Validation

Security gate correctly prevented pipeline progression.

Biggest Lesson

A failing security pipeline can indicate success.

The security controls worked exactly as designed.

---

# CI/CD Pipeline Evolution

## Stage 1

Repository Checkout

---

## Stage 2

Python Installation

Dependency Installation

---

## Stage 3

FastAPI Smoke Test

---

## Stage 4

Docker Image Build

---

## Stage 5

Pytest Unit Tests

---

## Stage 6

Semgrep SAST

Gitleaks Secrets Scan

---

## Stage 7

Trivy Container Scan

Fail on HIGH / CRITICAL findings

---

## Tier 2

- Kubernetes
- GitOps
- ArgoCD
- Automated Deployments

---

# Engineering Principles

- Automate repetitive work.
- Verify before committing.
- Keep commits focused.
- Read logs before changing code.
- Prefer reproducible environments.
- Fail early.
- Security should be integrated into the development lifecycle.

---

# Lessons Learned

- Save files before staging.
- Validate locally before automating.
- Small commits simplify debugging.
- CI environments expose assumptions hidden by local development.
- Security gates should fail for meaningful reasons.
- Documentation is part of engineering.

---

# Interview Talking Points

I can confidently explain:

- Git workflow
- Commit discipline
- Docker Images vs Containers
- Docker layer caching
- Container hardening
- Principle of Least Privilege
- GitHub Actions
- Unit testing
- Static Application Security Testing (Semgrep)
- Secrets scanning (Gitleaks)
- Container vulnerability scanning (Trivy)
- CI troubleshooting
- "Works on my machine" vs CI
- Security gates
- Reading CI logs
- YAML debugging

---

# Biggest Takeaway from Tier 1

A successful DevSecOps pipeline is not always green.

Sometimes a failing pipeline demonstrates that automated security controls are functioning correctly.

The objective is not to force every build to pass.

The objective is to ensure failures occur for the correct reasons and provide actionable feedback.

---

# Questions to Research

- Multi-stage Docker builds
- Docker image signing (Cosign)
- Software Bill of Materials (SBOM)
- Kubernetes Deployments
- Kubernetes Services
- GitOps fundamentals
- ArgoCD
- Admission Controllers
- Policy as Code
- Supply Chain Security

