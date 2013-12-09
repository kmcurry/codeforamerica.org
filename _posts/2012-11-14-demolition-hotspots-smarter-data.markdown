---
layout: post
status: publish
published: true
title: Demolition hotspots and smarter data
author: Nick Doiron
author_login: nickd
author_email: nickd@codeforamerica.org
wordpress_id: 18517
wordpress_url: http://codeforamerica.org/?p=18517
date: 2012-11-14 18:31:10.000000000 +00:00
categories:
- News
- 2012 fellows
- Macon
- Open Data
- San Francisco
tags: []
---
One thing that stands out about San Francisco is its neighborhoods. Months after moving to the city, I still hear of new neighborhoods and their specialties. There are some projects for digital maps that make sense of fuzzy neighborhood boundaries - maps using <a href="http://hood.theory.org/">online consensus</a> or <a href="http://www.crowdsourcing.org/document/exploring-place-through-user-generated-content-using-flickr-tags-to-describe-city-cores/6396/36">Flickr geotags</a>. For the most part, though, our datasets are oblivious to the streets intertwining below them.

I tried feeding one of these datasets into <a href="http://neo4j.org/learn/">Neo4j</a>, a NoSQL network database, to search for food deserts and demolition hotspots in my partner city: Macon, Ga. It's hard to pick a high-risk neighborhood out of a spreadsheet or a list of coordinates.

Once you broaden the scope of the data to include connecting streets, the immediate neighborhood adds context, hints at whether a street connects to a major artery or a maze of back roads, reveals whether a condemned house is around the corner or across a highway.

The project showed that among houses cited by the City, neighborhoods of demolished houses stood out. Where most cited houses had 0-5 demolished houses in their network, networks of demolished houses peak at around 10-12 demolitions.

<img src="http://demodexter.herokuapp.com/images/DemosInDemoNetworks.png" alt="" width="300" />

<strong>What else might we see in data tied to streets instead of spreadsheets?</strong>

I'm launching an experimental site and API for San Francisco called <a href="http://demodexter.herokuapp.com">DemoDexter</a>. At its core are 2,800 streets from <a href="http://openstreetmap.org">OpenStreetMap</a>. Each street is open for you to add your own data and get analysis back.

<em>Two examples:</em>

I added a "BART" tag to every street with a BART station. An API endpoint (/access/bart) helps map streets by how many links away they are from a station:

&nbsp;

<img class="aligncenter size-full wp-image-18776" title="SF BART Access" src="http://codeforamerica.org/wp-content/uploads/2012/11/Screen-Shot-2012-11-13-at-9.49.36-AM.png" alt="SF BART Access Map" width="577" height="526" />

<a href="http://tiles.mapbox.com/mapmeld/map/sfbart">Link to interactive map</a>

Jessica, another Code for America fellow, told me that urban planners are concerned about choice. People are happiest when they have access to multiple supermarkets and parks, not just one nearby. Here's a different map from the API, with streets color-coded by access to the two closest Chipotles (/choice/chipotle). Streets off of <a href="https://maps.google.com/maps?q=market+street+sf&amp;ll=37.781027,-122.411385&amp;spn=0.173391,0.339546&amp;fb=1&amp;gl=us&amp;hq=market+street&amp;hnear=San+Francisco,+California&amp;t=m&amp;fll=37.781027,-122.411385&amp;fspn=0.173391,0.339546&amp;z=12" target="_blank">Market Street</a> have bright color-coding, while those near the <a href="http://en.wikipedia.org/wiki/Sunset_District,_San_Francisco" target="_blank">Sunset's</a> one Chipotle are more subdued.

&nbsp;

<img class="aligncenter size-full wp-image-18777" title="SF Chipotle Choice" src="http://codeforamerica.org/wp-content/uploads/2012/11/Screen-Shot-2012-11-13-at-9.52.36-AM.png" alt="SF Chipotle Choice Map" width="613" height="502" />

<a href="http://tiles.mapbox.com/mapmeld/map/BARTChoice">Link to interactive map</a>

<a href="http://demodexter.herokuapp.com">DemoDexter</a> is open if you'd like to add tags showing how neighborhoods are served by <a href="http://tiles.mapbox.com/mapmeld/map/LibraryAccess">local libraries</a>, farmers' markets, or hackerspaces. If you have the right datasets, you could search for hotspots of business development or blight. For other cities, such as <a href="http://oaklandexter.herokuapp.com">Oakland</a>, take the code <a href="https://github.com/codeforamerica/DemoDexter">from GitHub</a> and the underlying street map from Michal Migurski's <a href="http://metro.teczno.com/">OpenStreetMap metro extracts</a>.

&nbsp;

Questions? Comments? Hit us up <a href="http://twitter.com/codeforamerica" target="_blank">@codeforamerica</a>.
