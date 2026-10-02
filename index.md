---
layout: default
title: Roman Rally
description: Working meetings on commissioning and first-look data from NASA's Nancy Grace Roman Space Telescope, organized by the Roman Science Collaboration.
---

<header class="hero">
  <p class="kicker">Roman Science Collaboration</p>
  <h1>Roman Rally</h1>
  <p class="lede">Short, in-person working meetings on data from NASA's Nancy Grace Roman Space Telescope, during commissioning and the mission's first look at the sky.</p>
  <p>A rally is a quick gathering. You show up, you do the work that is actually in front of you, and you head out again along your own road. The older meaning of the word is a road itself. Roman roads were built so a person or a message could meet another one halfway, without every town inventing the route. Roman Rally borrows both senses: a few shared days, organized by the Roman Science Collaboration, for people who want to sit with Roman data while those measurements are still new.</p>
  <p class="hero-actions">
    <a class="button" href="{{ '/events/first-rally/' | relative_url }}">The first Rally</a>
    <a class="button button-ghost" href="{{ '/about/' | relative_url }}">How a Rally works</a>
  </p>
</header>

<ul class="principles">
  <li>
    <h2>A few days, one room</h2>
    <p>Each Rally is a hackathon-style meeting, small enough that you can hear the next table. The useful part is often the conversation you did not put on the schedule.</p>
  </li>
  <li>
    <h2>Projects from the floor</h2>
    <p>Participants propose the work. Groups form around those ideas, and the plan is allowed to change by lunch.</p>
  </li>
  <li>
    <h2>Open notes, shared credit</h2>
    <p>Ideas, code, and rough results stay visible to the room. Substantial help is repaid with co-authorship. Leave at home anything you cannot share.</p>
  </li>
</ul>

<section class="prose" aria-labelledby="next-heading">
  <h2 id="next-heading">The next Rally</h2>
  <p>The first meeting does not have a date yet, and applications are not open. Every unset detail on the event page is marked <strong class="tbd">TBD</strong>, so you can see what the organizers still have to decide.</p>
</section>

<div class="card-list">
{% assign upcoming = site.events | where: "status", "upcoming" | sort: "sort_date" %}
{% if upcoming.size == 0 %}
  <div class="empty">
    <p>The next Rally is <strong class="tbd">TBD</strong>. When a meeting is ready to announce, add a file in <code>_events/</code> with <code>status: upcoming</code>.</p>
  </div>
{% else %}
  {% for event in upcoming %}
    {% include event_card.html event=event %}
  {% endfor %}
{% endif %}
</div>

<section class="prose">
  <h2>Why these meetings, and why now</h2>
  <p>Roman's surveys are wide, and a lot of fields will read the same images. The conversations that shape the early papers often happen before anyone has a polished result: a calibration that still looks strange, a catalog new enough that nobody has a habit for it, a person across the room who has already tried the thing you were about to start. A Rally is a few days set aside for that work.</p>
  <p>Roman launched on 30 August 2026. NASA has said it expects to release the first images by early 2027. Commissioning and that first public look are the natural season for this series. Later meetings can follow later data. Each event page will say which products are in scope. The mission decides what may be used, and a Rally does not grant data rights.</p>
  <p>The Roman Science Collaboration exists to help these kinds of projects find each other. Membership is voluntary, and you do not have to join the RSC to do science with Roman data. How to apply to a Rally is a separate question, answered on the <a href="{{ '/participation/' | relative_url }}">participation page</a> and on each event page. The collaboration's public home is on <a href="https://outerspace.stsci.edu/spaces/RSCPUB/pages/286851875/Roman+Science+Collaboration+RSC+Public+Page+Home">Outerspace at STScI</a>.</p>

  <h2 id="past">Past events</h2>
  <p>No Rally has been held yet. When the first one is over, it will be listed on the <a href="{{ '/events/#past' | relative_url }}">events page</a>, with the host, the dates, and a short note on what people worked on.</p>
</section>
