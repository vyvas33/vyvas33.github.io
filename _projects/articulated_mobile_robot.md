---
layout: page
title: Articulated Mobile Robot
description: A modular center-articulated multi-modal robot for complex environments
importance: 3
category: work
github: vyvas33/articulated_mobile_robot
related_publications: true
---

**My role:** I redesigned the robot so it moves reliably in inclined pipes. I also modeled its kinematics and dynamics, simulated them in MATLAB, and prototyped the robot.

<div class="row justify-content-sm-center">
    <div class="col-sm-8 mt-3 mt-md-0">
        {% include figure.liquid loading="eager" path="assets/img/assembled_robot_nobg.png" title="assembled robot" class="img-fluid rounded z-depth-0" %}
    </div>
</div>
<div class="caption">
    The assembled robot
</div>

Pipelines carrying gas, water and sewage need constant monitoring for clogging, aging, cracks and corrosion. They often run underground or inside complex infrastructure, which makes them hard and costly to inspect from outside. Inspection robots can reach places people can't, but most are built for just one environment: inside a pipe or on open ground. Many also struggle with bends, T-junctions and vertical sections. The goal of this project was one modular robot that can inspect pipes with bends and then drive over uneven terrain, without swapping hardware.

### Design

The robot has two driven modules, a base and a trailer, connected by a novel 2-DoF joint. A bevel-gear differential driven by two servo motors actuates the joint. On the ground, the robot steers by articulating about the vertical axis, like center-articulated Load-Haul-Dump vehicles. The pitch mode lets it follow bends and climb obstacles inside pipes.

In pipes, a wall-press mechanism keeps the wheels pushed against the walls. It uses a pantograph linkage with a spring and a lead screw. The spring absorbs small changes in pipe diameter, and when the normal force goes beyond acceptable limits, the lead screw adjusts the legs actively. On the ground, the robot needs a wider stance to stay stable. A configurable wheel distance mechanism slides each omnidirectional wheel along a hexagonal shaft to widen or narrow the support polygon.

Testing the first design showed three problems, which drove most of my redesign:

- **Worm gears lost too much torque.** I replaced them with a spur gear transmission. A SolidWorks Motion study of vertical pipe traversal showed the wheels needed about 2 Nm, so I chose 40 kg-cm Waveshare motors and redesigned the leg module around them.
- **The joint servos were too weak.** The study showed the joint needs about 60 kg-cm of peak torque per motor. The original 50 kg-cm servos caused unstable articulation on inclines, so I replaced them with 120 kg-cm Waveshare RSBL120-24 servos with magnetic encoders, and redesigned the joint housing.
- **Wheels had to rotate and slide in the same compact leg.** The hexagonal shaft solved this, because its cross-section carries the wheel's rotation while a lead screw moves the wheel along it.

### Modeling and Simulation

I developed kinematic, dynamic and static force models. The kinematics treat the robot as a base and trailer coupled by the articulation angle. I derived the dynamics with the Lagrangian method and simulated them in MATLAB across four cases: free response, wheel torque with and without joint damping, and combined wheel and joint actuation under damping. Across these torque and damping conditions, the simulated articulation was smooth and controlled. The static model relates the wall-press force to spring compression, friction and rolling resistance.

### Testing and Evaluation

I fabricated the prototype with 3D printing and precision machining, and operated it by radio teleoperation. I tested it in an inclined straight pipe with a 400 mm inner diameter, through a 90-degree bend, and on flat and uneven ground. In all three, it moved responsively and stably, and the joint articulated efficiently.

<div class="row justify-content-sm-center">
    <div class="col-sm-10 mt-3 mt-md-0">
        {% include video.liquid path="assets/video/multimodal_robot_demo.mp4" class="img-fluid rounded z-depth-1" controls=true autoplay=true loop=true muted=true %}
    </div>
</div>
<div class="caption">
    The robot traversing in-pipe and on-ground environments (3&times; speed).
</div>

### Conclusion

The robot works as a single platform for both pipes and open ground. The control and localization work is in our 2026 journal paper {% cite paper %}, and the full design report is available <a href="{{ 'assets/pdf/Report.pdf' | relative_url }}" target="_blank">here</a>. The wall-press mechanism has a load sensor, so the next step is real-time force feedback with slip detection, to regulate normal force and driving torque and cut wheel slip.
