"""
Main entry point for the capital gains tax calculation application.
"""

from src.cli import CapitalGainsCLI


def main():
    """Main function that starts the application."""
    cli = CapitalGainsCLI()
    cli.run()


if __name__ == "__main__":
    main()