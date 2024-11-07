# QuerySave

QuerySave is a backend solution for caching and similarity detection of prompts to optimize usage and reduce costs associated with large language model (LLM) API calls.

## Project Structure

- **app/**: Main application code.
- **automation/**: Automation scripts for setup, deployment, and testing.
- **tests/**: Unit and integration tests.
- **Dockerfile**: Docker configuration.
- **docker-compose.yml**: Docker Compose for managing services.

## Setup

1. Install dependencies:
    ```
    bash automation/install.sh
    ```

2. Start the FastAPI server:
    ```
    bash automation/start_server.sh
    ```

## Running Tests
```
bash automation/test.sh
```
