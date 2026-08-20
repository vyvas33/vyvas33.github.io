---
layout: page
title: Neuromuscular Models
description: "Hill type muscle models and reflex driven hopping"
importance: 4
category: work
github: vyvas33/hopping_model
---

![Muscle Animation](https://raw.githubusercontent.com/vyvas33/muscle_model/main/muscle_animation.gif)

### Hopping Model

In this work, I use a two-segment hopping model with a single extensor muscle to simulate vertical hopping. Hopping (and running) is characterized by alternating stance and flight phases. During stance, the leg is in contact with the ground and the muscles provide the force to propel the body off the ground. During the flight phase, the body moves under the influence of gravity. I represent the body as a point mass and the leg as a two-segment system, which are mass-less.

The muscle tendon complex (MTC) is modeled using the Hill Type Muscle Model. The model is based on the experiments conducted to understand the force-length and force-velocity relationships of the muscle. The MTC is composed of a contractile element (CE), a parallel passive element (PE) and a series elastic element (SEE). The activation of the muscle is controlled by a neural input $$STIM(t)$$. The input consists of a constant stimulation bias and a feedback component. I use the positive force feedback with delay (Geyer et al., 2003).

![Hopping Animation](https://raw.githubusercontent.com/vyvas33/hopping_model/main/Videos/hopping_animation.gif)

This control can essentially be transferred to legged robots. One implementation of such a controller is [Robotic Lower-Limb Prosthesis Control]({{ '/projects/prosthesis/' | relative_url }}), where a neuromuscular model computes the stance phase joint torques of a powered knee-ankle prosthesis.

### References

Geyer H, Seyfarth A, Blickhan R. Positive force feedback in bouncing gaits? Proc Biol Sci. 2003 Oct 22;270(1529):2173-83. doi: 10.1098/rspb.2003.2454. PMID: 14561282; PMCID: PMC1691493.
