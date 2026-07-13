---
layout: page
title: Articulated Mobile Robot
description: A modular center-articulated multi-modal robot for complex environments
importance: 3
category: work
github: vyvas33/articulated_mobile_robot
related_publications: true
---

<div class="row justify-content-sm-center">
    <div class="col-sm-8 mt-3 mt-md-0">
        {% include figure.liquid loading="eager" path="assets/img/assembled_robot_nobg.png" title="assembled robot" class="img-fluid rounded z-depth-0" %}
    </div>
</div>
<div class="caption">
    The assembled robot
</div>

Pipeline inspection robots are typically built for one environment: inside a pipe or on open ground. This robot does both. The goal was a single platform that could traverse straight pipes, navigate bends and junctions, and then drive across uneven terrain without swapping hardware.

The robot consists of two driven modules, a front (base) module and a rear (trailer) module, connected by a novel 2-DoF joint actuated through a bevel-gear differential driven by two servo motors. Steering on the ground is achieved by articulating the two modules about the vertical axis, exactly the way center-articulated vehicles like LHD machines turn, while the joint's pitch mode lets the robot follow vertical bends and climb over obstacles inside pipes. A SolidWorks Motion study showed the joint demands roughly 60 kg-cm of peak torque per motor; the earlier 50 kg-cm servos fell short and caused unstable articulation on inclines, so they were replaced with 120 kg-cm Waveshare RSBL120-24 servos with magnetic encoders for closed-loop position feedback.

Each leg carries a wall-press mechanism built around a pantograph linkage with a spring and a lead-screw active adjustment. The spring handles small variations in pipe diameter passively; when the normal force exceeds acceptable limits, the motor-driven lead screw engages to actively reposition the legs. This lets the robot maintain traction in pipes of varying diameter without operator input.

For ground locomotion, the inter-wheel distance needs to be wider than the in-pipe configuration to maintain stability. A configurable wheel distance mechanism handles this: each omnidirectional wheel rides on a hexagonal shaft through a linear bearing, so the shaft's cross-section couples wheel rotation while a lead screw slides the wheel along it, expanding or contracting the support polygon on demand. The drive itself started out using worm gears, but experiments revealed significant torque losses; these were replaced with a spur-gear transmission, and a SolidWorks Motion study of vertical pipe traversal (showing a ~2 Nm requirement) led to selecting 40 kg-cm Waveshare drive motors.

Kinematic, dynamic, and static force models of the robot were developed. The kinematics treat the platform as a base–trailer pair coupled by the articulation angle, and the dynamics were derived using the Lagrangian formulation, reduced to eliminate the constraint multipliers, and studied in simulation across free-response, wheel-torque, and damped joint-actuation cases. The static model relates wall-press force to spring compression, friction, and rolling resistance. The prototype was fabricated using a combination of 3D printing and precision machining and tested across straight pipes, bends, and uneven ground, demonstrating robust mobility and adaptable configuration in all three environments.

The control and localization side of this platform is detailed in our journal paper {% cite paper %}, and the full design report is available <a href="{{ 'assets/pdf/Report.pdf' | relative_url }}" target="_blank">here</a>.

<div class="row justify-content-sm-center">
    <div class="col-sm-10 mt-3 mt-md-0">
        {% include video.liquid path="assets/video/multimodal_robot_demo.mp4" class="img-fluid rounded z-depth-1" controls=true autoplay=true loop=true muted=true %}
    </div>
</div>
<div class="caption">
    The robot traversing in-pipe and on-ground environments (3&times; speed).
</div>
