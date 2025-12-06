def validate_data(df):
    """
    Validate incoming DataFrame before DB insertion.

    Rules:
    - No missing values
    - Additional rules can be added
    """

    if df.isnull().sum().any():
        print("[WARNING] Missing values detected.")
        return False

    return True
