---
layout: post
status: publish
published: true
title: Open311 at Code for America
author: Michael Lawrence Evans
author_login: michael
author_email: michael@codeforamerica.org
author_url: http://www.longliveman.com
wordpress_id: 8552
wordpress_url: http://codeforamerica.org/?p=8552
date: 2011-09-20 14:51:36.000000000 +00:00
categories:
- News
tags: []
---
We're deeply committed to <a href="http://www.open311.org">Open311</a> -- an interoperable standard that allows developers to seamlessly interact with 311 systems across the nation. 311 is an increasingly popular communication system for cities to enable citizen issue reporting. Open311 is an attempt to standardize the protocol so 311 apps built anywhere can be used everywhere. Thanks to <a href="http://code.google.com/soc/">Google Summer of Code</a>, we were able to bring some great additional talent onto our Open311 projects, and we think the results are exciting. Here's a summary of what we've done so far and where we're looking to go:
<h3>Open311 Dashboard</h3>
Late in 2010, our CTO, Dan Melton, had the idea for an <a href="http://codeforamerica.org/?cfa_project=open311-dashboard">Open311 Dashboard</a>. We want to help cities visualize and analyze 311 data on a clean, interactive dashboard. Early this year, I took it on as a 20% project, and soon thereafter I started to focus on it as project lead. This summer, Chris Barna and Bailey Smith joined my team to help design and build the back-end with Django and an advanced geospatial database. We're especially interested in trend analysis by block and by neighborhood. Over the next month, my team will be putting the finishing touches on the first release of the dashboard. More details and screenshots of the project can be found in <a href="http://codeforamerica.org/2011/08/31/chriss-cfa-summer-preview-the-open311-dashboard">Chris's update</a>.
<h3>Open311 Center on Joget</h3>
Michael Yap, the CEO of <a href="http://www.joget.org">Joget</a>, and I worked with Ashish Mittal in creating a prototype of an <a href="http://codeforamerica.org/2011/09/09/ashishs-cfa-summer-starting-the-open311-center/">Open311 Center</a>; it's a lightweight 311 back-end using Joget's open source workflow management system. Michael Yap and I are now planning to add a set of simple analytical tools for small cities to analyze request trends in real-time. More details on the Open311 Center can be found in <a href="http://codeforamerica.org/2011/09/09/ashishs-cfa-summer-starting-the-open311-center/">Ashish's update</a>.
<h3>Open311 Developer Libraries</h3>
Two of our Google Summer of Coders, Zach Williams and Ronaldo Barbachano, built <a href="https://github.com/codeforamerica/open311_python">Python</a> and <a href="https://github.com/codeforamerica/open311_php">PHP</a> libraries for Open311. The libraries make it easier for developers to use the API. The libraries also build on the success of Code for America's <a href="http://rubygems.org/gems/open311">Ruby library for Open311</a>, built by Dan Melton and Erik Michaels-Ober. The PHP library is currently being used to create an updated Open311 Facebook application and an <a href="https://github.com/tskochanski/Open311-Plugin-for-Ushahidi">Open311 plugin for Ushahidi</a>.
<h3>Open311 Facebook App</h3>
Stanford Rosenthal updated San Francisco's 311 Facebook app. Henry Jiang, who built the initial Facebook app for the City of San Francisco, worked closely with Stanford on the updated application. It now works with the latest version of the API. Also, with Dave Mitchell's help, the Facebook application has been extended to work in Boston.

San Francisco implemented the application and a demo can be found here: <a href="http://apps.facebook.com/sf_requests">http://apps.facebook.com/sf_requests</a>

We see great potential for the development of Open311 from the entire community, and we're excited to continue working on it this year and into the future.
