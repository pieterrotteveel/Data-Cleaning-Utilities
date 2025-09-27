def to_bool_cols(
    df: pd.DataFrame,
    cols: Sequence[str],
    true_values: Optional[Iterable[str]] = None,
    false_values: Optional[Iterable[str]] = None,
) -> pd.DataFrame:
    tv = set(map(str.lower, true_values)) if true_values else _TRUE_VALUES
    fv = set(map(str.lower, false_values)) if false_values else _FALSE_VALUES

    def _to_bool(x):
        if pd.isna(x):
            return pd.NA
        s = str(x).strip().lower()
        if s in tv:
            return True
        if s in fv:
            return False
        return pd.NA

    for c in cols:
        df[c] = df[c].map(_to_bool).astype("boolean")
    return df
