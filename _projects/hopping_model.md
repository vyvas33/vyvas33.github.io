---
layout: page
title: Hopping Model
description: "A hopping model with one muscle "
importance: 2
category: work
github: vyvas33/hopping_model
---

This work employs a two-segment hopping model with a single extensor muscle to simulate vertical hopping. Hopping (and running) is characterized by alternating stance and flight phases. During stance, the leg is in contact with the ground and the muscles provide the force to propel the body off the ground. During the flight phase, the body moves under the influence of gravity. We represent the body as a point mass and the leg as a two-segment system, which are mass-less. 

The muscle tendon complex (MTC) is modeled using the Hill Type Muscle Model. The MTC is composed of a contractile element (CE), a parallel passive element (PE) and a series elastic element (SEE). The activation of the muscle is controlled by a neural input $$STIM(t)$$. The input consists of a constant stimulation bias and a feedback component. In this work, we use the positive force feedback with delay (Geyer et al., 2003).

![Hopping Animation](https://raw.githubusercontent.com/vyvas33/hopping_model/main/Videos/hopping_animation.gif)

### References 
Geyer H, Seyfarth A, Blickhan R. Positive force feedback in bouncing gaits? Proc Biol Sci. 2003 Oct 22;270(1529):2173-83. doi: 10.1098/rspb.2003.2454. PMID: 14561282; PMCID: PMC1691493.
