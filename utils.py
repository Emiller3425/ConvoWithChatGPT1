def is_float(string):
    try:
        float(string)
        return True
    except ValueError:
        return False

def format_result(result):
    # Format the result for display (e.g., remove trailing zeros)
    if isinstance(result, int):
        return str(result)
    elif isinstance(result, float):
        formatted_result = format(result, ".6f")  # Display up to 6 decimal places
        formatted_result = formatted_result.rstrip("0").rstrip(".")  # Remove trailing zeros and decimal point
        return formatted_result
    else:
        return str(result)