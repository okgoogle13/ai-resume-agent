# AI Resume Agent Makefile

.PHONY: install test lint format clean run docker-build docker-run

# Install dependencies
install:
	pip install -r requirements.txt

# Run tests
test:
	pytest tests/ -v

# Run tests with coverage
test-coverage:
	pytest tests/ -v --cov=src --cov-report=html

# Lint code
lint:
	flake8 src/ tests/
	mypy src/

# Format code
format:
	black src/ tests/
	isort src/ tests/

# Clean up generated files
clean:
	find . -type f -name "*.pyc" -delete
	find . -type d -name "__pycache__" -delete
	find . -type d -name "*.egg-info" -exec rm -rf {} +
	rm -rf .pytest_cache/
	rm -rf .coverage
	rm -rf htmlcov/

# Run the application
run:
	streamlit run src/web/streamlit_app.py

# Build Docker image
docker-build:
	docker build -t ai-resume-agent .

# Run Docker container
docker-run:
	docker run -p 8501:8501 --env-file .env ai-resume-agent

# Development setup
dev-setup: install
	pre-commit install
	cp .env.example .env
	echo "Please edit .env file with your configuration"

# Deploy to Streamlit Cloud
deploy-streamlit:
	@echo "Push your code to GitHub and deploy via Streamlit Cloud dashboard"
	@echo "App entrypoint: src/web/streamlit_app.py"
