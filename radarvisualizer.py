import time
import urllib.request
import json
import matplotlib.pyplot as plt
import math
URL = "XXXXXXXXX" 
history = []
flight_data = []

HOME_LAT = 35.034
HOME_LON = -80.8442

phiHome = HOME_LAT * (math.pi/180)
lmdHome = HOME_LON * (math.pi/180)

show_alt = True
plt.ion()
fig, ax = plt.subplots(subplot_kw={'projection' : 'polar'}, figsize = (6,6))
ax.set_theta_zero_location('N')
ax.set_theta_direction(-1)
ax.set_rmax(180)
ax.set_rmin(0)

loop_counter = 0
    
while True:

    try:
        with urllib.request.urlopen(URL) as r:
            snapshot = json.loads(r.read().decode())["aircraft"]
            history.append(snapshot)
            
            for p in snapshot:
                if "lat" in p and "lon" in p:
                   lats = p["lat"]
                   lons = p["lon"]
                   flight = p.get("flight", "UNK").strip()
                   alt = p.get("alt_baro")
                   spd = p.get("gs")
                   flight_data.append((lats,lons,flight,alt,spd))
            
            for i, j, flight_name, alt, spd in flight_data:
                # calculating radius
                phiPlane = i * (math.pi/180)
                lmdPlane = j * (math.pi/180)
                
                dphi = phiPlane - phiHome
                dlmd = lmdPlane - lmdHome
                
                alpha = (math.sin(dphi/2)**2)+math.cos(phiHome)*math.cos(phiPlane)*(math.sin(dlmd/2)**2)
                r = 2 * 3959 * math.atan2(math.sqrt(alpha), math.sqrt(1-alpha))
                
                # calculating angle bearing
                y = math.sin(dlmd) * math.cos(phiPlane)
                x = math.cos(phiHome)*math.sin(phiPlane)-math.sin(phiHome)*math.cos(phiPlane)*math.cos(dlmd)
                
                theta_rad = math.atan2(y,x)
                theta_deg = theta_rad * (180/math.pi)
                
                ax.scatter(theta_rad, r, color = 'red', s=30)
                
                ax.text(theta_rad, r, f"  {flight_name}", fontsize = 8, va = "bottom")
                if show_alt:
                    ax.text(theta_rad, r, f"   ALT: {alt} ft", fontsize = 5, va = "top")
                else:
                    ax.text(theta_rad, r, f"   SPD: {spd} kts", fontsize = 5, va = "top")
                
                
            plt.pause(0.01)
            time.sleep(1)
            ax.clear()
            ax.set_theta_zero_location('N')
            ax.set_theta_direction(-1)
            ax.set_rmax(180)
            ax.set_rmin(180)
            
            flight_data.clear()
            loop_counter += 1
            if loop_counter >= 3:
                show_alt = not show_alt
                loop_counter = 0
                
    except Exception as e:
        print(f"Connection error: {e}", flush=True)  

