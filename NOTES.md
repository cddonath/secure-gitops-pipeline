# Secure GitOps Pipeline Notes

## Git

### git status

Purpose:
- Shows the state of the working directory and staging area.

Key Lesson:
- Run before staging.
- Run after staging.
- Run after committing.

---

### git add

Purpose:
- Moves changes into the staging area.

Key Lesson:
- Stage intentionally.
- `git add .` is fine after verifying changes with `git status`.

---

### git commit

Purpose:
- Creates a snapshot of the staged changes.

Key Lesson:
- `git commit -m` creates a one-line commit.
- `git commit` opens the configured text editor (Vim on my machine).

---

## Docker

### Image vs Container

Image
- Blueprint.
- Immutable.
- Contains application, runtime, dependencies, configuration.

Container
- Running instance of an image.
- Has processes, memory, networking, and logs.

### docker ps

Shows currently running containers.

### docker ps -a

Shows all containers, including stopped ones.

Exit code 0 = application exited successfully.

---

### Dockerfile Instructions

FROM
- Selects the base image.

WORKDIR
- Sets the default working directory.

COPY
- Copies files into the image.

RUN
- Executes commands during image build.

CMD
- Specifies the default command when the container starts.

### Container Hardening

#### Run as non-root user

Practice:
- Create a dedicated application user inside the image.
- Run the application as that user instead of root.

Why:
- Applies the Principle of Least Privilege.
- Reduces impact if the application is compromised.
- Helps satisfy common container security scanner checks.

Dockerfile instruction used:

```dockerfile
RUN useradd -m appuser

## Container Hardening Checklist

- [x] Run as non-root user (`USER`)
- [x] Use least privilege for file ownership (`chown`)
- [ ] Minimize image size
- [ ] Pin base image versions
- [ ] Scan image for vulnerabilities
- [ ] Use a minimal base image
- [ ] Avoid embedding secrets


## Troubleshooting Log

### GitHub Actions workflow failed before creating a job

Problem:
- A GitHub Actions workflow failed, but no `build` job appeared in the Actions UI.
- The workflow graph could not be shown.

Cause:
- The workflow YAML had an indentation error.
- The `Set up Python` step was accidentally nested under the previous `run: ls -R` command instead of being aligned as its own step.

Fix:
- Reviewed the full `.github/workflows/ci.yml` file.
- Corrected the indentation so each workflow step was aligned under `steps:`.
- Committed and pushed the fix.

Validation:
- GitHub Actions reran successfully.
- The workflow completed all steps:
  - checkout repository
  - show repository contents
  - set up Python
  - install dependencies
  - run API smoke test

Interview talking point:
- I debugged a CI failure by first identifying that no job had been created, which suggested the issue was with workflow parsing rather than application code. I inspected the YAML, found an indentation error, corrected it, and verified the fix by rerunning the GitHub Actions workflow successfully.
## Questions to Research