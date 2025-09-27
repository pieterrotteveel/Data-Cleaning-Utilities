def bps_to_decimal(series: Union[pd.Series, Sequence[Union[str, float, int]]]) -> pd.Series:
    s = pd.Series(series).astype("string").str.replace(r"(?i)\s*bps?\s*$", "", regex=True)
    s = s.str.replace("\u00A0", "", regex=False).str.replace(" ", "", regex=False)
    s = s.str.replace(",", ".", regex=False)
    return pd.to_numeric(s, errors="coerce") / 10000.0
