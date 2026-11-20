---
layout: page
title: Neuromuscular Models
description: "Hill-type muscle models and reflex-driven hopping"
importance: 4
category: work
github: vyvas33/hopping_model
---

**My role:** I implemented a simulation of vertical hopping in Python, with a Hill-type muscle model and a reflex controller, based on Geyer, Seyfarth and Blickhan (2003) [1].

Legged robots and prostheses need controllers that produce efficient, stable motion, and biological muscles do this through their own mechanics and reflexes. Hopping is the simplest bouncing gait, so it is a good place to study those reflexes. The objective of this project was to build a muscle-reflex model of hopping, and to check that a single muscle with reflex feedback is enough to produce stable hopping. The same principles can later drive the legs of a robot or a prosthesis.

![Muscle Animation](https://raw.githubusercontent.com/vyvas33/muscle_model/main/muscle_animation.gif)

### The Model

Hopping alternates between stance and flight. During stance, the leg is on the ground and the muscle pushes the body upward. During flight, the body moves only under gravity. I model the body as an 80 kg point mass on a two-segment, mass-less leg, with one extensor muscle acting across the knee.

The muscle-tendon complex is a Hill-type model, based on experiments on how muscle force depends on length and velocity. It has three parts: a contractile element, a parallel passive element and a series elastic element. A neural input, $$STIM(t)$$, sets the muscle's activation. It is a small constant bias (0.01) plus a feedback term. The feedback is positive force feedback with a 15 ms delay [1], so the muscle's own force, measured 15 ms earlier, raises its stimulation.

### Evaluation

I started the hopper at rest, 1 m above the ground, with only the baseline stimulation. Nothing in the controller sets a hopping rhythm, and the feedback alone produced it. Over the first few hops the amplitude grew, and after about 3 seconds the hopper settled into a steady cycle with about 0.19 m of foot clearance in each flight phase, which stayed the same for the rest of the 10-second run.

![Hopping Animation](https://raw.githubusercontent.com/vyvas33/hopping_model/main/Videos/hopping_animation.gif)

### Why It Matters

This control approach carries over to legged robots. I used it in the stance controller of a powered knee-ankle prosthesis (see [Robotic Lower-Limb Prosthesis Control]({{ '/projects/prosthesis/' | relative_url }})), where a neuromuscular model computes the joint torques during stance.

##### References

[1] H. Geyer, A. Seyfarth, R. Blickhan. "Positive force feedback in bouncing gaits?" *Proceedings of the Royal Society B*, 270(1529):2173–2183, 2003. doi: 10.1098/rspb.2003.2454
