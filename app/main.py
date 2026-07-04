from fastapi import FastAPI

app = FastAPI(
    title="Secure GitOps Pipeline",
    version="1.0.0",
    description="A secure DevSecOps demonstration project."
)


@app.get("/")
def root():
    return {
        "project": "Secure GitOps Pipeline",
        "version": "1.0.0"
    }


@app.get("/health")
def health():
    return {
        "status": "ok"
    }