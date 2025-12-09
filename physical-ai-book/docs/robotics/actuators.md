---
sidebar_position: 3
---

# Actuators in Robotics

Actuators are the "muscles" of robots, converting electrical signals into physical motion.

## What are Actuators?

Actuators are components that create motion in robots by converting energy (electrical, pneumatic, hydraulic) into mechanical movement.

## Types of Actuators

### 1. Electric Motors

#### DC Motors
**Simple DC Motors**
- Continuous rotation
- Speed controlled by voltage
- Inexpensive and widely available
- Used for wheels, fans, pumps
```python
# Example: DC motor control
def control_motor(speed, direction):
    if direction == "forward":
        motor_pin1.high()
        motor_pin2.low()
    else:
        motor_pin1.low()
        motor_pin2.high()
    
    pwm.duty_cycle(speed)  # 0-100%
```

**Servo Motors**
- Precise angular position control
- Typically 0-180° or 0-360° rotation
- Built-in position feedback
- Used for robot joints, grippers

**Types of Servos**:
- **Standard**: 180° rotation
- **Continuous**: Full 360° rotation
- **Digital**: More precise, faster response
```python
# Example: Servo control
def move_servo(angle):
    servo.angle = angle  # 0-180 degrees
    time.sleep(0.5)  # Wait for movement
```

**Stepper Motors**
- Move in discrete steps (e.g., 1.8° per step)
- Precise positioning without feedback
- Hold position when powered
- Used in 3D printers, CNC machines

**Advantages**:
- No position sensor needed
- Repeatable positioning
- High holding torque

#### Brushless DC Motors (BLDC)
- Higher efficiency than brushed motors
- Longer lifespan
- More expensive
- Require electronic speed controller (ESC)
- Used in drones, high-performance robots

### 2. Pneumatic Actuators

Uses compressed air to create motion.

#### Linear Actuators (Cylinders)
- Push/pull motion
- Fast response time
- Clean operation
- Used in pick-and-place robots

#### Rotary Actuators
- Rotational motion from air pressure
- Limited rotation angle
- High torque capability

**Advantages**:
- Simple and reliable
- Fast actuation
- Clean (no oil leaks)
- Safe in explosive environments

**Disadvantages**:
- Requires air compressor
- Difficult to control precisely
- Noisy operation

### 3. Hydraulic Actuators

Uses pressurized fluid (oil) to create motion.

#### Hydraulic Cylinders
- Very high force capability
- Smooth operation
- Used in heavy industrial robots
- Construction equipment

#### Hydraulic Motors
- High power density
- Continuous rotation
- Heavy-duty applications

**Advantages**:
- Extremely high force
- Smooth, controllable motion
- Self-lubricating

**Disadvantages**:
- Expensive
- Requires hydraulic pump
- Potential oil leaks
- Maintenance intensive

### 4. Specialized Actuators

#### Linear Actuators
- Convert rotary motion to linear
- Electric screw drives
- Used for extending/retracting

#### Piezoelectric Actuators
- Extremely precise (nanometer scale)
- Very fast response
- Limited motion range
- Used in precision instruments

#### Shape Memory Alloys (SMA)
- Change shape when heated
- Artificial muscles
- Compact and lightweight
- Used in soft robotics

#### Electroactive Polymers (EAP)
- Deform when voltage applied
- Flexible artificial muscles
- Still in research phase
- Potential for humanoid robots

## Motor Control Techniques

### 1. PWM (Pulse Width Modulation)
Control motor speed by varying pulse width.
```python
# PWM speed control
def set_speed(percent):
    # 0-100% speed
    pwm_value = (percent / 100) * 255
    motor_pwm.write(pwm_value)
```

### 2. PID Control
Maintain desired position/speed accurately.
```python
# Simple PID controller
class PIDController:
    def __init__(self, kp, ki, kd):
        self.kp = kp  # Proportional gain
        self.ki = ki  # Integral gain
        self.kd = kd  # Derivative gain
        self.prev_error = 0
        self.integral = 0
    
    def calculate(self, setpoint, current_value):
        error = setpoint - current_value
        self.integral += error
        derivative = error - self.prev_error
        
        output = (
            self.kp * error +
            self.ki * self.integral +
            self.kd * derivative
        )
        
        self.prev_error = error
        return output
```

### 3. Encoder Feedback
Use encoder to monitor actual position/speed.
```python
# Encoder-based position control
def move_to_position(target_position):
    while True:
        current_pos = encoder.read()
        error = target_position - current_pos
        
        if abs(error) < 5:  # Close enough
            motor.stop()
            break
        
        speed = pid.calculate(target_position, current_pos)
        motor.set_speed(speed)
```

## Motor Specifications

### Key Parameters

**1. Torque**
- Rotational force capability
- Measured in N⋅m or kg⋅cm
- Higher = can lift heavier loads

**2. Speed (RPM)**
- Rotations per minute
- Trade-off with torque
- Gear reduction affects both

**3. Voltage and Current**
- Operating voltage (e.g., 12V, 24V)
- Current draw (affects battery life)
- Stall current (maximum when blocked)

**4. Efficiency**
- Energy converted to useful work
- Affects battery runtime
- Typically 60-90%

### Selecting the Right Motor

Consider:
1. **Required torque** for your load
2. **Speed requirements**
3. **Precision needed** (servo vs DC)
4. **Power supply** constraints
5. **Size and weight** limitations
6. **Cost** budget

## Motor Drivers

Motors require driver circuits to control them safely.

### H-Bridge
- Controls DC motor direction and speed
- Examples: L298N, L293D
- Allows forward/reverse/brake

### Servo Controller
- Generates PWM signals for servos
- Can control multiple servos
- Examples: PCA9685

### Stepper Motor Driver
- Provides correct stepping sequence
- Examples: A4988, DRV8825
- Micro-stepping capability

## Gearboxes and Transmissions

### Purpose
- Increase torque (reduce speed)
- Reduce speed (increase torque)
- Change motion direction

### Gear Ratio
```
Gear Ratio = Output Speed / Input Speed
Torque Multiplication = 1 / Gear Ratio
```

**Example**: 100:1 gearbox
- Motor: 3000 RPM, 1 N⋅m torque
- Output: 30 RPM, 100 N⋅m torque

### Types
- **Spur gears**: Simple, efficient
- **Planetary**: Compact, high torque
- **Worm gears**: High ratio, self-locking

## Safety Considerations

1. **Current limiting**: Prevent motor damage
2. **Emergency stop**: Quick power cutoff
3. **Soft start**: Gradual acceleration
4. **Overheating protection**: Temperature monitoring
5. **Mechanical stops**: Prevent over-extension

## Common Problems and Solutions

### Motor Not Moving
- Check power supply
- Verify connections
- Test with multimeter
- Check driver chip

### Overheating
- Reduce duty cycle
- Add heat sinks
- Improve ventilation
- Check for mechanical binding

### Jittery Movement
- Improve PID tuning
- Check mechanical friction
- Verify power supply stability
- Add decoupling capacitors

### Insufficient Torque
- Check gear ratio
- Verify voltage level
- Reduce load weight
- Consider larger motor

---

*Next: Explore Future Trends in AI →*