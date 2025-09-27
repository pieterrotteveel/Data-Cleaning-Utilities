def to_wide_utl(
    df: pd.DataFrame,
    index: Sequence[str],
    names_from: str,
    values_from: str,
    aggfunc: str | callable = "first",
    fill_value: Optional[Union[int, float, str]] = None,
) -> pd.DataFrame:
    wide = df.pivot_table(index=index, columns=names_from, values=values_from, aggfunc=aggfunc, fill_value=fill_value)
    if isinstance(wide.columns, pd.MultiIndex):
        wide.columns = ["_".join(map(str, tup)).strip("_") for tup in wide.columns.values]
    return wide.reset_index()
