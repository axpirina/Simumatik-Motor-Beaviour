if initialize:
    ang_speed = 0
    abiadura = 0
    j=10
    i=100
  
else:
    if x1_voltage[0]-x2_voltage[0] > 20 or x1_voltage[0]-x2_voltage[0] < -20:
        
        # Angular speed in rpm is proportional to the frequency and amplitud (Simplification)
        mod = 1 if x1_voltage[0]-x2_voltage[0] > 20 else -1
        
        ang_speed = i * mod
        abiadura = abs(ang_speed) / 100
        # Calculate current (Simplification)
        x1_current = [i*0.001, 0, 0]
        x2_current = [-i*0.001, 0, 0]
        hautazkoa = [j,0,0]
        speed = [abiadura,0,0]
        korrontea = x1_current
        i=i+j
    else:
        ang_speed = 0
        x1_current = [0, 0, 0]
        x2_current = [0, 0, 0]
        hautazkoa = [j,0,0]
        speed = [abiadura,0,0]
        korrontea = x1_current
