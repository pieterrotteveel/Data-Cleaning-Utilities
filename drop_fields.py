def drop_fields(df: pd.DataFrame, cols: Sequence[str], errors: str = "ignore") -> pd.DataFrame:
    return df.drop(columns=list(cols), errors=errors)
