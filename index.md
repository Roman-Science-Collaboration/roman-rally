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
  <p class="lede">A week-long hackathon on commissioning and first-look data from NASA's Nancy Grace Roman Space Telescope.</p>
  <p class="hero-actions">
    <a class="button" href="{{ '/events/rally2026/' | relative_url }}">2026 Roman Rally</a>
    <a class="button button-ghost" href="{{ '/handbook/#what-it-means-to-host-a-rally-room' | relative_url }}">Host a Rally Room</a>
  </p>
</header>

<section class="facts home-facts" aria-label="Key facts">
  <h2 class="facts-title">At a glance</h2>
  <dl>
    <div>
      <dt>When</dt>
      <dd>Dec 14-18, 2026</dd>
    </div>
    <div>
      <dt>Where</dt>
      <dd>Online, and in-person Rally Rooms. Further sites are <strong class="tbd">TBD</strong>.</dd>
    </div>
    <div>
      <dt>Who</dt>
      <dd>Anyone who wants to experiment on the new data.</dd>
    </div>
    <div>
      <dt>Join</dt>
      <dd>Applications are not open. The form is <strong class="tbd">TBD</strong> on the <a href="{{ '/events/rally2026/' | relative_url }}">2026 Rally</a> page.</dd>
    </div>
    <div>
      <dt>Host</dt>
      <dd>Form by Nov 10. The link is <strong class="tbd">TBD</strong>. <a href="{{ '/handbook/#what-it-means-to-host-a-rally-room' | relative_url }}">What it means to host a Rally Room</a>.</dd>
    </div>
  </dl>
</section>

<div class="card-list">
{% assign upcoming = site.events | where: "status", "upcoming" | sort: "sort_date" %}
{% if upcoming.size == 0 %}
  <div class="empty">
    <p>The next Rally is <strong>Dec 14-18, 2026</strong>, online and at in-person Rally Rooms. Further locations are <strong class="tbd">TBD</strong>.</p>
  </div>
{% else %}
  {% for event in upcoming %}
    {% include event_card.html event=event %}
  {% endfor %}
{% endif %}
</div>

<section class="prose">
  <h2>How the week works</h2>
  <ul>
    <li>Participants propose the projects. Groups form around those ideas, work, and report out. The plan can change by lunch.</li>
    <li>Ideas, code, and rough results stay visible to the room and on Slack. Substantial help is repaid with co-authorship. Leave at home anything you cannot share.</li>
  </ul>
  <p>The useful part is often the conversation you did not put on the schedule.</p>

  <h2>Why now</h2>
  <p>Roman launched on 30 August 2026, and commissioning is underway. Commissioning and first public data products will be released prior to Dec 11. From early December the data moves fast, and there is a lot to learn: format, quality, scale, calibrations, new image and catalog formats, and dos and don'ts on the Roman Research Nexus.</p>
  <p><strong>We strongly encourage Roman Rally participants to join the <a href="https://outerspace.stsci.edu/spaces/RSCPUB/pages/286851875/Roman+Science+Collaboration+RSC+Public+Page+Home">Roman Science Collaboration</a> (RSC).</strong> The RSC exists to help make the most of Roman data. Membership is voluntary, and you do not have to join the RSC to do science with Roman data.</p>
</section>

<section class="invitation-share" aria-labelledby="share-the-invitation">
  <h2 id="share-the-invitation">Share the invitation</h2>
  <p>Forward it, or post it where your community will see it. Two QR codes:</p>
  <ul class="invitation-links">
    <li><strong>Scan to join the Rally</strong> opens <a href="https://roman-science-collaboration.github.io/roman-rally/">https://roman-science-collaboration.github.io/roman-rally/</a>.</li>
    <li><strong>Seeking Rally Hosts</strong> opens <a href="https://roman-science-collaboration.github.io/roman-rally/handbook/#what-it-means-to-host-a-rally-room">https://roman-science-collaboration.github.io/roman-rally/handbook/#what-it-means-to-host-a-rally-room</a>.</li>
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
  <h2 id="past">Past events</h2>
  <p>None yet.</p>
</section>
