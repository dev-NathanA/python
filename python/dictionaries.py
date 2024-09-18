monthConversions = {
    1: "January",
    2: "February",
    "Mar": "March",
    "Apr": "April",
    "May": "May",
    "Jun": "June",
    "Jul": "July",
    "Aug": "August",
    "Sep": "September",
    "Oct": "October",
    "Nov": "November",
    "Dec": "December"
}

print(monthConversions[1])
print(monthConversions.get("Dec"))
print(monthConversions.get("Mon", "Not a valid key"))
