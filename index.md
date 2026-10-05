---
layout: default
title: Roman Rally
description: Hackathon focused on commissioning and first-look data from NASA's Nancy Grace Roman Space Telescope, organized by the Roman Science Collaboration.
---

<header class="hero">
  <p class="kicker">Roman Science Collaboration</p>
  <h1>Roman Rally</h1>
  <p class="lede">Week-long hackathon focused on commissioning and first-look data from NASA's Nancy Grace Roman Space Telescope.</p>
  <p>Join us for the Roman Rally on December 14-18, 2026! It is organized by the Roman Science Collaboration, for people who want to experiment on new Roman data.</p>
  <p class="hero-actions">
    <a class="button" href="{{ '/events/rally2026/' | relative_url }}">2026 Roman Rally -- Commissioning and First Look Data</a>
  </p>
</header>

<ul class="principles">
  <li>
    <h2>A few days of cleared schedules and like minds in a shared (physical or virtual) space.</h2>
    <p>Each Rally is a hackathon-style meeting, where we brainstorm experiments and topics, work together in small teams, and wrap-up and report out at the end of the week. The useful part is often the conversation you did not put on the schedule.</p>
  </li>
  <li>
    <h2>Projects from the floor</h2>
    <p>Participants propose the work. Groups form around those ideas, and the plan is allowed to change by lunch.</p>
  </li>
  <li>
    <h2>Open notes, shared credit</h2>
    <p>Ideas, code, and rough results stay visible to the room and on Slack. Substantial help is repaid with co-authorship. Leave at home anything you cannot share.</p>
  </li>
</ul>

<section class="prose" aria-labelledby="next-heading">
  <h2 id="next-heading">The first Roman Rally</h2>
  <p>Would you like to host a rally room? Fill out this form by Nov 10. Notes on rooms, Zoom, and keeping a local site in step with the others are in the <a href="{{ '/handbook/' | relative_url }}">site handbook</a>.</p>
</section>

<div class="card-list">
{% assign upcoming = site.events | where: "status", "upcoming" | sort: "sort_date" %}
{% if upcoming.size == 0 %}
  <div class="empty">
    <p>The next Rally is <strong>Dec 14-18, 2026</strong> both online and at several physical locations. In-person Rally locations are still TBD.</p>
  </div>
{% else %}
  {% for event in upcoming %}
    {% include event_card.html event=event %}
  {% endfor %}
{% endif %}
</div>

<section class="prose">
  <h2>Why these meetings, and why now</h2>
  <p>Roman's data will flow fast starting in early December. We all have a lot to learn about the data (format, quality, handling the scale, calibrations). The Roman Rally will be a place to learn and experiment on the Roman data in real-time. We imagine many lessons learned will flow from the rally: a calibration that still looks strange, dealing with new image and catalog formats, dos and don'ts on the Roman Research Nexus. The Rally is a few days set aside for that work.</p>
  
  <p>Roman launched on 30 August 2026 and commissioning is underway. Commissioning and first public look data products will be released prior to Dec 11. </p>
  <p><strong>We strongly encourage Roman Rally participants to join the Roman Science Collaboration (RSC). The RSC exists to help make the most of Roman data. Membership is voluntary, and you do not have to join the RSC to do science with Roman data. The collaboration's public home is on <a href="https://outerspace.stsci.edu/spaces/RSCPUB/pages/286851875/Roman+Science+Collaboration+RSC+Public+Page+Home">Outerspace at STScI</a>.</p>

  <h2 id="past">Past events</h2>
  <p>None yet.</p>
</section>
