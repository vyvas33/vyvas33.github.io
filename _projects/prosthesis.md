---
layout: page
title: Robotic Lower-Limb Prosthesis Control
description: "Sensing, estimation and control for a powered knee-ankle prosthesis"
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

Amputees suffer from increased energy consumption, and this is aggravated by mechanically passive prostheses. Active prostheses can help by performing positive work while walking. However, high-level decisions are needed to control the behavior of the prosthesis. These high-level control decisions are dependent on the state of the robotic leg, as well as the human's intent. 

In this work, I develop the control stack for the prosthesis, from reading raw sensor frames to commanding the motors. I implement two high-level controllers, the bioinspired **Neuromuscular Control** for the stance phase of walking, and the Minimum Jerk Control for the swing phase. The controllers depend on the hip cue of the human in some stages of the controller. Here, I implement an **Error State Kalman Filter** to estimate the hip angle by fusing two IMUs. Finally, I test the controllers on an instrumented treadmill and tune them to the human's comfort.

### Hardware Overview
The leg itself was designed and built in earlier work in the lab [1]. The motors on the leg are controlled by Elmo motor drives, one each for the
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

Both the knee and ankle joints are series-elastic, which means the joint and the motor are
connected through a spring, which lets us measure torque for free, from
the spring deflection rather than a dedicated torque sensor. The low-level
controller implemented here is velocity-based SEA control. It computes a velocity
command and a feedforward torque from a dynamic model of the rotor, and
sends the velocity command to the drives in velocity mode.

<!-- <div class="row justify-content-sm-center">
    <div class="col-12 mt-3 mt-md-0">
        {% include video.liquid path="assets/video/prosthesis_standing.mp4" class="img-fluid rounded z-depth-1" controls=true autoplay=true loop=true muted=true %}
    </div>
</div>
<div class="caption">
    Standing controller on the prosthesis
</div> -->

### State Estimation
The pose of the human leg (thigh) is estimated by an Error State Kalman Filter [2, 3] that fuses two IMUs and the joint encoders. The two IMUs are placed on the prosthesis foot and the human thigh. The foot IMU is corrected using ZUPT (Zero-velocity update) [4, 5] and the thigh IMU is corrected by propagating the foot IMU's readings through forward kinematics, using the joint angles read from the encoders.

### Control 
The Neuromuscular controller [6] is a model based controller that computes stance phase joint torques by simulating muscles and neural pathways. It was first applied to a powered prosthesis on this platform in [1]. We simulate three muscle groups, namely Vasti, Gastrocnemius and the Soleus group. Based on the current joint angles and the hip angle, the muscles generate forces, from which desired torques are computed through the moment arm. The torques are then tracked by the velocity based SEA control.  

During swing, the controller computes minimum jerk reference trajectories for the knee and the ankle, such that the jerk (the rate of change of acceleration) is minimum across the trajectory. If we use the Euler-Lagrange equation to compute the minimum, we realize that the trajectory is just a quintic polynomial, so it costs almost nothing in real time to compute the trajectory. 

### Testing 

We test the controllers by walking with the prosthesis on a split-belt instrumented treadmill. We use a bypass socket so able-bodied individuals can use the prosthesis and test the controllers.

<div class="row justify-content-sm-center">
    <div class="col-12 mt-3 mt-md-0">
        {% include video.liquid path="assets/video/prosthesis_walking.mp4" class="img-fluid rounded z-depth-1" controls=true autoplay=true loop=true muted=true %}
    </div>
</div>
<div class="caption">
    Walking on the treadmill
</div>


### What next?

A common source of control errors I encountered during testing was the state machine that switches between swing and stance based on contact. To avoid these switches, I want to develop an end-to-end controller that does not rely on finite states.

Reinforcement learning is a promising way to learn such a controller, but it needs an accurate model of the human and prosthesis system to learn from. So I'm exploring how we can simulate that system, learn the control policy in simulation, and deploy it zero-shot without extensive tuning on hardware.

<hr>

##### References

<div style="font-size: 0.85rem;" markdown="1">

1. N. Thatte. "Design and Evaluation of Robust Control Methods for Robotic Transfemoral Prostheses." PhD thesis, Robotics Institute, Carnegie Mellon University, 2019. [link](https://www.proquest.com/dissertations-theses/design-evaluation-robust-control-methods-robotic/docview/2458563444/se-2)
2. J. Sola. "Quaternion kinematics for the error-state Kalman filter." 2017. [arXiv:1711.02508v1](https://arxiv.org/abs/1711.02508v1)
3. A. R. Jimenez, F. Seco, J. C. Prieto, J. Guevara. "Indoor Pedestrian Navigation using an INS/EKF framework for Yaw Drift Reduction and a Foot-mounted IMU." *Workshop on Positioning, Navigation and Communication (WPNC)*, 2010.
4. I. Skog, P. Handel, J.-O. Nilsson, J. Rantakokko. "Zero-Velocity Detection - An Algorithm Evaluation." *IEEE Transactions on Biomedical Engineering*, 2010.
5. J. Tao et al. "An enhanced foot-mounted PDR method with adaptive ZUPT and multi-sensors fusion for seamless pedestrian navigation." *GPS Solutions*, 2022.
6. H. Geyer, H. Herr. "A Muscle-Reflex Model That Encodes Principles of Legged Mechanics Produces Human Walking Dynamics and Muscle Activities." *IEEE Transactions on Neural Systems and Rehabilitation Engineering*, 2010.

</div>
