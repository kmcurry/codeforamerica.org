---
layout: post
status: publish
published: true
title: CfA Pitching In During Boston's "Snow-pocalypse"
author: Talin Salway
author_login: talin
author_email: talin@codeforamerica.org
wordpress_id: 3012
wordpress_url: http://c4a.me/?p=3012
date: 2011-02-17 15:48:27.000000000 +00:00
categories:
- News
- Dispatches
tags:
- boston
- Boston Snow GeoRSS JSON ruby opensource Open311 Groundcrew
wordpress_html: true
wordpress_permalink: http://www.codeforamerica.org/2011/02/17/cfa-bostons-snowpocalypse/
---

<p>A few weeks ago, Boston was experiencing a snow-pocalypse. Inches upon inches of snow had piled up, cutting off businesses and trapping citizens in their home. But early that morning, the Code for America offices received an email:</p>
<blockquote><p>“Hi CFA team – Boston is currently in the middle of a blizzard! We are exploring a possible partnership with GroundCrew, called SnowCrew, which will enable citizens-volunteers to self-organize around snow shoveling for their neighbours.”</p></blockquote>
<p>The email was from Nigel Jacobs from Boston’s Department of New Urban Mechanics — the department spearheading interesting and innovative new efforts to solve city problems — and they had found a way out of snow-pocalypse. Cellphone-using citizens would send pictures &amp; GPS locations of unshoveled sidewalks to the government, and a set of volunteers would track the posts, ready to take action, watching for reports of snowy sidewalks, and use the <a href="http://groundcrew.us/">GroundCrew program</a> to coordinate their efforts to help out.</p>
<p>There remained only one problem: they couldn’t see where to go. </p>
<p>In order to display the reports on a map, Groundcrew needed to get its data in GeoRSS format — a common mappable data format — but Boston’s reported data didn’t generate the right output. There was technical barrier between a civic problem and a citizen solution. And that’s where we came in.</p>
<p>After receiving Nigel’s note, we were able to review the situation with the data, and fortunately found that this was just a quick coding mission. In a few hours that morning, we wrote a <a href="https://github.com/YenTheFirst/open311-to-georss"></a>short script</p>