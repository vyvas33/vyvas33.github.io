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

Amputees spend more energy walking than able-bodied people, and mechanically passive prostheses make this worse. Active prostheses can help by performing positive work while walking. But high-level decisions are needed to control the behavior of the prosthesis, and these depend on the state of the robotic leg as well as the human's intent. The goal of this project is to build that controller for a powered knee-ankle prosthesis, so that it works across walking speeds and feels comfortable to the user.

<div class="row justify-content-sm-center">
    <div class="col-12 mt-3 mt-md-0">
        {% include video.liquid path="assets/video/prosthesis_walking_v2.mp4" class="img-fluid rounded z-depth-1" controls=true autoplay=true loop=true muted=true %}
    </div>
</div>
<div class="caption">
    Walking on the treadmill
</div>

### Design

I implement two high-level controllers: the bioinspired **Neuromuscular Control** for the stance phase of walking, and **Minimum Jerk Control** for the swing phase. The high-level controller consumes the prosthesis state as well as human hip features to make control decisions. To get those hip features, I implement an **Error State Kalman Filter** that estimates the hip angle and position by fusing two IMUs.

### Hardware

The leg itself was designed and built in earlier work in the lab [1]. The motors on the leg are controlled by Elmo motor drives, one each for the knee and ankle. Ground reaction sensors and two encoders per joint feed a custom MCU. The drives and the MCU talk to a Jetson Orin over EtherCAT, which I built on PySOEM, a Python library. Raw sensor data goes into the state estimator, the estimator's output goes to the high-level controller, and the low-level controller uses that to command the motors.

<div class="row justify-content-sm-center">
    <div class="col-sm-8 mt-3 mt-md-0">
        {% include figure.liquid loading="eager" path="assets/img/cmu_leg.png" title="the prosthesis" class="img-fluid rounded z-depth-0" %}
    </div>
</div>
<div class="caption">
     CMU Powered Prosthesis Leg
</div>

Both joints are series-elastic: the joint and the motor are connected through a spring, which lets us measure torque for free, from the spring deflection rather than a dedicated torque sensor. The low-level controller I implemented is velocity-based SEA control. It computes a velocity command and a feedforward torque from a dynamic model of the rotor, and sends the velocity command to the drives in velocity mode.

<!-- <div class="row justify-content-sm-center">
    <div class="col-12 mt-3 mt-md-0">
        {% include video.liquid path="assets/video/prosthesis_standing.mp4" class="img-fluid rounded z-depth-1" controls=true autoplay=true loop=true muted=true %}
    </div>
</div>
<div class="caption">
    Standing controller on the prosthesis
</div> -->

### State Estimation

The pose of the human thigh is estimated by an Error State Kalman Filter [2, 3] that fuses two IMUs and the joint encoders. The IMUs sit on the prosthesis foot and the human thigh. The foot IMU is corrected using ZUPT (zero-velocity update) [4, 5], and the thigh IMU is corrected by propagating the foot IMU's readings through forward kinematics, using the joint angles from the encoders.

### Control

The Neuromuscular controller [6] is model-based and computes stance-phase joint torques by simulating muscles and neural pathways. It was first applied to a powered prosthesis on this platform in [1]. We simulate three muscle groups: the Vasti, Gastrocnemius and Soleus. From the current joint angles and the hip angle, the muscles generate forces, and the moment arms turn those forces into desired torques. The velocity-based SEA control then tracks the torques.

During swing, the controller computes minimum-jerk reference trajectories for the knee and ankle, where jerk is the rate of change of acceleration. If we use the Euler-Lagrange equation to find the minimum, the trajectory turns out to be a quintic polynomial, so it costs almost nothing to compute in real time.

### Evaluation

I tested the Error State Kalman Filter offline against previously logged data before putting it on the leg. I then tested the controllers by walking with the prosthesis on a split-belt instrumented treadmill. A bypass socket lets able-bodied individuals use the prosthesis. The control is independent of walking speed, and I tested it at speeds from 0.7 to 1.3 m/s. The most common source of control errors was the state machine that switches between swing and stance based on contact.

### Conclusion and What Next?

The controllers work on hardware across the speeds I tested. However, they mainly work for level walking and inclines. I want to develop an end-to-end controller that works across different locomotion modes. Reinforcement learning in simulation is a promising way to learn such a controller, but it needs an accurate model of the human and prosthesis system to learn from. So I'm exploring how we can simulate that system, learn the control policy in simulation, and deploy it zero-shot without extensive tuning on hardware.

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
