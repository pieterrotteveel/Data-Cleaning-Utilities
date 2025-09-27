def decimal_to_bps(series: Union[pd.Series, Sequence[Union[str, float, int]]]) -> pd.Series:
    s = pd.to_numeric(pd.Series(series), errors="coerce")
    return s * 10000.0
