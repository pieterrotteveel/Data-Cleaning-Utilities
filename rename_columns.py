def rename_columns(df: pd.DataFrame, mapping: Mapping[str, str]) -> pd.DataFrame:
    unknown = set(mapping.keys()) - set(df.columns)
    if unknown:
        raise KeyError(f"Columns not found: {sorted(unknown)}")
    return df.rename(columns=mapping)
