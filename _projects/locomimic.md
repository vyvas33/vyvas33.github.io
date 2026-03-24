---
layout: page
title: LocoMimic
description: "Learning to walk using reinforcement learning."
importance: 1
category: work
github: vyvas33/loco_mimic
---

Teaching a robot to walk is hard. Teaching it to walk like a human is harder. Most locomotion and whole body controller approaches rely on hand-crafted reward functions that tell the robot what good walking looks like, e.g. stay upright, move forward, don't fall. We take a different approach. Instead of defining walking, we show it. The robot learns to imitate the motion directly.

We train a policy using reinforcement learning on the Unitree G1 humanoid in MuJoCo. The reward function is built on ideas from DeepMimic and BeyondMimic. At each timestep the robot is rewarded for how closely its body positions, orientations, and velocities match a reference walking motion from the LAFAN1 dataset.

We use Soft Actor-Critic (SAC), an off-policy method that learns from stored past experience rather than discarding it after each update. This makes it substantially more sample efficient than on-policy methods. After 1 million environment steps, SAC produces a policy that shows clear imitation behavior. The robot attempts to follow the reference motion and maintains balance for meaningful stretches of time. A PPO baseline trained under identical conditions has not yet converged at the same sample count, which is consistent with the sample efficiency advantage SAC is known for.

The video below shows the trained SAC policy alongside the reference motion it is trying to imitate.

<div class="row mt-3 justify-content-center">
    <div class="col-sm-8 col-md-6 mt-3 mt-md-0 mx-auto text-center d-flex justify-content-center">
        <video src="{{ 'assets/video/sac_tracking_v2_1M_steps.mp4' | relative_url }}" class="img-fluid rounded z-depth-1" controls autoplay loop muted playsinline></video>
    </div>
</div>

With more training time the policy should improve considerably. One million steps is modest by motion imitation standards, and the reward curve was still trending upward at the end of training.

---

**Status:** *This project is still under progress. We aim to extend this to learning a controller for a musculoskeletal human model, which involves a significantly higher dimensional space and complex mechanics.*

### References
1. Peng, X. B., Abbeel, P., Berseth, G., & van de Panne, M. (2018). *DeepMimic: Example-Guided Deep Reinforcement Learning of Physics-Based Character Skills*. ACM Transactions on Graphics (TOG).
2. Liao, Q., Truong, T. E., Huang, X., Gao, Y., Tevet, G., Sreenath, K., & Liu, C. K. (2025). *BeyondMimic: From Motion Tracking to Versatile Humanoid Control via Guided Diffusion*. arXiv:2508.08241.
3. Haarnoja, T., Zhou, A., Abbeel, P., & Levine, S. (2018). *Soft Actor-Critic: Off-Policy Maximum Entropy Deep Reinforcement Learning with a Stochastic Actor*. ICML.
4. Amazon Frontier AI & Robotics (FAR). *Fast SAC (Learning Sim-to-Real Humanoid Locomotion in 15 Minutes)*. 
