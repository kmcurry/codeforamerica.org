---
layout: post
status: publish
published: true
title: 'Random Hacks of Kindness '
author: Chacha Sikes
author_login: chacha
author_email: chacha@codeforamerica.org
author_url: http://chachaville.com
wordpress_id: 6021
wordpress_url: http://codeforamerica.org/?p=6021
date: 2011-06-08 09:23:24.000000000 +00:00
categories:
- News
tags: []
---
Went up to my Code for America city (Seattle) this weekend to participate in Random Hacks of Kindness, or #RHOK3. <a href="http://rhok.org">Random Hacks of Kindness</a> is a movement of software developers, hackers, and humanitarian workers who get together for intensive weekends building tools to support emergency relief efforts.

In Seattle, we had about 80 people actively developing projects this weekend. I helped to facilitate the large group collaboration, helping people who don't know each other to quickly find alliances in the group so as to have productive working teams. This was called a "<a href="http://www.cnn.com/2011/TECH/innovation/06/08/hacks.kindness.followup/">Brain Collision</a>" on CNN, and I was excited to know that this was the first time that some of movers & shakers at NASA were able to attend a participatory coding event like RHOK. I'm grateful to Willow Brugh (<a href="http://www.jigsawrenaissance.org/">Jigsaw Renaissance</a> & Johnny Diggz <a href="http://www.tropo.com">Tropo</a>for bringing me up there to participate.

Microsoft had given us space on their campus in Redmond, and we had hundreds of feet of whiteboard plastered with wireframes, post-it notes as we created many working prototypes. It was awesome. Have a look:

<object width="400" height="300"> <param name="flashvars" value="offsite=true&lang=en-us&page_show_url=%2Fphotos%2Flinepithemate%2Fsets%2F72157626915607946%2Fshow%2F&page_show_back_url=%2Fphotos%2Flinepithemate%2Fsets%2F72157626915607946%2F&set_id=72157626915607946&jump_to="></param> <param name="movie" value="http://www.flickr.com/apps/slideshow/show.swf?v=104087"></param> <param name="allowFullScreen" value="true"></param><embed type="application/x-shockwave-flash" src="http://www.flickr.com/apps/slideshow/show.swf?v=104087" allowFullScreen="true" flashvars="offsite=true&lang=en-us&page_show_url=%2Fphotos%2Flinepithemate%2Fsets%2F72157626915607946%2Fshow%2F&page_show_back_url=%2Fphotos%2Flinepithemate%2Fsets%2F72157626915607946%2F&set_id=72157626915607946&jump_to=" width="400" height="300"></embed></object>

<a href="http://www.flickr.com//photos/linepithemate/sets/72157626915607946/show/">Slideshow</a>

Pascal Shuback, who is an emergency manager for King County, created SAARAA, which is a situational reporting mobile application which allows for crowd-sourcing information about emergency situations. For example, you can report a drowning child (using the similar data intake methods that emergency responders use currently) or a fire or other situation. And you can upload pictures. The idea is to have as much information about an emerging situation so as to understand it and respond more effectively.

There were a number of people from NASA (including Michael Laine, of the Space Elevator idea, who prototyped a "smoke detector on a string" or "tethered tower" which is a tool that can help assess air quality or temperature, which emergency relief workers could drop down the side of a tall building, or float up in a weather balloon, to get an understanding of the location of a fire or other disaster.

<h3>MoveFood</h3>
The project I worked on at RHOK was called MoveFood. MoveFood is a tool that allows people with food to announce that the food is available, and then people who need food can claim it. This can help in everyday situations, but the tool would also be useful in the event of an ongoing disruption to the supply chain of food.

There were <strong>FOUR</strong> groups in other cities that also worked on this. We struggled with the tension between real disasters and this form of everyday disaster. One important thing about disasters is that you should, ideally, be as prepared as you can be: ahead of time.

At the event, we created an API for the food transactions, and a javascript+html front end, so that the tool could be used as a web application. I worked on the front end, and also made it possible that any food items could be announced in short format via twitter and text (using a service called "<a href="http://smsified.com/">SMSified</a>".) For example, a message would say: Apples 40 pounds (37.788299, -122.399983) EXP: 2011-07-11 t.co/abcdef. Replying with a text message would allow you to claim the item. Johnny Diggs, who's company makes SMSified & Tropo, helped me figure out how to connect our database to text message.

Kip Silverman, from Portland, has been thinking about this idea for over two years, and brought a lot of knowledge about the legal implications of food sharing. I'm definitely planning to continue working on this project, and am excited to see how this could help in our cities. Not only is food an issue with people not having enough to eat, but also a huge source of waste in cities. Making it easier to distribute the food would help reduce waste. Practicing this form of resource distribution in non-emergency situations will also help in the event of an actual emergency.

<h3>Disaster Response</h3>
Like most people, I'm in awe of first responders and people who rescue people in need. It was a tremendous opportunity to be able to collaborate with real life first responders like Pascal Shuback (he was a fireman.) Claire from Microsoft's disaster response team, said that software that is developed to work in a crisis situation can also normally be used in everyday situations, such as at the grocery store.

I enjoyed trying to help my own team conceptualize and wireframe our project. I said "Imagine if an earthquake or flood happened right now. What would we build to help coordinate food exchange?" I can definitely say that this form of thinking help to weed out some of the philosophical technological ideas that often inhabit the minds of developers like myself. Thinking about emergency response has some interesting form factors. The technology you use should be stable, ubiquitous, easy to fix, use clear language, work quickly, not have too many parts and be redundant in the event of failures of various grids: electrical, internet, mobile. For MoveFood, we imagined a "disaster switch" that could kick into effect. This would allow a dispatcher to help coordinate food distributions.

<h3>Other projects</h3>
<strong>iRecord</strong>
A way to have offline emergency communications routed through phones, basically having an interface to the cloud. (*I think I have this name right.)

<strong>Eco-tricorder</strong>
A way to get information about water quality, superfund sites, and government representatives for a location - to understand the state of the environment and be able to help out the EPA or similar organizations to recommend areas that have low quality environmental factors (poor air quality, bad water.)

<strong>HelpSauce</strong>
A tool to map emerging twitter hashtags to figure out where a situation is working. Talking about using !help (instead of #help) as a twitter way to indicate that you are actually participating in an event (vs. talking about it) Ex. !earthquake or #earthquake. !help !sos

<strong>Open211</strong>
<a href="http://rectangl.es">"Redirectory"</a> - an open social services directory. More work was done to bring this to Portland, Oakland, &amp; Seattle and other cities.

We had about 80 people working on these projects, and teams were generally 5-10 people. 2 days of development. Multiple programming languages and skillsets, and most people did not know each other already. I really learned so much about designing software for emergency situations, and I've already started sharing this with the other Code for America fellows. They don't know it yet, but I might declare one of our Labs Fridays "Emergency Friday" where we hack for emergencies. So thanks to everyone who participated.
