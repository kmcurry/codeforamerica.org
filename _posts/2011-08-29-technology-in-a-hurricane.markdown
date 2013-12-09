---
layout: post
status: publish
published: true
title: Technology In A Hurricane
author: Abhi Nemani
author_login: Abhi
author_email: abhi@codeforamerica.org
wordpress_id: 8197
wordpress_url: http://codeforamerica.org/?p=8197
date: 2011-08-29 13:48:40.000000000 +00:00
categories:
- Commentary
tags: []
---
As Hurricane Irene has now passed through the east coast -- which just so happened to overlap with my brief trip to New York -- the most common terms I've heard in response sound something like "overhyped" and "underwhelming." (All in all, that's probably a good thing; the opposite would be much, much worse.) With that lens, however, we risk glazing over the nitty gritty of the weekend -- that is, what was done to prepare, manage, and respond to the storm. And in particular, we risk missing an opportunity to take stock of what I think was a watershed moment in the Gov 2.0 movement.
<h3>Before the Storm: NYC.Gov</h3>
As Irene approached New York City, there was understandably a lot of confusion and concern about, frankly, what was going on. Was the hurricane going to hit the city? Was there going to be an evacuation? If so, when and where? And notably in the midst of that confusion, citizens turned to their government, particularly their government's website, for clarification. New York City aptly posted evacuation maps and crisis guides online for easy access, but there was in fact so much traffic on <a href="http://nyc.gov">NYC.gov</a> that the site went down on Friday afternoon. Not good. While this suggests the city should consider a more scalable infrastructure -- maybe take the popular recommendation of the cloud -- I found two immediate reactions more interesting.

First, Civic Commons' Philip Ashlock <a href="http://crisis-response.s3-website-us-east-1.amazonaws.com/irene.html">mirrored the data and info</a> that he had downloaded onto Amazon's (usually) reliable cloud, sharing the link all around. Instead of being embarrassed, the City's Chief Digital Officer <a href="http://codeforamerica.org/wp-content/uploads/2011/08/rsterne.png">Rachel Sterne even tweeted</a> out the link herself. They understood, it was the information, not the host that mattered.

Second, the city <a href="http://gov20.govfresh.com/as-nyc-gov-buckles-city-government-pivots-to-the-internet-to-share-hurricane-irene-resources/">"optimized" their website</a>. NYC.gov has a wealth of information and even editorialized content, but with more data, comes higher load times and the need for more bandwidth. Neither of which are preferable in a crisis. So after the site went down, it soon came back up, slimmed down. Significantly. See for yourself:

<a href="http://codeforamerica.org/wp-content/uploads/2011/08/nyc-irene.jpg"><img class="aligncenter size-large wp-image-8210" title="nyc-irene" src="http://codeforamerica.org/wp-content/uploads/2011/08/nyc-irene-616x1024.jpg" alt="" width="616" height="1024" /></a>

It clocks in at a lean 54 kilobytes and a 3.2 second load time, according to Chrome. What's more notable than the tweaks -- I doubt this version will stay up long -- is the utilitarian and practical thinking. I'd imagine it was a something of a bitter pill to swallow, chopping off so much of the sites, but it's good that they remembered that websites don't need to be all things at all times.
<h3>During the Storm: Twitter &amp; Crisis Mapping</h3>
A growing trend in the civic technology space is the use of mobile devices and people on-the-ground to crowdsource information reporting: platforms such as SeeClickFix, CitySourced, and Ushahidi and have gained traction in cities around the world, with the latter especially coming to relevancy in crisis situations. As <a href="http://radar.oreilly.com/2011/08/social-mapping-and-crisis-data.html">Alex Howard of O'Reilly Radar</a> put it, "In this information ecosystem, media, government and citizens alike will play a critical role in sharing information about what's happening and providing help to one another." And Irene was a proof point. His post details the numerous data reporting platforms in use during the hurricane, and in New York alone, I counted at least three: <a href="http://www.mobilecommons.com/blog/2011/08/text-irene-to-877877-to-report-hurricane-damages/">CrowdMap</a>, <a href="http://www.wnyc.org/articles/wnyc-news/2011/aug/26/your-signs-prepared-or-unprepared-new-york/">NYTimes/WNYC</a>, and of course <a href="http://www.nyc.gov/apps/311/allServices.htm?requestType=topService&amp;serviceName=Hurricane+Damage+Report">311</a>. While these are likely valuable tools for citizens and governments alike, the multiplicity and the possible redundancy therein suggests the need for better integration and standardization across various platforms. And here's why:

<a href="http://codeforamerica.org/wp-content/uploads/2011/08/warning.png"><img class="aligncenter size-full wp-image-8215" title="warning" src="http://codeforamerica.org/wp-content/uploads/2011/08/warning.png" alt="" width="610" /></a>

That was the warning prompt sitting atop the <a href="http://nycsevereweather.crowdmap.com/">NYC's Severe Weather CrowdMap</a>, and it reads (excerpted), "This is an information sharing site. Insofar as any posts made concern weather conditions and weather-related service disruptions, the City will not take action." This disconnect between information and action acts as a hollow barrier for meaningful civic participation. Not only is there a skewed perception then of the actual damage, there's also a bad image of hundreds of seemingly unresolved problems. Just putting dots on a map is sometimes a bad thing. Especially in the context of service requests and citizen/government interaction, <a href="http://www.innovations.harvard.edu/cache/documents/1285/128521.pdf">where it's said</a> that so much trust is built through two-way dialogue and conversation.

(<a href="http://open311.org/2011/07/ushahidi-and-the-open311-ecosystem/">Current efforts</a> to align Ushahidi with the Open311 specification should start to help with this ongoing challenge of standardization.)

Another tool government turned to, especially here in New York, was social media, and in particular, twitter. (Of course, they weren't the only ones, and for those of us trapped indoors, <a href="http://twitter.com/irene">@Irene</a> was an entertaining read.) <a href="http://twitter.com/@NYCMayorsOffice">@NYCMayorsOffice</a> seemed to led the way in New York with their updates on the storm and evacuation plans more than doubling their monthly tweet rate, according to TweetStats (see left).

<a href="http://codeforamerica.org/wp-content/uploads/2011/08/nyc-chart.jpg"><img class="aligncenter size-full wp-image-8231" title="nyc-chart" src="http://codeforamerica.org/wp-content/uploads/2011/08/nyc-chart.jpg" alt="" width="598" height="338" /></a>

This activity was rewarded. On Thursday, August 25, @NYCMayorsOffice had 24,507 follows; today, August 29, it has 52,228, according to <a href="http://twittercounter.com/NYCMayorsOffice">TwitterCounter</a>. <strong>That's a 113 percent increase (+27,721) in four days.</strong> Hopefully, the city will continue to leverage that resource moving forward not just in the clean up, but for future engagement.
<h3>After?</h3>
I came across many posts this weekend of people asking, something along the lines of "What if we had all of this technology during Katrina?" I'm not sure how to answer that, honestly. I can only hope things would have turned out differently. But I don't think that's where our focus should be right now. We've got now a strong and growing infrastructure for civic action in a crisis -- an infrastructure that has proven useful for coordination and communication. And I've only touched on a small piece of it. We should continue building it, developing and integrating our systems, and roll it out everywhere with a different question in mind: "With the best technology imaginable, what will the next crisis look like?"
