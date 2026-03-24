---
layout: page
title: projects
permalink: /projects/
description:  
nav: true
nav_order: 3
---

<!-- pages/projects.md -->
<div class="projects">

{% assign sorted_projects = site.projects | sort: "importance" %}
<ul style="list-style-type: none; padding-left: 0; margin-top: 1rem;">
{% for project in sorted_projects %}
  <li style="margin-bottom: 2rem;">
    <h3 style="margin-bottom: 0.2rem;">
      <a href="{{ project.url | relative_url }}">{{ project.title }}</a>
      {% if project.github %}
      <a href="https://github.com/{{ project.github }}" target="_blank" title="View repository" style="font-size: 1.1rem; margin-left: 0.5rem; color: var(--global-theme-color);">
        <i class="fa-brands fa-github"></i>
      </a>
      {% endif %}
    </h3>
    <p style="margin-top: 0; color: var(--global-text-color-light);">{{ project.description }}</p>
  </li>
{% endfor %}
</ul>

</div>

<h2 class="publication-heading">publications</h2>
<div class="publications">
{% bibliography %}
</div>
