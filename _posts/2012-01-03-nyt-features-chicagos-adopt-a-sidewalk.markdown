---
layout: post
status: publish
published: true
title: NYT Features Chicago's "Adopt-a-Sidewalk"
author: Abhi Nemani
author_login: Abhi
author_email: abhi@codeforamerica.org
wordpress_id: 10389
wordpress_url: http://codeforamerica.org/?p=10389
date: 2012-01-03 08:04:19.000000000 +00:00
categories:
- News
tags: []
---
As the Windy City prepares for another major snow season, Chicago's CTO John Tolva and team have been hard at work, turning out a robust suite of online tools to help citizens track and even support the city's management efforts: <a href="http://www.cityofchicago.org/city/en/depts/mayor/snowportal/chicagoshovels.html">ChicagoShovels.org</a>. Today, the <em><a href="http://www.nytimes.com/2012/01/03/us/chicagoshovels-web-site-gives-lowdown-on-snow.html?_r=1">New York Times</a></em> featured their innovative efforts -- which ranged from real-time snow plow tracking to 311-powered crowdsourcing:
<blockquote>Among other elements of the new Web site: organization of a “Snow Corps,” which will match volunteers with mounds to shovel; winter-related computer applications to guide people when two inches of snow has fallen, alerting them to parking bans on city streets or, if it is too late, telling them where their car has been towed to; and an “adopt-a-sidewalk” program that will soon allow residents to share shoveling tools and claim shoveling responsibilities on a map.</blockquote>
Notably, <a href="http://webapps.cityofchicago.org/eforms/org/cityofchicago/adoptsidewalk/index.jsp">"Adopt-a-Sidewalk,"</a> which is tool launching soon, is in fact built on top of (or <a href="https://github.com/Chicago/adopt-a-sidewalk">forked </a> to use the technical term) of the app <a href="http://codeforamerica.org/?cfa_project=adopt-a-hydrant">CfA fellows developed for the city of Boston last year</a>: <a href="http://adoptahydrant.org">Adopt-a-Hydrant</a>.

<a href="http://codeforamerica.org/wp-content/uploads/2012/01/chicagoshovels.png"><img class="aligncenter size-full wp-image-10391" title="chicagoshovels" src="http://codeforamerica.org/wp-content/uploads/2012/01/chicagoshovels.png" alt="" width="222" height="83" /></a>

If you recall, that tool, as well, was made as a response to the city concerns over the impact of snowstorms on emergency readiness. Developed by fellow Erik Michaels-Ober, Adopt-a-Hydrant, however, <a href="http://civiccommons.org/2011/11/crowdsourcing-civic-infrastructure/">was written to function as a platform</a>, able to be re-purposed for any kind of civic infrastructure; in fact, the original app included reference to "Hydrant" only once in the code, making it simple and easy to be reused. Of course, as you can see on GitHub, the city of Chicago is <a href="https://github.com/Chicago/adopt-a-sidewalk/commits/development">building on top of the platform</a> with new features and customizations -- which should only make it more useful for the <a href="http://marketplace.civiccommons.org/apps/adopt-hydrant">next city</a>.

As the article rightly notes, however, it remains to be whether Chicagoans will "really wish to officially stake out shoveling responsibilities," so we too are eager to see the platform rolled out this year. <a href="http://abclocal.go.com/wls/story?section=resources&amp;id=8487788">ABC Chicago reports</a> that it will launch after beta testing with the media partner, <a href="http://www.ohsowe.com/home">OhSoWe</a>.

In any event, this, to me, illustrates both to the value of reusable software and the creative ways cities can use it -- the motivating ideas for our <a href="http://marketplace.civiccommons.org">Civic Commons Marketplace</a>. The Marketplace, which just beta launched, is intended to help cities connect around the software they buy and build; the thinking being that cities need to know what others are using to share tools and best practices for better, more cost-effective services. Put simply, cities can and should share technology for the public good. And indeed that's exactly what we're seeing here with Chicago building off of Boston's efforts: open, collaborative civic innovation.

[cc-mkplc app="adoptahydrant" height="370px"]
