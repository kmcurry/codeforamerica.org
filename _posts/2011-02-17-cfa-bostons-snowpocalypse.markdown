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
---
A few weeks ago, Boston was experiencing a snow-pocalypse. Inches upon inches of snow had piled up, cutting off businesses and trapping citizens in their home. But early that morning, the Code for America offices received an email:

<blockquote>"Hi CFA team - Boston is currently in the middle of a blizzard! We are exploring a possible partnership with GroundCrew, called SnowCrew, which will enable citizens-volunteers to self-organize around snow shoveling for their neighbours."</blockquote>

The email was from Nigel Jacobs from Boston's Department of New Urban Mechanics -- the department spearheading interesting and innovative new efforts to solve city problems -- and they had found a way out of snow-pocalypse. Cellphone-using citizens would send pictures & GPS locations of unshoveled sidewalks to the government, and a set of volunteers would track the posts, ready to take action, watching for reports of snowy sidewalks, and use the <a href="http://groundcrew.us/">GroundCrew program</a> to coordinate their efforts to help out.

There remained only one problem: they couldn't see where to go. 

In order to display the reports on a map, Groundcrew needed to get its data in GeoRSS format -- a common mappable data format -- but Boston's reported data didn't generate the right output. There was technical barrier between a civic problem and a citizen solution. And that's where we came in.

After receiving Nigel's note, we were able to review the situation with the data, and fortunately found that this was just a quick coding mission. In a few hours that morning, we wrote a <a href="https://github.com/YenTheFirst/open311-to-georss" />short script</a> to translate city's reports of snow issues to mappable GeoRSS, which piped in neatly into Groundcrew's citizen mobilization platform. With a little bit of work on Groundcrew's end, the citizen volunteers were able to see where help was needed, and they could take action and get involved.

<img src="http://codeforamerica.org/wp-content/uploads/2011/01/snowcrew-311-1024x554.jpg" alt="" title="snowcrew-311" width="600" class="aligncenter size-large wp-image-3216" />

<em><a href="https://github.com/YenTheFirst/open311-to-georss/">Source code available on GitHub.</a></em>
