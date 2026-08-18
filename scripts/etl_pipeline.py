"""
Bluestock Mutual Fund Capstone
ETL pipeline for cleaning raw CSV files and loading them into SQLite.
"""

from pathlib import Path
import sqlite3
import pandas as pd


PROJECT_ROOT = Path(__file__).resolve().parents[1]
DATA_RAW = PROJECT_ROOT / "data" / "raw"
DATA_PROCESSED = PROJECT_ROOT / "data" / "processed"
DATABASE_DIR = PROJECT_ROOT / "database"
DATABASE_FILE = DATABASE_DIR / "mutual_fund.db"


def log(message: str) -> None:
    """Print a standardized ETL status message."""
    print(f"[ETL] {message}")


def setup_directories() -> None:
    """Create required project directories if they do not exist."""
    DATA_RAW.mkdir(parents=True, exist_ok=True)
    DATA_PROCESSED.mkdir(parents=True, exist_ok=True)
    DATABASE_DIR.mkdir(parents=True, exist_ok=True)


def find_csv_files() -> list[Path]:
    """Return all CSV files available in the raw data directory."""
    files = list(DATA_RAW.glob("*.csv"))
    log(f"Found {len(files)} CSV files in raw folder.")
    return files


def clean_column_names(df: pd.DataFrame) -> pd.DataFrame:
    """Normalize column names by trimming and replacing spaces/hyphens."""
    df = df.copy()
    df.columns = (
        df.columns.astype(str)
        .str.strip()
        .str.lower()
        .str.replace(" ", "_", regex=False)
        .str.replace("-", "_", regex=False)
    )
    return df


def clean_dataframe(df: pd.DataFrame) -> pd.DataFrame:
    """Remove empty/duplicate rows and trim text fields."""
    df = clean_column_names(df)
    df = df.dropna(how="all")
    df = df.drop_duplicates()

    for column in df.select_dtypes(include=["object"]).columns:
        df[column] = df[column].astype(str).str.strip()

    return df


def process_csv(file: Path) -> pd.DataFrame | None:
    """Read, clean, and save one raw CSV file."""
    log(f"Processing: {file.name}")

    try:
        df = pd.read_csv(file)
        original_rows = len(df)

        df = clean_dataframe(df)
        cleaned_rows = len(df)

        output_file = DATA_PROCESSED / f"{file.stem}_clean.csv"
        df.to_csv(output_file, index=False)

        log(f"Saved: {output_file.name}")
        log(f"Rows: {original_rows} -> {cleaned_rows}")

        return df

    except Exception as error:
        log(f"ERROR processing {file.name}: {error}")
        return None


def load_to_database() -> None:
    """Load every processed CSV file into the SQLite database."""
    log("Loading processed CSV files into SQLite...")

    connection = sqlite3.connect(DATABASE_FILE)

    try:
        processed_files = list(DATA_PROCESSED.glob("*.csv"))

        for file in processed_files:
            try:
                df = pd.read_csv(file)

                table_name = (
                    file.stem
                    .replace("_clean", "")
                    .replace(" ", "_")
                )

                df.to_sql(
                    table_name,
                    connection,
                    if_exists="replace",
                    index=False,
                )

                log(f"Loaded table: {table_name}")

            except Exception as error:
                log(f"ERROR loading {file.name}: {error}")

        connection.commit()

    finally:
        connection.close()

    log("SQLite loading completed.")


def validate_database() -> None:
    """Display SQLite tables and their row counts for validation."""
    log("Validating SQLite database...")

    connection = sqlite3.connect(DATABASE_FILE)

    try:
        tables = pd.read_sql_query(
            """
            SELECT name
            FROM sqlite_master
            WHERE type = 'table'
            ORDER BY name
            """,
            connection,
        )

        print("Database tables:")

        for table in tables["name"]:
            count = pd.read_sql_query(
                f'SELECT COUNT(*) AS row_count FROM "{table}"',
                connection,
            )
            print(f"{table}: {count.iloc[0]['row_count']} rows")

    finally:
        connection.close()


def main() -> None:
    """Run the complete ETL process."""
    print("\n" + "=" * 65)
    print("BLUESTOCK MUTUAL FUND ETL PIPELINE")
    print("=" * 65)

    setup_directories()

    raw_files = find_csv_files()

    if not raw_files:
        raise FileNotFoundError("No CSV files found in data/raw.")

    successful = 0

    for file in raw_files:
        if process_csv(file) is not None:
            successful += 1

    print(
        f"\nSuccessfully processed "
        f"{successful}/{len(raw_files)} files."
    )

    load_to_database()
    validate_database()

    print("\n" + "=" * 65)
    print("ETL PIPELINE COMPLETED SUCCESSFULLY")
    print("=" * 65)


if __name__ == "__main__":
    main()