---
layout: post
status: publish
published: true
title: See Click Mural
author: John Mertens
author_login: john
author_email: john@codeforamerica.org
author_url: http://mertonium.com
wordpress_id: 9488
wordpress_url: http://codeforamerica.org/?p=9488
date: 2011-10-21 12:24:30.000000000 +00:00
categories:
- CfA Labs
- Philadelphia
tags: []
---
<a href="http://codeforamerica.org/wp-content/uploads/2011/10/seeclickmural.png"><img class="alignleft size-full wp-image-9492" title="seeclickmural" src="http://codeforamerica.org/wp-content/uploads/2011/10/seeclickmural.png" alt="" width="600" /></a>Moments after giving a talk on open data and code reuse at the Code for America Summit, Ben Berkowitz (SeeClickFix) and Aaron Ogle (CfA) grabbed me and said, "can we make a simple map mashup of all the murals verses graffiti reports in Philly?"

Of course we can. And, of course, we can do it with free and open source resources.

I give you <a title="SeeClickMural" href="http://seeclickmural.herokuapp.com/" target="_blank">SeeClickMural</a>.  I'm not exactly sure what correlations come up, but it is an interesting exercise in quickly combining multiple feeds of open data.

Here's how we did it:
<ul>
	<li>The graffiti reports came from this <a href="http://seeclickfix.com/philadelphia/issues?end_date=Any&amp;format=json&amp;num_results=500&amp;page=1&amp;search=graffiti&amp;sort=issues.created_at&amp;start_date=Any&amp;status%5BAcknowledged%5D=true&amp;status%5BArchived%5D=true&amp;status%5BClosed%5D=true&amp;status%5BOpen%5D=true&amp;at=philadelphia+pa" target="_blank">SeeClickFix feed</a>.</li>
	<li>The mural data came from MuralFarm.org (via <a href="http://x.iriscouch.com/murals/_design/geo/_spatiallist/geojson/full?bbox=-180,-90,180,90" target="_blank">this geocouch instance</a>).</li>
	<li>The actual map uses <a title="Polymaps homepage" href="http://polymaps.org/" target="_blank">Polymaps</a> (from <a title="SimpleGeo" href="http://simplegeo.com/" target="_blank">SimpleGeo</a> &amp; <a title="Stamen" href="http://stamen.com/" target="_blank">Stamen</a>).</li>
	<li>The backend and frontend framework came from <a href="https://github.com/zachwill/flask_heroku" target="_blank">zachwill's flask_heroku</a>.  It is a dead-simple way to setup a static web server with the best of HTML5 boilerplate and bootstrap CSS already baked in - and all of it is ready for deployment to Heroku. (btw Zach is a 2012 CfA fellow.)</li>
</ul>

[cc-mkplc app="SeeClickFix"]
