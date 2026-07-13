---
layout: page
title: Powered Knee-Ankle Prosthesis 
description: "Low-level hardware control for a powered lower-limb prosthesis"
importance: 1
category: work
github: vyvas33/cmu_leg
_styles: |
  .post img {
    max-height: 300px;  
  }

---

<p class="text-muted" style="font-size: 0.9rem;">
Legged Systems Group, Robotics Institute | Carnegie Mellon University | Ongoing<br>
</p>

A number of control strategies have been developed for lower-limb
prostheses, but current approaches still struggle with generalization and recognizing human intent. Reinforcement learning combined with learning in simulation is a promising way to address both but testing that idea requires iteration on control strategies quickly, and the CMU Leg's control stack was built to run on a Simulink Real-Time target, not something suited to fast experimentation, especially for learning based approaches. So, I built the control stack on Python.

### Hardware Overview
The motors on the leg are controlled by Elmo motor drives, one each for the
knee and ankle. Ground reaction sensors and two encoders
per joint feed a custom MCU. The drives and the MCU talk to a Jetson Orin over EtherCAT.

<div class="row justify-content-sm-center">
    <div class="col-sm-8 mt-3 mt-md-0">
        {% include figure.liquid loading="eager" path="assets/img/cmu_leg.png" title="the prosthesis" class="img-fluid rounded z-depth-0" %}
    </div>
</div>
<div class="caption">
     CMU Powered Prosthesis Leg
</div>

The EtherCAT interface is built on PySOEM, a Python library. Raw sensor
data is fed into a state estimator, which outputs the state used by the
high-level controller, the low-level controller then uses that output to
command the motors.

Both the knee and ankle joints are series-elastic which means the joint and the motor are
connected through a spring, which lets us measure torque for free, from
the spring deflection rather than a dedicated torque sensor. The low-level
controller here is velocity-based SEA control. It computes a velocity
command and a feedforward torque from a dynamic model of the rotor, and
sends the velocity command to the drives in velocity mode.

<div class="row justify-content-sm-center">
    <div class="col-12 mt-3 mt-md-0">
        {% include video.liquid path="assets/video/prosthesis_standing.mp4" class="img-fluid rounded z-depth-1" controls=true autoplay=true loop=true muted=true %}
    </div>
</div>
<div class="caption">
    Standing controller on the prosthesis
</div>

### Control Testing
To stand, the leg first moves each joint to a zero position along a
min-jerk trajectory, a smooth start-to-end motion profile that
minimizes jerk (the rate of change of acceleration). 

Early on, this control oscillated. Two things possibly fed into it 1) the control loop
was only reliably hitting around 750 Hz instead of the target 1 kHz, which
effectively inflated the velocity commands the control law was sending 2) there was a torque bias showing up even under no load, which was poisoning a few terms in the SEA control. Recalibrating the
joint encoders against the motor-side encoders removed the bias, and after making the loop itself more efficient  enough to hold a steady 1 kHz, the
oscillations were gone.
