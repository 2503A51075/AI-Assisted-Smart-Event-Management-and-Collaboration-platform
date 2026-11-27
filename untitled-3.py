def is_leap_year(year: int) -> bool:
    if isinstance(year, bool) or not isinstance(year, int):
        raise TypeError("year must be an integer")
    if year < 1:
        raise ValueError("year must be a positive integer")

    return year % 400 == 0 or (year % 4 == 0 and year % 100 != 0)


assert is_leap_year(2000) is True
assert is_leap_year(1900) is False
assert is_leap_year(2024) is True
assert is_leap_year(2023) is False

for year in (2000, 1900, 2024, 2023):
    status = "is a leap year" if is_leap_year(year) else "is not a leap year"
    print(f"{year} {status}")