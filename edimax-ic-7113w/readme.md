# Use Temperature and Humidity from EDIMAX IC-7113W with Homeassistant

**Example Config in HA**

sensor:
   - platform: command_line
    name: Temperature
    command: "python3 /config/python_scripts/temperature.py"
    scan_interval: 360
    unit_of_measurement: "°C"
  - platform: command_line
    name: Humidity
    command: "python3 /config/python_scripts/humidity.py"
    scan_interval: 600
    unit_of_measurement: '%'
    
