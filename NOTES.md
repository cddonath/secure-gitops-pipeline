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


## Questions to Research