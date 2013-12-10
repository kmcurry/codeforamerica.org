---
layout: post
status: publish
published: true
title: 'Coping with the Shutdown: Federal Data'
author: Michal Migurski
author_login: Michal Migurski
author_email: mike@codeforamerica.org
wordpress_id: 26490
wordpress_url: http://www.codeforamerica.org/?p=26490
date: 2013-10-03 00:42:14.000000000 +00:00
categories:
- News
- Data
tags: []
wordpress_html: true
wordpress_permalink: http://www.codeforamerica.org/2013/10/03/coping-with-the-shutdown-federal-data/
---

<p>The Federal Government has shut down operations. It’s not the first such event (there were <a href="http://www.washingtonpost.com/blogs/wonkblog/wp/2013/09/25/here-is-every-previous-government-shutdown-why-they-happened-and-how-they-ended/" title="Here is every previous government shutdown, why they happened and how they ended">three in 1977 alone</a>), though it does have <a href="http://www.theatlantic.com/politics/archive/2013/09/your-false-equivalence-guide-to-the-days-ahead/280062/" title="Your False-Equivalence Guide to the Days Ahead">certain unique characteristics</a>. Leaving the politics aside for the moment, what’s a civic hacker or data journalist to do <a href="http://shutdowngov.tumblr.com/" title="Shutdown.gov">when most of the government web and FTP presence is unreachable as well</a>?</p>
<p><a href="http://www.theonion.com/articles/us-on-verge-of-fullscale-government-hoedown,34057/?ref=auto"><img alt="U.S. On Verge Of Full-Scale Government Hoedown (The Onion)" class="size-medium wp-image-26494 alignleft" height="169" src="http://www.codeforamerica.org/wp-content/uploads/2013/10/government-hoedown-300x169.jpg" title="U.S. On Verge Of Full-Scale Government Hoedown (The Onion)" width="300"/></a></p>
<p>We have two responses brewing at Code for America.</p>
<p>Team 2013 Las Vegas and other fellows have been iterating on an API for the <a href="http://web.archive.org/web/20130929215439/https://www.census.gov/eos/www/naics/" title="North American Industry Classification System">North American Industry Classification System</a> (NAICS) for use in their city project. Normally available as a series of Excel spreadsheet files, Lou Huang and team have developed a simple JSON-based API for searching and accessing this useful data and made it available at <a href="http://naics.us/">NAICS.us</a>. The source code behind the service is available under <a href="https://github.com/codeforamerica/naics-api">GitHub.com/codeforamerica</a>. We’d been adding documentation and search capabilities when the government shutdown began, but it’s an opportune time to push it out of the nest early.</p>
<p>In the land of U.S. Census geographic and demographic data, the FTP server at <a href="ftp://ftp.census.gov">ftp.census.gov</a> is ordinarily a stable repository of extensive, high-quality files in downloadable ZIP form. This week, it’s unresponsive for the foreseeable future.</p>
<p>A community of census data users have worked with Code for America to <a href="http://forever.codeforamerica.org/Census-API/shutdown-2013.html">pool their collected backups</a> and made them available online in lieu of the normal Census.gov service. <a href="http://censusreporter.org/">IRE Census Reporter</a> developer Ian Dees has set up a <a href="https://census-backup.s3.amazonaws.com/index.html" title="Census Backup">selection of 2012 data hosted on Amazon S3</a>. Experimental cartographer Eric Fischer has made available his <a href="http://trafficways.org/tiger/edges/">complete collection of 2013 TIGER/Line edge shapefiles</a>. CUNY Mapping Service director Steven Romalewski supplied <a href="http://forever.codeforamerica.org/Census-API/shutdown-2013-districts-2013.html">2013 districts</a>. @OpenNebraska sent <a href="http://forever.codeforamerica.org/Census-API/shutdown-2013-tiger-2012.html">2012 TIGER/Line edges</a>. Darrell Fuhriman provided valuable <a href="http://forever.codeforamerica.org/Census-API/shutdown-2013-data-2010-2011.html">demographic summary files</a> from 2010. GeoCommons reminded us that <a href="http://geocommons.com/search?query=census">6,000 Census-derived datasets can be found on their service</a>.</p>
<p>This potluck-style process highlights the survivalist-style utility of big, dumb physical servers with actual hard drives. I think of my neighbor’s rain-catchment system, the chest freezer in the basement or my recently-earned Ham Radio license and laugh, but <a href="http://sunlightfoundation.com/blog/2013/10/02/government-apis-arent-a-backup-plan/" title="Government APIs Aren't A Backup Plan">Sunlight Foundation’s Eric Mill reminds us of the critical role of bulk data</a>:</p>
<blockquote><p>The only reliable way to preserve data online is to make copies — and the more copies, the better!</p>
<p>That’s why <strong>a government API will never be enough</strong>. It’s just so much easier to copy data when it’s directly downloadable in bulk. APIs can be extremely useful, but they also centralize control and form a <a href="http://fcw.com/articles/2013/10/01/private-sector-apps-api-shutdown.aspx">single point of failure</a>. Ultimately, <a href="http://sunlightfoundation.com/blog/2012/03/21/government-do-you-really-need-an-api/">APIs are optional</a> — data is a necessity.</p>
<p>…</p>
<p>Just as importantly: hosting static files requires fewer people, smaller systems, and less technical expertise. It’s vastly simpler and cheaper than hosting a live, “smart” data service. In the face of hard funding decisions, that’s going to matter.</p></blockquote>
<p>We’re not exactly <a href="http://en.wikipedia.org/wiki/The_Postman_(film)">getting our mail from Kevin Costner</a> yet, but these real and direct consequences of the federal shutdown remind us of the fragile pieces loosely joined that make up our digital platforms. Whether caused by GOP deadlock or <a href="http://aws.amazon.com/message/67457/">east coast electrical storms</a>, the data and services we build on are periodically stressed. What are you doing to prepare for the unexpected?</p>
<hr/>
<p>Questions? Comments? Hit us up <a href="http://twitter.com/codeforamerica">@codeforamerica</a>.</p>
