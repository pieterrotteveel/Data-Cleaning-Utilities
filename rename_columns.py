def rename_columns(df: pd.DataFrame, mapping: Mapping[str, str]) -> pd.DataFrame:
    """
    Thin wrapper around DataFrame.rename with validation.
    Example:
        df = rename_columns(df, {"old": "new"})
    """
    unknown = set(mapping.keys()) - set(df.columns)
    if unknown:
        raise KeyError(f"Columns not found: {sorted(unknown)}")
    return df.rename(columns=mapping)
