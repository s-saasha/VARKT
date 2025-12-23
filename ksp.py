import krpc
import time
import csv

def get_data():
    conn = krpc.connect(name='Getting data')

    vessel = conn.space_center.active_vessel
    ut = conn.add_stream(getattr, conn.space_center, 'ut')
    altitude = conn.add_stream(getattr, vessel.flight(), 'mean_altitude')
    speed = conn.add_stream(getattr, vessel.flight(vessel.orbit.body.reference_frame), 'speed')
    mass = conn.add_stream(getattr, vessel, 'mass')
    
    filename = 'data1.csv'
    start_time = ut()
    
    with open(filename, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow([
                "time",
                "altitude",
                "speed",
                "mass"
            ])

        while True:
            t = ut() - start_time
            alt = altitude()
            spd = speed()
            m = mass()
            writer.writerow([
                round(t, 2),
                round(alt, 2),
                round(spd, 2),
                round(m, 3) 
            ])
            
            time.sleep(0.1)


if __name__ == "__main__":
    get_data()