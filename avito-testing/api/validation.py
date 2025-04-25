def validate_fixed_length(fixed_length: int) -> bool:
    return lambda lst: len(lst) == fixed_length
