import sqlite3


def connect_to_db(db_file, db_type="sqlite"):
    """Connect to SQLite DB. Easily extendable to other DB types."""
    if db_type == "sqlite":
        return sqlite3.connect(db_file)
    else:
        raise ValueError(f"Unsupported database type: {db_type}")


def create_table_from_df(df, conn):
    """Create SQL table from pandas DataFrame."""
    df.to_sql("data_table", conn, if_exists="replace", index=False)
    conn.commit()
