# Hello Flask App with CI/CD Pipeline

A simple Flask application that greets users with "hello my friends" and includes an automated CI/CD pipeline using GitHub Actions.

**Status Badge**


```markdown
![CI/CD Pipeline](https://github.com/AnisEmad/Flask_hello/actions/workflows/cicd.yml/badge.svg)
```

## Features

- Simple Flask web application
- Automated testing with pytest
- Continuous Integration and Continuous Deployment
- Docker containerization
- Automatic deployment to Docker Hub

## Project Structure

```
.
├── app.py                 # Main Flask application
├── test_app.py           # Pytest test suite
├── requirements.txt      # Python dependencies
├── Dockerfile           # Docker configuration
├── .github/
│   └── workflows/
│       └── ci-cd.yml    # GitHub Actions workflow
└── README.md            # This file
```

## Prerequisites

- Python 3.10+
- Docker (for containerization)
- GitHub account
- Docker Hub account

## Local Setup

1. **Clone the repository**
   ```bash
   git clone https://github.com/AnisEmad/Flask_hello.git
   cd Flask_hello
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the application**
   ```bash
   python app.py
   ```

4. **Run tests**
   ```bash
   pytest -v
   ```

## CI/CD Pipeline

The project uses GitHub Actions for automated testing and deployment. The pipeline is triggered on:
- Push to `main` branch
- Pull requests to `main` branch

### Pipeline Stages

#### 1. **Checkout Code**
- Retrieves the latest code from the repository

#### 2. **Set Up Python Environment**
- Installs Python 3.10
- Upgrades pip to the latest version

#### 3. **Install Dependencies**
- Installs all required packages from `requirements.txt`

#### 4. **Run Tests**
- Executes pytest with verbose output
- Validates that the app returns "hello my friends"

#### 5. **Docker Build and Push**
- Sets up Docker Buildx for multi-platform builds
- Authenticates with Docker Hub using secrets
- Builds Docker image
- Pushes image to Docker Hub as `yansoon10/hello-app:latest`
- Only executes if all previous steps succeed

## GitHub Secrets Configuration

To enable Docker Hub deployment, add the following secrets to your GitHub repository:

1. Go to your repository on GitHub
2. Navigate to **Settings** → **Secrets and variables** → **Actions**
3. Add the following secrets:
   - `DOCKERHUB_USERNAME`: Your Docker Hub username
   - `DOCKERHUB_TOKEN`: Your Docker Hub access token

### Creating a Docker Hub Access Token

1. Log in to [Docker Hub](https://hub.docker.com/)
2. Go to **Account Settings** → **Security**
3. Click **New Access Token**
4. Give it a description and create the token
5. Copy the token and add it to GitHub secrets

## Running the Docker Container

Once the image is pushed to Docker Hub, you can run it anywhere:

```bash
docker pull yansoon10/hello-app:latest
docker run -p 5000:5000 yansoon10/hello-app:latest
```

Access the application at `http://localhost:5000`

## Testing

The test suite validates that the Flask app returns the correct greeting message.

```bash
# Run all tests
pytest -v

# Run specific test file
pytest test_app.py -v
```

## Workflow File

The complete workflow configuration can be found in `.github/workflows/ci-cd.yml`

## Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

The CI/CD pipeline will automatically run tests on your PR!

## Troubleshooting

### Pipeline Fails at Docker Push
- Verify Docker Hub credentials in GitHub secrets
- Ensure Docker Hub token has write permissions
- Check if repository name `yansoon10/hello-app` exists and you have access

### Tests Fail
- Ensure the Flask app returns exactly "hello my friends"
- Check Python version compatibility
- Verify all dependencies are in `requirements.txt`


## Author

**AnisEmad**
- GitHub: [@AnisEmad](https://github.com/AnisEmad)



