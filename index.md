---

## layout: default

title: Roman Rally
description: Hackathon focused on commissioning and first-look data from NASA's Nancy Grace Roman Space Telescope, organized by the Roman Science Collaboration.

![Illustration of two rally cars: a purple Roman Space Telescope car labeled Wide Field Racing and a teal Euclid car, racing across a dusty lunar surface]({{ '/assets/images/roman-rally-banner.png' | relative_url }})

Illustration by Robyn

Roman Science Collaboration

# Roman Rally

A week-long hackathon on commissioning and first-look data from NASA's Nancy Grace Roman Space Telescope.

[2026 Roman Rally]({{ '/events/rally2026/' | relative_url }}) [Host a Rally Room]({{ '/handbook/#what-it-means-to-host-a-rally-room' | relative_url }})

## At a glance

When

Dec 14-18, 2026

Where

Online, and in-person Rally Rooms. Full list is on the [2026 Rally]({{ '/events/rally2026/' | relative_url }}) page.

Who

Anyone who wants to experiment on the new data.

Join

[Participant sign-up form](https://docs.google.com/forms/d/1KZgV9BmCQiFieGkorWnvCNWMoyuz-FSELj9YmTKGAtw/viewform) opens Monday, Nov 2, 2026. Details are on the [2026 Rally]({{ '/events/rally2026/' | relative_url }}) page.

Host

[Host form](https://docs.google.com/forms/d/1ovYDq2ZmVzcV_1i-PXOV6LtKhW3Cnx8XK-7muMQbAiA/viewform), responses ideally due Oct 30. [What it means to host a Rally Room]({{ '/handbook/#what-it-means-to-host-a-rally-room' | relative_url }}).

{% assign upcoming = site.events | where: "status", "upcoming" | sort: "sort_date" %} {% if upcoming.size == 0 %}

The next Rally is **Dec 14-18, 2026**, online and at in-person Rally Rooms.  [Host your own](https://docs.google.com/forms/d/1ovYDq2ZmVzcV_1i-PXOV6LtKhW3Cnx8XK-7muMQbAiA/viewform).

 {% else %} {% for event in upcoming %} {% include event_card.html event=event %} {% endfor %} {% endif %}

## How the week works

- Participants propose the projects. Groups form around those ideas, work, and report out. The plan can change by lunch.
- Ideas, code, and rough results stay visible to the room and on Slack. Substantial help is repaid with co-authorship. Leave at home anything you cannot share.

The useful part is often the conversation you did not put on the schedule.

## Why now

Roman launched on 30 August 2026, and commissioning is underway. Commissioning and first public data products will be released prior to Dec 11. From early December the data moves fast, and there is a lot to learn: format, quality, scale, calibrations, new image and catalog formats, and dos and don'ts on the Roman Research Nexus.

**We strongly encourage Roman Rally participants to join the [Roman Science Collaboration](https://outerspace.stsci.edu/spaces/RSCPUB/pages/286851875/Roman+Science+Collaboration+RSC+Public+Page+Home) (RSC).** The RSC exists to help make the most of Roman data. Membership is voluntary, and you do not have to join the RSC to do science with Roman data.

## Share the invitation

Forward it, or post it where your community will see it. Two QR codes:

- **Scan to join the Rally** opens [https://roman-science-collaboration.github.io/roman-rally/](https://roman-science-collaboration.github.io/roman-rally/).
- **Seeking Rally Hosts** opens [https://roman-science-collaboration.github.io/roman-rally/handbook/#what-it-means-to-host-a-rally-room](https://roman-science-collaboration.github.io/roman-rally/handbook/#what-it-means-to-host-a-rally-room).

![Invitation to the Roman Rally, December 14-18, 2026, online and at in-person Rally Rooms at participating institutions. A few days of hands-on work on early Nancy Grace Roman Space Telescope commissioning and first-look data, organized by the Roman Science Collaboration. One QR code, Scan to join the Rally, links to https://roman-science-collaboration.github.io/roman-rally/ and a second, Seeking Rally Hosts, links to https://roman-science-collaboration.github.io/roman-rally/handbook/#what-it-means-to-host-a-rally-room.]({{ '/assets/images/roman-rally-invitation.jpg' | relative_url }})

[Download the invitation (JPG)]({{ '/assets/images/roman-rally-invitation.jpg' | relative_url }})

## Past events

None yet.
