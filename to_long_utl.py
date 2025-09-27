def to_long_utl(
    df: pd.DataFrame,
    id_vars: Optional[Sequence[str]] = None,
    value_vars: Optional[Sequence[str]] = None,
    var_name: str = "variable",
    value_name: str = "value",
) -> pd.DataFrame:
    return pd.melt(df, id_vars=id_vars, value_vars=value_vars, var_name=var_name, value_name=value_name)
