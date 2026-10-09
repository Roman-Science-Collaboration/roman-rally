---
layout: default
title: Roman Rally
description: Hackathon focused on commissioning and first-look data from NASA's Nancy Grace Roman Space Telescope, organized by the Roman Science Collaboration.
---

<figure class="hero-banner">
  <picture>
    <source srcset="{{ '/assets/images/roman-rally-banner.webp' | relative_url }}" type="image/webp">
    <img src="{{ '/assets/images/roman-rally-banner.png' | relative_url }}" width="973" height="314" alt="Illustration of two rally cars: a purple Roman Space Telescope car labeled Wide Field Racing and a teal Euclid car, racing across a dusty lunar surface">
  </picture>
  <figcaption>Illustration by Robyn</figcaption>
</figure>

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
  <p>Would you like to host a rally room? Fill out this form by Nov 10. The form link is <strong class="tbd">TBD</strong>. <a href="{{ '/handbook/#what-it-means-to-host-a-rally-room' | relative_url }}">What it means to host a Rally Room</a> explains the commitment and a draft shape of the week. Notes on rooms, Zoom, and keeping a local site in step with the others are in the <a href="{{ '/handbook/' | relative_url }}">site handbook</a>.</p>
  <p class="host-pointer">In-person Rally Rooms beyond the sites already named for 2026 are still <strong class="tbd">TBD</strong>. Interested in hosting a Rally Room? See <a href="{{ '/handbook/#what-it-means-to-host-a-rally-room' | relative_url }}">what it means to host</a>.</p>
</section>

<div class="card-list">
{% assign upcoming = site.events | where: "status", "upcoming" | sort: "sort_date" %}
{% if upcoming.size == 0 %}
  <div class="empty">
    <p>The next Rally is <strong>Dec 14-18, 2026</strong>, online and at in-person Rally Rooms. Further locations are still <strong class="tbd">TBD</strong>. Interested in hosting a Rally Room? See <a href="{{ '/handbook/#what-it-means-to-host-a-rally-room' | relative_url }}">what it means to host</a>.</p>
  </div>
{% else %}
  {% for event in upcoming %}
    {% include event_card.html event=event %}
  {% endfor %}
{% endif %}
</div>

<section class="invitation-share" aria-labelledby="share-the-invitation">
  <h2 id="share-the-invitation">Share the invitation</h2>
  <p>Download the invitation and forward it, or post it where your community will see it. It carries the dates, a short description of the week, and two QR codes.</p>
  <ul class="invitation-links">
    <li><strong>Scan to join the Rally</strong> opens <a href="https://roman-science-collaboration.github.io/roman-rally/">https://roman-science-collaboration.github.io/roman-rally/</a>.</li>
    <li><a href="{{ '/handbook/#what-it-means-to-host-a-rally-room' | relative_url }}">Seeking Rally Hosts</a> opens <a href="https://roman-science-collaboration.github.io/roman-rally/handbook/#what-it-means-to-host-a-rally-room">https://roman-science-collaboration.github.io/roman-rally/handbook/#what-it-means-to-host-a-rally-room</a>. Want to host a local Rally Room? That is the page the second code opens.</li>
  </ul>
  <figure class="invitation-figure">
    <a href="{{ '/assets/images/roman-rally-invitation.jpg' | relative_url }}" download>
      <img src="{{ '/assets/images/roman-rally-invitation.jpg' | relative_url }}" width="1200" height="1500" alt="Invitation to the Roman Rally, December 14-18, 2026, online and at in-person Rally Rooms at participating institutions. A few days of hands-on work on early Nancy Grace Roman Space Telescope commissioning and first-look data, organized by the Roman Science Collaboration. One QR code, Scan to join the Rally, links to https://roman-science-collaboration.github.io/roman-rally/ and a second, Seeking Rally Hosts, links to https://roman-science-collaboration.github.io/roman-rally/handbook/#what-it-means-to-host-a-rally-room.">
    </a>
    <figcaption>
      <a class="button" href="{{ '/assets/images/roman-rally-invitation.jpg' | relative_url }}" download>Download the invitation (JPG)</a>
    </figcaption>
  </figure>
</section>

<section class="prose">
  <h2>Why these meetings, and why now</h2>
  <p>Roman's data will flow fast starting in early December. We all have a lot to learn about the data (format, quality, handling the scale, calibrations). The Roman Rally will be a place to learn and experiment on the Roman data in real-time. We imagine many lessons learned will flow from the rally: a calibration that still looks strange, dealing with new image and catalog formats, dos and don'ts on the Roman Research Nexus. The Rally is a few days set aside for that work.</p>
  
  <p>Roman launched on 30 August 2026 and commissioning is underway. Commissioning and first public look data products will be released prior to Dec 11. </p>
  <p><strong>We strongly encourage Roman Rally participants to join the <a href="https://outerspace.stsci.edu/spaces/RSCPUB/pages/286851875/Roman+Science+Collaboration+RSC+Public+Page+Home">Roman Science Collaboration</a> (RSC). </strong> 
    The RSC exists to help make the most of Roman data. Membership is voluntary, and you do not have to join the RSC 
    to do science with Roman data.</p>

  <h2 id="past">Past events</h2>
  <p>None yet.</p>
</section>
