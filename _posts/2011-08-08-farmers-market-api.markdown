---
layout: post
status: publish
published: true
title: Farmers' Market API
author: John Mertens
author_login: john
author_email: john@codeforamerica.org
author_url: http://mertonium.com
wordpress_id: 7910
wordpress_url: http://codeforamerica.org/?p=7910
date: 2011-08-08 14:13:25.000000000 +00:00
categories:
- CfA Labs
tags:
- labs
wordpress_html: true
wordpress_permalink: http://www.codeforamerica.org/2011/08/08/farmers-market-api/
---

<p><a href="http://usda.iriscouch.com/farmers_markets/_design/geo/_rewrite/#4.57/39.256/-96.913"><img alt="" class="alignleft size-full wp-image-7918" src="http://codeforamerica.org/wp-content/uploads/2011/08/Farmers-Market-Map1.png" title="Farmers-Market-Map" width="610"/></a></p>
<p>I love getting my fruit and veggies from my local Farmer’ Market. Unfortunately, as a recent SF transplant I wasn’t sure how to find my local Farmers’ Market. A quick search led me to a <a href="http://search.ams.usda.gov/farmersmarkets/" target="_blank" title="USDA AMS Farmers' Market Search">USDA website which seemed to contain most of the markets in the country</a>.</p>
<p>Being an open data geek, I looked for an API. Finding none, I decided to <a href="http://usda.iriscouch.com/farmers_markets/_design/geo/_spatiallist/geojson/full?bbox=-122.61248930742187,37.655669842383595,-122.24788054277343,37.83240550745524">make one</a>. To do this, I:</p>
<ol>
<li>Used the “Export to Excel” function to download the whole dataset.</li>
<li>Cleaned it up in <a href="http://code.google.com/p/google-refine/" target="_blank" title="Learn more about Google Refine">Google Refine</a>; normalized some fields, geocoded some records, added a geojson fields.</li>
<li>Uploaded it to a <a href="http://iriscouch.com" target="_blank" title="Free CouchDB hosting ">free couchdb instance</a>.</li>
<li>Added the open source <a href="https://github.com/maxogden/geocouch-utils" target="_blank" title="Download from GitHub">geocouch-utils</a> CouchApp (which gives you a <a href="http://usda.iriscouch.com/farmers_markets/_design/geo/_rewrite/#4.57/39.256/-96.913" target="_blank" title="The Farmers' Markets Map">nice map out of the box</a>).</li>
</ol>
<p>All of this was done in about an hour and at a cost of $0.</p>
<p>So if you’re a developer who also likes fresh fruit &amp; veg, build something <a href="http://usda.iriscouch.com/farmers_markets/_design/geo/_spatiallist/geojson/full?bbox=-122.61248930742187,37.655669842383595,-122.24788054277343,37.83240550745524">on it</a>. I’ll be <a href="http://www.pcfma.com/market_home.php?market_id=13" target="_blank" title="Info on the Fillmore Farmers' Market">down on Fillmore</a>.</p>
