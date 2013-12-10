---
layout: post
status: publish
published: true
title: Mapping Floods With Lightweight Technology
author: Emily Wright Moore
author_login: emily
author_email: emily@codeforamerica.org
wordpress_id: 18468
wordpress_url: http://codeforamerica.org/?p=18468
date: 2012-11-02 11:50:29.000000000 +00:00
categories:
- News
- Austin
- Fellowship
- Gov2.0
tags: []
wordpress_html: true
wordpress_permalink: http://www.codeforamerica.org/2012/11/02/mapping-floods/
---

<p><strong><a href="http://codeforamerica.org/wp-content/uploads/2012/11/Daniel-Herrera3.jpg"><img alt="" class="alignright size-medium wp-image-18476" height="160" src="http://codeforamerica.org/wp-content/uploads/2012/11/Daniel-Herrera3-300x200.jpg" title="Flooded crossing" width="240"/></a></strong></p>
<h2>Turn Around, Don’t Drown</h2>
<p><a href="http://en.wikipedia.org/wiki/Low_water_crossing">Low water crossings</a> aren’t something we get a lot of here in San Francisco, but many Austinites are intimately familiar with them. <a href="http://en.wikipedia.org/wiki/Flash_flood">Flash floods</a> and sudden high-volume rain cause runoff and will quickly fill or overflow riverbeds and low lying areas and cause low water crossings to close, making streets impassable.</p>
<p><a href="http://codeforamerica.org/wp-content/uploads/2012/11/image001.png"><img alt="" class="alignright size-medium wp-image-18477" height="180" src="http://codeforamerica.org/wp-content/uploads/2012/11/image001-300x225.png" title="image001" width="240"/></a></p>
<p>When this happens, it’s important that drivers have enough information to know which routes to take. In person, it’s difficult to tell how quickly water is flowing, or even how deep it is. <a href="http://en.wikipedia.org/wiki/The_Oregon_Trail_(video_game)">Oregon Trail</a>-style attempts to ford these crossings result in multiple casualties each year.</p>
<p>In June, when I met Matt Porcher of the <a href="http://www.austintexas.gov/department/watershed-protection">Watershed Department</a>, for him to close crossings required leaving a message with the on-duty officer at <a href="http://www.austinhsem.com/">Austin Homeland Security and Emergency Management</a>. When they called back he would relay to them the closed crossing(s). Which the officer would then post to the website, <a href="http://www.austinhsem.com/go/doctype/3603/81175/">here</a>. Site visitors could then view the list to figure out if any of the listed closures were along their intended routes.</p>
<p>This was a great opportunity for lightweight technology to make this process better and easier. So we did. Matt and I built <a href="http://atxfloods.com/">ATXfloods.com</a> using CartoDB, Google Docs, HTML, CSS, and a little bit of JavaScript. It’s lightweight, easy to setup, and completely free. It’s also a responsive design that works on a smartphone or tablet.</p>
<p><a href="http://codeforamerica.org/wp-content/uploads/2012/11/Screen-Shot-2012-11-01-at-4.50.53-PM.png"><img alt="" class="alignnone size-large wp-image-18478" height="351" src="http://codeforamerica.org/wp-content/uploads/2012/11/Screen-Shot-2012-11-01-at-4.50.53-PM-1024x562.png" title="Screen Shot 2012-11-01 at 4.50.53 PM" width="640"/></a></p>
<p><a href="http://codeforamerica.org/wp-content/uploads/2012/11/atxfloods_eoc.jpeg"><img alt="" class="alignright size-medium wp-image-18488" height="180" src="http://codeforamerica.org/wp-content/uploads/2012/11/atxfloods_eoc-300x225.jpg" title="atxfloods_eoc" width="240"/></a>Having something on a map makes it more usable, shareable, and easier to track. We’ve been delighted to see the use of it spread and increase the effectiveness of other efforts. For example, the Austin Fire Department uses it to track closures so they know which route to take for emergencies.</p>
<p><a href="http://codeforamerica.org/wp-content/uploads/2012/11/atxfloods_eoc.jpeg"><br/>
</a></p>
<p> </p>
<h2><strong>Here’s how it works:</strong></h2>
<ul>
<li><strong>CartoDB<br/>
</strong>With a CartoDB account, you can import a CSV file of locations.<br/>
For help setting it up, here’s a great <a href="https://github.com/boundsj/maplate">tutorial</a> by 2012 Fellow <a href="http://codeforamerica.org/jesse-bounds/">Jesse Bounds</a>.<br/>
To see how to set up the open/closed status of the points in CartoDB, check out the readme on the github repo, <a href="https://github.com/emilyville/floodwatch/tree/gh-pages">here</a>.<br/>
<a href="http://codeforamerica.org/wp-content/uploads/2012/11/Screen-Shot-2012-11-01-at-1.55.17-PM.png"><img alt="" class="alignnone size-medium wp-image-18479" height="220" src="http://codeforamerica.org/wp-content/uploads/2012/11/Screen-Shot-2012-11-01-at-1.55.17-PM-300x270.png" title="Screen Shot 2012-11-01 at 1.55.17 PM" width="243"/></a>    <a href="http://codeforamerica.org/wp-content/uploads/2012/11/Screen-Shot-2012-11-01-at-4.54.00-PM.png"><img alt="" class="alignnone size-medium wp-image-18480" height="220" src="http://codeforamerica.org/wp-content/uploads/2012/11/Screen-Shot-2012-11-01-at-4.54.00-PM-300x228.png" title="Screen Shot 2012-11-01 at 4.54.00 PM" width="300"/><br/>
</a></li>
<li><strong>Bootstrap and HTML/CSS files<br/>
</strong>Download a <a href="http://twitter.github.com/bootstrap/">Bootstrap</a> template and customize it to give it your own style, or use <a href="https://github.com/emilyville/floodwatch">this one</a>. ATXfloods uses tabs to display some extra content like the Twitter hashtag #atxfloods, some extra tips, and links to helpful resources.<br/>
<a href="http://codeforamerica.org/wp-content/uploads/2012/11/Screen-Shot-2012-11-01-at-4.56.37-PM.png"><img alt="" class="alignnone size-medium wp-image-18481" height="262" src="http://codeforamerica.org/wp-content/uploads/2012/11/Screen-Shot-2012-11-01-at-4.56.37-PM-300x262.png" title="Screen Shot 2012-11-01 at 4.56.37 PM" width="300"/><br/>
<strong><br/>
</strong></a></li>
<li><strong>Tabletop.js and Google Docs<br/>
</strong>Next, we needed a good way for people to know when looking at the map how current the information is. We used <a href="https://github.com/jsoma/tabletop">Tabletop.js</a> to easily integrate Google Docs spreadsheets and display the most recent status update at the top of the page.<br/>
<a href="http://codeforamerica.org/wp-content/uploads/2012/11/Screen-Shot-2012-11-01-at-4.57.53-PM.png"><img alt="" class="alignnone size-medium wp-image-18482" height="194" src="http://codeforamerica.org/wp-content/uploads/2012/11/Screen-Shot-2012-11-01-at-4.57.53-PM-300x194.png" title="Screen Shot 2012-11-01 at 4.57.53 PM" width="300"/><br/>
</a>Google Docs happens to be blocked in most of Austin City employees, so I used a Google form that can be filled out on a phone, or from email, and will directly update the <a href="https://docs.google.com/a/emilyville.com/spreadsheet/pub?key=0AvUsRT_oqcQvdC1uN2VIUERTLV9IRlBHby1IdjhjU3c&amp;output=html">spreadsheet</a> and ATXfloods.com.<br/>
<a href="http://codeforamerica.org/wp-content/uploads/2012/11/Screen-Shot-2012-11-01-at-4.58.06-PM.png"><img alt="" class="alignnone size-medium wp-image-18483" height="114" src="http://codeforamerica.org/wp-content/uploads/2012/11/Screen-Shot-2012-11-01-at-4.58.06-PM-300x114.png" title="Screen Shot 2012-11-01 at 4.58.06 PM" width="300"/></a></li>
</ul>
<p>Also note that if you don’t have your own URL or hosting, you can host it on <a href="http://pages.github.com/">GitHub Pages</a>, like <a href="http://emilyville.github.com/floodwatch/">this version</a>.</p>
<p>Share it. <a href="https://github.com/emilyville/floodwatch/tree/gh-pages">Fork it</a>. Use it to map something cool!</p>
<p><strong><strong>Questions? Email us.<br/>
</strong></strong>Emily Wright: emily[@]codeforamerica.org<br/>
Matt Porcher: matthew.porcher[@]austintexas.gov</p>
<p> </p>
<p>Questions? Comments? Hit us up <a href="http://twitter.com/codeforamerica">@codeforamerica</a>.</p>
