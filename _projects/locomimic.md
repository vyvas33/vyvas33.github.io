---
layout: page
title: LocoMimic
description: "Learning to walk using reinforcement learning."
importance: 1
category: work
github: vyvas33/loco_mimic
---
Teaching a robot to walk is hard. Teaching it to walk like a human is harder. Most locomotion and whole body controller approaches rely on hand-crafted reward functions that tell the robot what good walking looks like, stay upright, move forward, don't fall. We take a different approach. Instead of defining walking, we show it. The robot learns to imitate the motion directly.

We train a policy using reinforcement learning on the Unitree G1 humanoid in MuJoCo. The reward function is built on ideas from DeepMimic and BeyondMimic. At each timestep the robot is rewarded for how closely its body positions, orientations, and velocities match a reference walking motion from the LAFAN1 dataset.

We compare two algorithms, PPO and SAC, but my focus was on getting SAC to work. SAC is an off-policy method that learns from stored past experience rather than discarding it after each update, making it substantially more sample efficient than on-policy methods like PPO. The catch is that this efficiency comes with fragility: the critic can overestimate Q-values in ways that quietly poison training.

That's exactly what we saw. Every SAC run followed the same pattern, reward peaks, collapses, and never recovers. Diagnosing and addressing this took a combination of architectural changes, training procedure adjustments, and a closer look at how the environment itself interacts with off-policy learning. The result of that work is MeanSAC, which replaces the standard min-Q target with a mean-Q target alongside LayerNorm in the critic. Together these changes brought mean return from 13.3 to 30.0 and mean episode length from 237 to 490 steps across 800 million environment steps.

However, PPO ultimately scored higher. Although SAC is theoretically more sample efficient, it converged to a lower mean training return than PPO at 800M steps. We attribute this primarily to the fact that the reward formulation was highly tuned for PPO.

<div class="row mt-3 justify-content-center">
    <div class="col-sm-4 mt-3 mt-md-0 text-center">
        {% include figure.liquid loading="eager" path="assets/img/ppo.gif" class="img-fluid rounded z-depth-1" caption="PPO" %}
    </div>
    <div class="col-sm-4 mt-3 mt-md-0 text-center">
        {% include figure.liquid loading="eager" path="assets/img/sac.gif" class="img-fluid rounded z-depth-1" caption="SAC" %}
    </div>
    <div class="col-sm-4 mt-3 mt-md-0 text-center">
        {% include figure.liquid loading="eager" path="assets/img/fast_sac.gif" class="img-fluid rounded z-depth-1" caption="MeanSAC" %}
    </div>
</div>

<div class="mt-4 text-center">
    For training plots and full results, see the <a href="https://sites.google.com/andrew.cmu.edu/locomimic/" target="_blank">project website</a>. The full report is available <a href="{{ 'assets/pdf/LocoMimic_Report.pdf' | relative_url }}" target="_blank">here</a>.
</div>

