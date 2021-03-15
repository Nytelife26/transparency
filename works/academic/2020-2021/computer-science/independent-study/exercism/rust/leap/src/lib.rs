pub fn is_leap_year(year: u64) -> bool {
    let four = year % 4 == 0;
    let hund = year % 100 == 0;
    four && (!hund || year % 400 == 0)
}
