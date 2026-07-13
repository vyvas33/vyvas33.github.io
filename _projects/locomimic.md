---
layout: page
title: LocoMimic
description: "Learning to walk using reinforcement learning."
importance: 2
category: work
github: vyvas33/loco_mimic
---

<p class="text-muted" style="font-size: 0.9rem;">
Introduction to Robot Learning course project | Carnegie Mellon University | Spring 2026<br>
<strong>My focus:</strong> off-policy RL
</p>

> On a single environment, SAC matched and beat PPO at equal environment interactions, but scaling to thousands of parallel environments made it collapse mid-training. With a combination of fixes, **MeanSAC** eliminated the collapses and raised mean return from 13.3 to 30.0.

Teaching a robot to walk is hard. Teaching it to walk like a human is harder. Most locomotion and whole body controller approaches rely on hand-crafted reward functions that tell the robot what good walking looks like, stay upright, move forward, don't fall. We take a different approach. Instead of defining walking, we show it. The robot learns to imitate the motion directly from a clip.

We train a policy using reinforcement learning on the Unitree G1 humanoid in MuJoCo. The reward function is built on ideas from DeepMimic [1] and BeyondMimic [2]. At each timestep the robot is rewarded for how closely its body positions, orientations, and velocities match a reference walking motion from the LAFAN1 dataset [3].

We compare two algorithms, PPO [4] and SAC [5], but my focus was on getting SAC to work. SAC is an off-policy method that learns from stored past experience rather than discarding it after each update, making it substantially more sample efficient than on-policy methods like PPO. The catch is that this efficiency comes with fragility: the critic can overestimate Q-values in ways that quietly poison training.

I started small, with a single environment in MuJoCo. At that scale it worked, it matched and even beat PPO for the same number of environment interactions. The problem showed up when I scaled it up. Training fast means running thousands of environments in parallel to collect experience, and at that scale vanilla SAC broke.

Every SAC run followed the same pattern: reward peaks, collapses, and never recovers. Diagnosing it took a mix of architectural changes, training procedure adjustments, and a closer look at how the environment interacts with off-policy learning. The result is MeanSAC, which replaces the standard min-Q target with a mean-Q target and adds LayerNorm to the critic, following recent recipes for fast, stable off-policy RL in humanoid control, FastSAC [6] and FastTD3 [7]. Evaluated after 800 million training steps, these changes raised mean return from 13.3 to 30.0 and mean episode length from 237 to 490 steps.

PPO still evaluated higher after the same 800M steps, but the reward was tuned for PPO from the start. At single-environment scale SAC was actually the stronger of the two; the point of MeanSAC was to keep that working once I scaled up.

<div class="row justify-content-sm-center mt-3">
    <div class="col-sm-10 mt-3 mt-md-0">
        {% include figure.liquid loading="eager" path="assets/img/sac_vs_meansac.png" class="img-fluid rounded z-depth-1" %}
    </div>
</div>
<div class="caption">
    Vanilla SAC (red) collapses mid-training around 200M steps and never fully recovers. MeanSAC (purple) holds a higher, stable return and episode length across 800M steps.
</div>

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

<hr>

##### References

<div style="font-size: 0.85rem;" markdown="1">

1. X. B. Peng, P. Abbeel, S. Levine, M. van de Panne. "DeepMimic: Example-Guided Deep Reinforcement Learning of Physics-Based Character Skills." *ACM Transactions on Graphics*, 2018. [doi:10.1145/3197517.3201311](https://doi.org/10.1145/3197517.3201311)
2. Q. Liao et al. "BeyondMimic: From Motion Tracking to Versatile Humanoid Control via Guided Diffusion." 2025. [arXiv:2508.08241](https://arxiv.org/abs/2508.08241)
3. Lvhaidong. "LAFAN1 Retargeting Dataset." Hugging Face, 2024. [link](https://huggingface.co/datasets/lvhaidong/LAFAN1_Retargeting_Dataset)
4. J. Schulman, F. Wolski, P. Dhariwal, A. Radford, O. Klimov. "Proximal Policy Optimization Algorithms." 2017. [arXiv:1707.06347](https://arxiv.org/abs/1707.06347)
5. T. Haarnoja, A. Zhou, P. Abbeel, S. Levine. "Soft Actor-Critic: Off-Policy Maximum Entropy Deep Reinforcement Learning with a Stochastic Actor." 2018. [arXiv:1801.01290](https://arxiv.org/abs/1801.01290)
6. Y. Seo, C. Sferrazza, J. Chen, G. Shi, R. Duan, P. Abbeel. "Learning Sim-to-Real Humanoid Locomotion in 15 Minutes." 2025. [arXiv:2512.01996](https://arxiv.org/abs/2512.01996)
7. Y. Seo, C. Sferrazza, H. Geng, M. Nauman, Z.-H. Yin, P. Abbeel. "FastTD3: Simple, Fast, and Capable Reinforcement Learning for Humanoid Control." 2025. [arXiv:2505.22642](https://arxiv.org/abs/2505.22642)

</div>

