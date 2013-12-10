---
layout: post
status: publish
published: true
title: PHL API Arrives
author: John Mertens
author_login: john
author_email: john@codeforamerica.org
author_url: http://mertonium.com
wordpress_id: 5386
wordpress_url: http://codeforamerica.org/?p=5386
date: 2011-04-25 17:24:33.000000000 +00:00
categories:
- CfA Labs
tags:
- labs
wordpress_html: true
wordpress_permalink: http://www.codeforamerica.org/2011/04/25/phl-api-arrives/
---

<p>Philly Tech Week kicked off this week with the unveiling of the <a href="http://OpenDataPhilly.org">OpenDataPhilly.org</a> data catalog.  CfA’s contribution to the catalog comes in the form of <a href="http://phlapi.com" target="_blank" title="PHL API">PHL API</a> – a RESTful API of Philadelphia-related geospatial data. This data can be used for a variety of purposes, like figuring out where your closest library is, or <a href="http://phlapi.com:5984/examples" target="_blank" title="Sanitation district example.">what sanitation district you live in</a>.  The base data for PHL API has come from the <a href="http://www.pasda.psu.edu/uci/SearchResults.aspx?Keyword=philadelphia&amp;Go=Go&amp;searchType=keyword&amp;condition=AND&amp;sessionID=5798483202011425212330" target="_blank" title="PASDA website">Pennsylvania Spatial Data Access</a> website.</p>
<p>Why is this awesome?  Because it takes data in a proprietary format (shapefile) and makes it accessible via an API in multiple formats (kml &amp; geojson), thereby lowering the barrier to entry for working with geospatial data.</p>
<p>The first iteration of this project came out of our Philly Data Camp at the end of February under the name of PhillyAPI.  Since then, we’ve embraced and contributed to the <a href="https://github.com/maxogden/civicapi" target="_blank" title="Civic API on GitHub">CivicAPI</a> framework and extended some of the base functionality.</p>
<div class="wp-caption alignnone" id="attachment_5387" style="width: 620px"><a href="http://codeforamerica.org/wp-content/uploads/2011/04/Screen-shot-2011-04-25-at-5.33.57-PM.png"><img alt="PHL API Map" class="size-large wp-image-5387" height="363" src="http://codeforamerica.org/wp-content/uploads/2011/04/Screen-shot-2011-04-25-at-5.33.57-PM-1024x581.png" title="PHLAPI_screenshot" width="610"/></a><p class="wp-caption-text">Bike Routes and Public Schools in Philadelphia</p></div>
<p>Love bombs need to be dropped on CfA fellow (and my cube-mate), Max Ogden, and <a href="http://twitter.com/#!/mheadd" title="Mark on teh twitterz">Mark Headd</a> for their help and guidance.  Max has <a href="http://maxogden.com/#/blog/diy-public-data-api" target="_blank" title="How to make URTOWN API">written a great walkthrough</a> on the technical process to inspire other civic-minded developers to liberate the data in their area.  He has also gotten me addicted to CouchDB…</p>
