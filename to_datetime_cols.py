def to_datetime_cols(
    df: pd.DataFrame,
    cols: Sequence[str],
    dayfirst: bool = True,
    yearfirst: bool = False,
    utc: Optional[bool] = None,
    fmt: Optional[str] = None,
    errors: str = "coerce",
) -> pd.DataFrame:
    for c in cols:
        df[c] = pd.to_datetime(df[c], format=fmt, dayfirst=dayfirst, yearfirst=yearfirst, errors=errors, utc=utc)
    return df
