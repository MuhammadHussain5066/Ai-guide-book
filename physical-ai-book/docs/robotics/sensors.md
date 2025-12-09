---
sidebar_position: 2
---

# Sensors in Robotics

Sensors are the "eyes and ears" of robots, allowing them to perceive and understand their environment.

## What are Sensors?

Sensors convert physical phenomena (light, sound, pressure, distance) into electrical signals that robots can process and respond to.

## Types of Sensors

### 1. Vision Sensors

#### Cameras
- **RGB Cameras**: Standard color vision
- **Depth Cameras**: 3D perception (Intel RealSense, Kinect)
- **Stereo Cameras**: Calculate depth from two images
- **Thermal Cameras**: Heat detection

**Applications**:
- Object detection and recognition
- Navigation and obstacle avoidance
- Facial recognition
- Quality inspection

#### LIDAR (Light Detection and Ranging)
- Laser-based distance measurement
- Creates 3D point cloud maps
- Highly accurate distance sensing
- Used in autonomous vehicles

### 2. Proximity Sensors

#### Ultrasonic Sensors
- Uses sound waves to measure distance
- Range: 2cm to 4m typically
- Low cost and easy to use
- Weather-resistant
```python
# Example: Ultrasonic sensor reading
def get_distance():
    # Send pulse
    trigger_pin.high()
    time.sleep(0.00001)
    trigger_pin.low()
    
    # Measure echo
    duration = measure_echo()
    distance = (duration * 0.0343) / 2  # Speed of sound
    return distance
```

#### Infrared (IR) Sensors
- Short-range proximity detection
- Line following in mobile robots
- Object detection
- Low cost

### 3. Touch and Force Sensors

#### Tactile Sensors
- Detect physical contact
- Measure pressure and force
- Enable delicate manipulation
- Used in robotic grippers

#### Force/Torque Sensors
- Measure forces in multiple axes
- Essential for precise manipulation
- Collaborative robot safety
- Assembly applications

### 4. Motion Sensors

#### IMU (Inertial Measurement Unit)
- **Accelerometer**: Measures acceleration
- **Gyroscope**: Measures rotation
- **Magnetometer**: Measures magnetic field (compass)

**Applications**:
- Balance and stability
- Orientation tracking
- Motion detection
- Navigation
```python
# Example: IMU data reading
def read_imu():
    accel = imu.get_acceleration()  # (x, y, z)
    gyro = imu.get_gyroscope()      # (roll, pitch, yaw)
    
    # Calculate tilt angle
    tilt = math.atan2(accel.y, accel.z)
    return tilt
```

#### Encoders
- Measure wheel or joint rotation
- Provide position and speed feedback
- Essential for accurate movement
- Types: Optical, Magnetic, Mechanical

### 5. Environmental Sensors

#### Temperature Sensors
- Monitor system temperature
- Prevent overheating
- Environmental awareness

#### Humidity Sensors
- Measure moisture levels
- Agricultural robots
- Environmental monitoring

#### Gas Sensors
- Detect specific gases
- Safety applications
- Environmental monitoring

#### Sound Sensors (Microphones)
- Voice commands
- Sound localization
- Environmental awareness
- Human-robot interaction

## Sensor Fusion

Combining data from multiple sensors for better accuracy and reliability.

### Why Sensor Fusion?
- **Redundancy**: Backup if one sensor fails
- **Accuracy**: Reduce individual sensor errors
- **Completeness**: Get full picture of environment
- **Robustness**: Work in various conditions

### Example: Autonomous Navigation
- **LIDAR**: Precise distance mapping
- **Camera**: Object recognition
- **IMU**: Orientation and movement
- **GPS**: Global position
- **Wheel encoders**: Local movement tracking
```python
# Simple sensor fusion example
def fused_position():
    gps_pos = gps.get_position()
    imu_offset = imu.get_displacement()
    encoder_distance = encoders.get_distance()
    
    # Combine with weights
    fused = (
        gps_pos * 0.5 + 
        imu_offset * 0.3 + 
        encoder_distance * 0.2
    )
    return fused
```

## Sensor Selection Criteria

### 1. Range
- Minimum and maximum detection distance
- Must match application requirements

### 2. Accuracy
- Measurement precision needed
- Trade-off with cost

### 3. Response Time
- How quickly sensor updates
- Critical for fast-moving robots

### 4. Environmental Conditions
- Temperature range
- Water/dust resistance
- Lighting conditions

### 5. Cost
- Budget constraints
- Balance with performance needs

### 6. Size and Weight
- Physical constraints
- Power consumption

## Common Sensor Problems

### 1. Noise
- Random fluctuations in readings
- **Solution**: Filtering, averaging

### 2. Drift
- Gradual change in readings over time
- **Solution**: Calibration, sensor fusion

### 3. Dead Zones
- Areas where sensor doesn't work
- **Solution**: Multiple sensors, different types

### 4. Environmental Interference
- Sunlight affects IR sensors
- Sound affects ultrasonic sensors
- **Solution**: Choose appropriate sensor type

## Sensor Integration Tips

1. **Calibration**: Always calibrate sensors before use
2. **Filtering**: Use moving average or Kalman filters
3. **Error Handling**: Plan for sensor failures
4. **Testing**: Test in actual operating conditions
5. **Documentation**: Keep track of sensor specifications

---

*Next: Understanding Actuators →*