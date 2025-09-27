def infer_decimal_thousands(sample: Sequence[str]) -> Tuple[str, Optional[str]]:
    dot_decimal = sum(bool(re.search(r"\d+\.\d{1,}", s)) for s in sample)
    comma_decimal = sum(bool(re.search(r"\d+,\d{1,}", s)) for s in sample)
    dot_thou = sum(bool(re.search(r"\d{1,3}(?:\.\d{3})+(?:\D|$)", s)) for s in sample)
    comma_thou = sum(bool(re.search(r"\d{1,3}(?:,\d{3})+(?:\D|$)", s)) for s in sample)

    if comma_decimal > dot_decimal:
        decimal = ","
    elif dot_decimal > comma_decimal:
        decimal = "."
    else:
        if dot_thou > comma_thou:
            decimal = ","
        elif comma_thou > dot_thou:
            decimal = "."
        else:
            decimal = "." 

    thousands = "," if decimal == "." else "."
    return decimal, thousands

