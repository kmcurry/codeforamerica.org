---
layout: post
status: publish
published: true
title: 'Explore City Art 3 Ways: On Foursquare, Twitter & Mobile Sites'
author: Anna Bloom
author_login: anna
author_email: annab@codeforamerica.org
wordpress_id: 9782
wordpress_url: http://codeforamerica.org/?p=9782
date: 2011-11-22 14:01:17.000000000 +00:00
categories:
- News
tags: []
---
<a href="http://codeforamerica.org/wp-content/uploads/2011/11/art-app-team-hangout3.jpg"><img class="alignleft size-large wp-image-9803" title="art-app-team-hangout3" src="http://codeforamerica.org/wp-content/uploads/2011/11/art-app-team-hangout3-1024x246.jpg" alt="" width="600" height="113" /></a>

&nbsp;

&nbsp;

&nbsp;

Above, see the team Google+ Hangout photo shoot.

The two hip dudes holding the heart? That's Michael Ellsworth and Corey Gutch, the dynamic design team duo from the Seattle creative agency <a href="http://www.dumbeyes.com/">Dumb Eyes</a> who also help to run Seattle's <a href="http://seattleartwalks.org/">monthly art walks</a>.

The refined, bearded gentleman? That's Matt Blair, the culture-loving smartphone developer from Portland who created <a href="http://publicartpdx.com/">Portland's first public art app</a> that launched last April.

The two with the toothy grins? That's me and John Mertens at Code for America's offices in San Francisco.

Together over the course of the last six months, our team collaborated with developers, designers, residents, and city staff from Portland, Seattle, San Francisco, Philadelphia, and Boston, and county staff from King County, Washington, to help make public and street art more discoverable in cities. Today we are proud to announce three new ways to explore art in these five cities. Including:

<strong>1. Foursquare.</strong>
In four cities -- Boston, Philadelphia, Seattle, and San Francisco -- you are now able to check in, comment, and explore nearly 3,000 pieces of public art.

<strong>2. Twitter.</strong>
Anywhere you go, if you find street art or public art, you can Tweet a geo-located image at @publicartapp and help map it. The results appear at <a href="http://artmapper.org">artmapper.org.</a>

This app, developed by John with help from civic hacker Mark Headd, is currently a part of an art exhibit, "Here Be Dragons: Mapping Information and Imagination," at the <a href="http://www.theintersection.org/calendar/index.php?op=view&amp;id=4280">Intersection for the Arts in San Francisco</a>, and won honorable mention for the first annual <a href="http://www.summerofsmart.org/about/">Summer of Smart hackathon</a>. The technology was also used in <a href="http://www.summerofsmart.org/projects/public-art-spaces-2/">Public Art Spaces</a>, an award-winning app from the same competition that enables the public to tag spaces in cities where they would like to see public art.

<strong>3. One smartphone app, and five city-specific mobile websites help you to find public art near you:
</strong><em>(Design by the Dumb Eyes team; meant for display on smartphones.)</em>

In Boston, <a href="http://bos.publicartapp.mobi">http://bos.publicartapp.mobi</a>
In Seattle, <a href="http://sea.publicartapp.mobi">http://sea.publicartapp.mobi</a>
In San Francisco, <a href="http://sf.publicartapp.mobi">http://sf.publicartapp.mobi</a>
In Philadelphia, <a href="http://phl.publicartapp.mobi">http://phl.publicartapp.mobi</a>
In Portland, go to <a href="http://publicartpdx.com/">Public Art PDX</a> to download an app for iPod, iPad or iTouch.

In all of these cities, we also published the location data and other details for public art in a machine-readable format for anyone to use. We look forward to seeing other inspired developers mix and mash this data up and create new apps that help people interact and explore the history and culture that capture the spirit of these cities.

Special thanks to the following people and organizations that supported this project and helped make it possible:

<strong>City Staff</strong>
Kate Patterson, public relations manager, San Francisco Arts Commission
Allison Cummings, senior registrar, San Francisco Arts Commission
Jeffrey Pierce, web and technology coordinator, Seattle Office of Arts &amp; Cultural Affairs
Lori Patrick, public relations manager, Seattle Office of Arts &amp; Cultural Affairs
Tina Hoggatt, coordinator of outreach and and education for King County's Public Art 4Culture
Moira Baylson, cultural officer, Philadelphia Office of Arts Culture &amp; the Creative Economy
Margot Berg, public art director, Philadelphia Office of Arts Culture &amp; the Creative Economy
Steve Weinik, administrative and IT services manager, City of Philadelphia Mural Arts Program
Karen Goodfellow, staff director, Boston Art Commission

<strong>Advisory Board
</strong>George Oates, Project Lead and Designer for The Internet Archive's Open Library and cofounder of Flickr
Jay Nath, Director of Innovation for the City of San Francisco
Josette Melchor, Executive Director of the Gray Area Foundation for the Arts
Nathaniel Vaughn Kelso, Design Technologist at Stamen Design
Richard Koci Hernandez, Emmy-Award-winning multimedia producer; UC Berkeley Graduate School Professor
Dan O’Neil, Executive Director at Smart Chicago Collaborative; cofounder of EveryBlock
Michael Evans, 2011 Code for America Fellow now a technologist at Stamen Design

<strong>Additional Support</strong>
Aaron Ogle, Code for America fellow
Max Ogden, Code for America fellow
Karen Johnson, Seattle journalist, and lover of cities

<strong>Tech links</strong>

<strong></strong>All of the code developed for the project is open source and can be found on GitHub:
<ul>
	<li><a href="https://github.com/mertonium/public_art_finder/blob/master/foursquare_uploader/uploader.rb" target="_blank">Source code for the Foursquare uploader</a></li>
	<li><a href="https://github.com/mertonium/muralmapper" target="_blank">Source code for Artmapper.org</a></li>
	<li><a href="https://github.com/mertonium/public_art_finder/tree/master/viewer_couchapp" target="_blank">Source code for the mobile app</a></li>
</ul>
The data powering each site can be accessed via the following REST APIs:
(returned as GeoJSON unless noted)
<ul>
	<li><a href="http://sf.publicartapp.mobi/all" target="_blank">http://sf.publicartapp.mobi/all</a> - every record (use sparingly - we're on a free host)</li>
	<li><a href="http://sf.publicartapp.mobi/data?bbox=-122.4148,37.7731,-122.3848,37.8031" target="_blank">http://sf.publicartapp.mobi/data?bbox=-122.4148,37.7731,-122.3848,37.8031</a> - every record within the given bounding box (central San Francisco in this case)</li>
	<li><a href="http://sf.publicartapp.mobi/kml" target="_blank">http://sf.publicartapp.mobi/kml</a> - every record downloaded as a KML file</li>
	<li><a href="http://sf.publicartapp.mobi/api" target="_blank">http://sf.publicartapp.mobi/api</a> - access to the standard CouchDB API</li>
</ul>
<div><span style="font-size: small;"><span class="Apple-style-span" style="line-height: 24px;">Just swap out "sf" in the above urls to switch data sets.</span></span></div>
