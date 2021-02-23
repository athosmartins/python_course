text = open('json_test.txt','r')
t = ''.join(text)

pos1 = t.find("SALARY.MONTH_1.V4")
pos2 = t.find(",",pos1)
s1 = float(t[pos1+21:pos2-1])
print('Salary Month 1 = ',s1)

pos3 = t.find("SALARY.MONTH_2.V4")
pos4 = t.find(",",pos3)
s2 = float(t[pos3+21:pos4-1])
print('Salary Month 2 = ',s2)

pos5 = t.find("SALARY.MONTH_3.V4")
pos6 = t.find(",",pos5)
s3 = float(t[pos5+21:pos6-1])
print('Salary Month 3 = ',s3)

pos7 = t.find("SALARY.MONTH_4.V4")
pos8 = t.find(",",pos7)
s4 = float(t[pos7+21:pos8-1])
print('Salary Month 4 = ',s4)

salaries = [s1,s2,s3,s4]
min_s = min(salaries)
print("Lowest Salary = ",min_s)

avg_s = (s1+s2+s3+s4)/4
print("Average Salary =",avg_s)
