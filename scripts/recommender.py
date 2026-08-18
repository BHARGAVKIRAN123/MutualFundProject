
import pandas as pd
from pathlib import Path


def recommend_funds(
    performance_file,
    risk_appetite,
    top_n=3
):
    """
    Recommend top funds by Sharpe ratio
    within the requested risk grade.

    Parameters
    ----------
    performance_file : str or Path
        Path to scheme performance CSV.

    risk_appetite : str
        Low / Moderate / High

    top_n : int
        Number of funds to return.

    Returns
    -------
    pandas.DataFrame
    """

    df = pd.read_csv(
        performance_file
    )

    df["risk_grade_clean"] = (
        df["risk_grade"]
        .astype(str)
        .str.strip()
        .str.lower()
    )

    df["sharpe_ratio"] = pd.to_numeric(
        df["sharpe_ratio"],
        errors="coerce"
    )

    risk = str(
        risk_appetite
    ).strip().lower()

    # Exact match first
    result = df[
        df["risk_grade_clean"] == risk
    ].copy()

    # Fallback matching
    if result.empty:

        if risk == "low":

            result = df[
                df["risk_grade_clean"]
                .str.contains(
                    "low",
                    na=False
                )
                &
                ~df[
                    "risk_grade_clean"
                ].str.contains(
                    "moderate",
                    na=False
                )
            ].copy()

        elif risk == "moderate":

            result = df[
                df["risk_grade_clean"]
                .str.contains(
                    "moderate",
                    na=False
                )
            ].copy()

        elif risk == "high":

            result = df[
                df["risk_grade_clean"]
                .str.contains(
                    "high",
                    na=False
                )
            ].copy()

    result = result.dropna(
        subset=["sharpe_ratio"]
    )

    result = (
        result
        .sort_values(
            "sharpe_ratio",
            ascending=False
        )
        .head(top_n)
    )

    return result[
        [
            "amfi_code",
            "scheme_name",
            "fund_house",
            "risk_grade",
            "sharpe_ratio"
        ]
    ]


if __name__ == "__main__":

    project_root = Path(__file__).resolve().parents[1]

    performance_file = (
        project_root
        / "data"
        / "processed"
        / "07_scheme_performance_clean.csv"
    )

    print("\nLow Risk:")
    print(
        recommend_funds(
            performance_file,
            "Low"
        ).to_string(index=False)
    )

    print("\nModerate Risk:")
    print(
        recommend_funds(
            performance_file,
            "Moderate"
        ).to_string(index=False)
    )

    print("\nHigh Risk:")
    print(
        recommend_funds(
            performance_file,
            "High"
        ).to_string(index=False)
    )
