def split_column(
    df: pd.DataFrame,
    col: str,
    into: Sequence[str],
    sep: Optional[str] = None,
    regex: Optional[str] = None,
    n: int = -1,
    drop: bool = False,
    strip_parts: bool = True,
) -> pd.DataFrame:
    if col not in df.columns:
        raise KeyError(f"Column not found: {col}")
    s = df[col].astype("string")

    if regex:
        parts = s.str.extract(regex, expand=True)
    else:
        parts = s.str.split(sep=sep, n=n, expand=True)

    if parts.shape[1] != len(into):
        needed = len(into) - parts.shape[1]
        if needed > 0:
            for _ in range(needed):
                parts[parts.shape[1]] = pd.NA
        else:
            parts = parts.iloc[:, : len(into)]

    parts.columns = list(into)
    if strip_parts:
        for c in parts.columns:
            parts[c] = parts[c].str.strip()

    for c in parts.columns:
        df[c] = parts[c]

    if drop:
        df = df.drop(columns=[col])
    return df
