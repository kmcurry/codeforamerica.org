---
layout: post
status: publish
published: true
title: Blake's CfA Summer
author: Blake Hall
author_login: blake
author_email: blake@codeforamerica.org
wordpress_id: 8191
wordpress_url: http://codeforamerica.org/?p=8191
date: 2011-08-30 06:28:50.000000000 +00:00
categories:
- News
- 2011 Interns
tags: []
---
This summer I worked with four other interns on building up Code for America's Developer Tools. We found a bunch of open Government APIs for different agencies and dataset. We then built wrappers for the APIs to allow developers better access to the data. 

Justin Stoller -- a fellow intern -- and I worked on making Ruby Gems for the <a href="https://github.com/codeforamerica/world_bank_ruby">World Bank</a>, <a href="https://github.com/codeforamerica/fed_spending_ruby">Fed Spending</a>, <a href="https://github.com/codeforamerica/epa_python">EPA EnviroFacts</a>, NTIA & FCC's <a href="http://broadbandmap.gov/" target="_blank">BroadbandMap.gov</a>, and a few others. I then built a quick little web app to help demonstrate some of the <a href="https://github.com/codeforamerica/broadband_map_ruby">broadband data</a> that you can access: <a href="http://compare-broadband.heroku.com/">http://compare-broadband.heroku.com/</a>

<a href="http://compare-broadband.heroku.com/"><img src="http://codeforamerica.org/wp-content/uploads/2011/08/wireless.png" alt="" title="wireless" width="610px" class="aligncenter size-full wp-image-8192" /></a>

The app, <a href="http://compare-broadband.heroku.com/">Compare Broadband</a>, uses the <a href="http://broadbandmap.gov/" target="_blank">BroadbandMap.gov</a> gem I wrote to check to locations against <a href="http://broadbandmap.gov/" target="_blank">broadbandmap.gov</a>'s data and return a comparison of each locations broadband providers, both wireline and wireless, as well as each provider's advertised speeds. This is just a minuscule example of what can be done using these government API's that can now be accessed easily through our gems, eggs, and libraries.

<a href="http://compare-broadband.heroku.com/"><img src="http://codeforamerica.org/wp-content/uploads/2011/08/broadband-1024x279.png" alt="" title="broadband" width="610px" class="aligncenter size-large wp-image-8193" /></a>

<em>(Over the summer of 2011, <a href="http://codeforamerica.org/2011/06/15/meet-the-2011-cfa-interns/">over a dozen students interned</a> with Code for America. They brought great energy, passion, and skills to bear on our projects and our mission to make government more open and efficient. Over the next week, we’ll be posting their summaries of their work and learnings, in addition to an overview of the summer.)</em>
