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
---
Philly Tech Week kicked off this week with the unveiling of the <a href="http://OpenDataPhilly.org">OpenDataPhilly.org</a> data catalog.  CfA's contribution to the catalog comes in the form of <a title="PHL API" href="http://phlapi.com" target="_blank">PHL API</a> - a RESTful API of Philadelphia-related geospatial data. This data can be used for a variety of purposes, like figuring out where your closest library is, or <a title="Sanitation district example." href="http://phlapi.com:5984/examples" target="_blank">what sanitation district you live in</a>.  The base data for PHL API has come from the <a title="PASDA website" href="http://www.pasda.psu.edu/uci/SearchResults.aspx?Keyword=philadelphia&amp;Go=Go&amp;searchType=keyword&amp;condition=AND&amp;sessionID=5798483202011425212330" target="_blank">Pennsylvania Spatial Data Access</a> website.

Why is this awesome?  Because it takes data in a proprietary format (shapefile) and makes it accessible via an API in multiple formats (kml &amp; geojson), thereby lowering the barrier to entry for working with geospatial data.

The first iteration of this project came out of our Philly Data Camp at the end of February under the name of PhillyAPI.  Since then, we've embraced and contributed to the <a title="Civic API on GitHub" href="https://github.com/maxogden/civicapi" target="_blank">CivicAPI</a> framework and extended some of the base functionality.

[caption id="attachment_5387" align="alignnone" width="610" caption="Bike Routes and Public Schools in Philadelphia"]<a href="http://codeforamerica.org/wp-content/uploads/2011/04/Screen-shot-2011-04-25-at-5.33.57-PM.png"><img class="size-large wp-image-5387" title="PHLAPI_screenshot" src="http://codeforamerica.org/wp-content/uploads/2011/04/Screen-shot-2011-04-25-at-5.33.57-PM-1024x581.png" alt="PHL API Map" width="610" height="363" /></a>[/caption]

Love bombs need to be dropped on CfA fellow (and my cube-mate), Max Ogden, and <a title="Mark on teh twitterz" href="http://twitter.com/#!/mheadd">Mark Headd</a> for their help and guidance.  Max has <a title="How to make URTOWN API" href="http://maxogden.com/#/blog/diy-public-data-api" target="_blank">written a great walkthrough</a> on the technical process to inspire other civic-minded developers to liberate the data in their area.  He has also gotten me addicted to CouchDB...
