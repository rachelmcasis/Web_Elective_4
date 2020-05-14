d = 10
g_min = 43
g_sec = 30

time= g_min / 60
time_2 =g_sec / 3600

f_time = time + time_2
f_dist = d / 1.61

ave_final_speed = f_dist / f_time
ave_final_time = f_dist / ave_final_speed

print()
print("The average Speed is:", ave_final_speed)
print()
print("While the ave Time is:", ave_final_time)


