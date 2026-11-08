# dump1090-fa-radar-visualizer

A Python script that creates a real-time polar radar visualization of nearby aircraft by parsing data from a local dump1090-fa server.

## Features
* Real-time live tracking using the dump1090-fa aircraft.json endpoint.
* Polar coordinate layout tracking true compass headings and distance relative to a home position.
* Haversine distance formulas to calculate live ground distance and true bearings.
* Dynamic labels that automatically alternate between showing flight Altitude (ft) and Ground Speed (kts).

## Prerequisites
Ensure you have Python 3 and matplotlib installed:

```bash
pip install matplotlib
```

## Configuration
Before running the script, update these variables in the code:
* **URL**: Change the IP address to match your dump1090 receiver.
* **HOME_LAT / HOME_LON**: Set your decimal latitude and longitude to center the radar over your location.

## Usage
Run the script using the following command:

```bash
python radar_visualizer.py
```
