"""
Bluestock Mutual Fund Capstone
Master execution script.

Run this file from the project root:
    python scripts/run_pipeline.py
"""

from etl_pipeline import main


def run() -> None:
    """Execute the complete ETL pipeline."""
    main()


if __name__ == "__main__":
    run()
