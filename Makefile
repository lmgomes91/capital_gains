# Makefile for Capital Gains Tax Calculator

# Variables
PYTHON = python3
MAIN = main.py

# Default target
.PHONY: all
all: clean test run clean

# Run the application
.PHONY: run
run: clean
	@echo "Running Capital Gains Tax Calculator..."
	@echo "Enter JSON operations, one line per simulation. Empty line to finish."
	@$(PYTHON) $(MAIN)
	@$(MAKE) clean

# Run tests
.PHONY: test
test: clean
	@echo "Running tests..."
	@$(PYTHON) -m unittest discover -v
	@$(MAKE) clean

# Run tests with coverage
.PHONY: coverage
coverage: clean
	@echo "Running tests with coverage..."
	@$(PYTHON) -m pip install coverage
	@$(PYTHON) -m coverage run -m unittest discover
	@$(PYTHON) -m coverage report -m
	@$(MAKE) clean

# Run tests with HTML coverage report
.PHONY: coverage-html
coverage-html: clean
	@echo "Running tests with HTML coverage report..."
	@$(PYTHON) -m pip install coverage
	@$(PYTHON) -m coverage run -m unittest discover
	@$(PYTHON) -m coverage html
	@echo "HTML coverage report generated in htmlcov/index.html"
	@$(MAKE) clean

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

# Help
.PHONY: help
help:
	@echo "Available targets:"
	@echo "  all         	- Run clean, tests, application, and clean again"
	@echo "  run         	- Clean, run the application, then clean again"
	@echo "  test        	- Clean, run all tests, then clean again"
	@echo "  coverage    	- Clean, run tests with coverage report, then clean again"
	@echo "  coverage-html  - Clean, run tests with coverage report, generate html report, then clean again"
	@echo "  clean       	- Remove Python cache files"
	@echo "  help        	- Show this help message"
