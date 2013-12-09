---
layout: post
status: publish
published: true
title: 'Zach''s CfA Summer: <br>"Made With [EPA] Data"'
author: Zach Williams
author_login: zach
author_email: zach@codeforamerica.org
wordpress_id: 8343
wordpress_url: http://codeforamerica.org/?p=8343
date: 2011-09-02 14:06:16.000000000 +00:00
categories:
- News
- 2011 Interns
tags: []
---
<a href="http://madewithdata.org"><img src="http://codeforamerica.org/wp-content/uploads/2011/09/epa.jpg" alt="" title="epa" width="300" class="alignright size-full wp-image-8344" /></a>When Code for America selected me as a Google Summer of Code Intern for the <a href="http://codeforamerica.org/?cfa_project=government-rubygems-pythoneggs-gsoc">Government Gems and Eggs project</a> this summer, I knew the next few months were going to be awesome. For the first time ever, I was able to meet and work with people truly committed to making government data more accessible.

Most developers don't especially enjoy working with APIs. It normally consists of reading a large amount of documentation with few examples, followed by a fair amount of troubleshooting whenever things don't work as expected. On top of that, visualizations and graphs aren't generally made overnight — a fair amount of development is spent working with data formats you might not be especially fond of (I'm looking at you XML).

But, when data and APIs become accessible, developers can make visualizations and applications that allow multiple individuals to grasp the larger picture of what's taking place around them (the immediate examples that come to mind are the <a href="http://nyc.longliveman.com/" target="_blank">NYC Graffiti Snapshot</a> or <a href="http://www.zeit.de/datenschutz/malte-spitz-data-retention" target="_blank">Zeit's visualization</a> of mobile telecom data).

This summer I ended up writing 8 different Python API wrappers — all of which are available on Code for America's Github page — along with a <a href="https://github.com/codeforamerica/Python-API-Module" target="_blank">base module other developers can use</a> going forward.

The big news from our work this summer, in my opinion, are matching <a href="https://github.com/codeforamerica/epa_ruby" target="_blank">Ruby</a> and <a href="https://github.com/codeforamerica/epa_python" target="_blank">Python</a> <wbr>wrappers for the EPA's API (an API so large and complex that no other wrappers had previously been written for it). A wealth of government data and information is now available to developers — and the <a href="https://github.com/codeforamerica/epa_python" target="_blank">documentation on the Github repositories</a> features tons of working examples.</wbr>

Throughout my last few weeks as an intern at Code for America, I worked on finishing <a href="http://madewithdata.com/" target="_blank">madewithdata.com</a> — a simple site that currently allows users to explore the radiation and water pollution information now made available through the EPA API wrappers. I actually learned quite a few things while developing the site:

<ul>
	<li>The <a href="http://en.wikipedia.org/wiki/List_of_United_States_cities_by_population" target="_blank">top 25 most-populated US cities</a> are made up of 531 ZIP Codes.</li>
	<li>2190 facilities in those ZIP Codes have permits to pollute public water sources.</li>
	<li>The ZIP Code 32218 in Jacksonville, Florida has the most polluters — 178 facilities have been granted EPA permits to pollute public water sources (some of the records date back to the 1970s).</li>
</ul>
Also, all the code I used to make the site (and find the number of polluters) is available on my <a href="https://github.com/zachwill" target="_blank">personal Github page</a>.
