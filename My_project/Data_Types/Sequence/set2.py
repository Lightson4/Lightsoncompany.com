FPO = {'dept of computer', 'dept of mathematic', 'dept of statistics', 'dept of econs', 'dept of acc', 'dept of business'}
faculty_of_science = {'dept of computer', 'dept of mathematic', 'dept of statistics'}
faculty_of_arts = {'dept of econs', 'dept of acc', 'dept of business'}
print(faculty_of_arts.issubset (FPO))
print(FPO.issuperset (faculty_of_science))
print(faculty_of_science.issubset(FPO))
print(FPO.issuperset(faculty_of_arts))