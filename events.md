---
layout: default
title: Events
description: Upcoming and past Roman Rally meetings. Each meeting has its own page.
permalink: /events/
---

<header class="page-header">
  <p class="kicker">Calendar</p>
  <h1>Events</h1>
  <p class="lede">One page per meeting. Upcoming Rallies are announced here when a host and a season are real enough to say out loud. Past Rallies stay here afterward, with a short note on the work.</p>
</header>

<section aria-labelledby="upcoming-heading">
  <h2 id="upcoming-heading">Upcoming</h2>
  <div class="card-list">
  {% assign upcoming = site.events | where: "status", "upcoming" | sort: "sort_date" %}
  {% if upcoming.size == 0 %}
    <div class="empty">
      <p>The next Rally is <strong class="tbd">TBD</strong>.</p>
    </div>
  {% else %}
    {% for event in upcoming %}
      {% include event_card.html event=event %}
    {% endfor %}
  {% endif %}
  </div>
</section>

<section aria-labelledby="past-heading">
  <h2 id="past-heading">Past events</h2>
  {% assign past = site.events | where: "status", "past" | sort: "sort_date" | reverse %}
  {% if past.size == 0 %}
  <div class="empty">
    <p>No Roman Rally has been held yet. This block is the placeholder for meetings that have already happened. Dates, hosts, and notes will collect here after the first gathering. To file one, set <code>status: past</code> on its file in <code>_events/</code> and add a few sentences about the projects people actually did.</p>
  </div>
  {% else %}
  <div class="card-list">
    {% for event in past %}
      {% include event_card.html event=event %}
    {% endfor %}
  </div>
  {% endif %}
</section>

<section class="prose">
  <h2>Adding a meeting</h2>
  <p>Copy <code>_events/TEMPLATE.md</code> to a new file in <code>_events/</code>, remove the line <code>published: false</code>, and replace each <strong class="tbd">TBD</strong>. Set <code>status</code> to <code>upcoming</code> or <code>past</code>. The lists on this page, and the card on the home page, update when the site is rebuilt. The <a href="https://github.com/Roman-Science-Collaboration/roman-rally/blob/main/README.md">README</a> has the click-by-click version for the GitHub website.</p>
</section>
