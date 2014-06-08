#Zeller Method project
# We'll be using Zeller's congruence, which is an algorithm devised by Christian Zeller to 
# calculate the day of the week for any Julian or Gregorian calendar date:
#h = ( ( q +( (m+1) * 26 // 10)+ Y +( Y // 4)+ 6 * (Y // 100)+ (Y // 400)) % 7 )
#... all of which translates to this:
#dayOfWeek = (dayOfMonth + ((month + 1) * 26 // 10) + year + (year // 4) +
#   6 * (year/ / 100) + (year // 400)) % 7)
# Note that in this algorithm h is the day of the week starts from Saturday
# (0 = Saturday, 1 = Sunday, 2 = Monday,..., 6 = Friday)
# Note that in this algorithm, January and February are counted as
# months #13 & #14 of the previous year, which will need to factor into your method.

def zeller(q, m, Y):
    # Where: q = day of month; m = month of the year (string); Y = year
    # This method should return the day of the week as a string
    months = ['January','February','March','April','May','June','July','August','September','October','November','December']
    for i in range(0,12):
        if(m==months[i]):
            m2=i+1
    if (m2<3):
        m2 = m2+12
        Y -= 1
    days=['Saturday','Sunday','Monday','Tuesday','Wednesday','Thursday','Friday']
    h = ( ( q +( (m2+1) * 26 // 10)+ Y +( Y // 4)+ 6 * (Y // 100)+ (Y // 400)) % 7 )
    return days[h]