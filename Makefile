# Variables
PYTHON = python3
SRC_DIR = src
TEST_DIR = tests
MAIN = main.py

# Default target
.PHONY: all
all: test run

# Run the application
.PHONY: run
run:
	@echo "Running Capital Gains Tax Calculator..."
	@echo "Enter JSON operations, one line per simulation. Empty line to finish."
	@$(PYTHON) $(MAIN)

# Run tests
.PHONY: test
test:
	@echo "Running tests..."
	@$(PYTHON) -m unittest discover -v

# Run tests with coverage
.PHONY: coverage
coverage:
	@echo "Running tests with coverage..."
	@$(PYTHON) -m coverage run -m unittest discover
	@$(PYTHON) -m coverage report -m

# Clean up Python cache files
.PHONY: clean
clean:
	@echo "Cleaning Python cache files..."
	@find . -type d -name "__pycache__" -exec rm -rf {} +
	@find . -type f -name "*.pyc" -delete
	@find . -type f -name "*.pyo" -delete
	@find . -type f -name "*.pyd" -delete
	@find . -type f -name ".coverage" -delete
	@find . -type d -name "*.egg-info" -exec rm -rf {} +
	@find . -type d -name "*.egg" -exec rm -rf {} +
	@find . -type d -name ".pytest_cache" -exec rm -rf {} +
	@echo "Clean complete!"

# Install dependencies
.PHONY: install
install:
	@echo "Installing dependencies..."
	@$(PYTHON) -m pip install -r requirements.txt

# Create requirements.txt
.PHONY: requirements
requirements:
	@echo "Creating requirements.txt..."
	@$(PYTHON) -m pip freeze > requirements.txt

# Help
.PHONY: help
help:
	@echo "Available targets:"
	@echo "  all         - Run tests and then the application"
	@echo "  run         - Run the application"
	@echo "  test        - Run all tests"
	@echo "  coverage    - Run tests with coverage report"
	@echo "  clean       - Remove Python cache files"
	@echo "  install     - Install dependencies"
	@echo "  requirements - Create requirements.txt file"
	@echo "  help        - Show this help message"
