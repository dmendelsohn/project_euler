# How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)?
def compute(verbose=False): #note jan 1 1901 was a Tuesday, so date%7==5 is required
    four_years = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]*4
    four_years[37] = 29  # Leap day
    sundays, date = 0, 2 # First of Jan 1 1901 is Tuesday, which is date #2 (Sunday is 0)
    for i in range(1, 12*100):
        date = (date + four_years[(i-1)%48]) % 7  # Compute start date of month i
        if date == 0:
        	sundays += 1
    return sundays, "Number of months starting on Sunday in 20th century"
