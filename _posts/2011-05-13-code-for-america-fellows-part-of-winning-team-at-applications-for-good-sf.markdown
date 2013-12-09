---
layout: post
status: publish
published: true
title: 'Applications for Good SF: <br />"All Income Foods" App Wins!'
author: Michelle Koeth
author_login: michelle
author_email: michelle@codeforamerica.org
wordpress_id: 5669
wordpress_url: http://codeforamerica.org/?p=5669
date: 2011-05-13 10:39:49.000000000 +00:00
categories:
- News
tags: []
---
Having only attended one other code-a-thon before in my life, in <a href="http://codeforamerica.org/2011/03/04/presidents-day-data-camp-dc/" target="_blank">Washington D.C.</a>, last weekend's <a href="http://applicationsforgood.org/contest-announcement/san-francisco/sf-comes-together-to-build-applications-for-good/">Applications for Good</a> competition gave me the opportunity to experience civic app development, West coast-style.
<div style="float: right; margin-left: 10px;">

[caption id="attachment_5672" align="alignleft" width="248" caption="Applications for Good Registration Table"]<a href="http://codeforamerica.org/wp-content/uploads/2011/05/codeathon1.jpg"><img class="size-medium wp-image-5672 " title="Applications for Good Registration Table" src="http://codeforamerica.org/wp-content/uploads/2011/05/codeathon1-300x197.jpg" alt="" width="248" height="178" /></a>[/caption]

</div>
Moderated by Arthur Grau of <a href="http://www.one-economy.com/" target="_blank">One Economy</a>, the event began with a round table introduction of everyone in attendance -- who they were, what they wanted to build, and how they wanted to be involved. The usual suspects were assembled: technology entrepreneurs, local community  activists, civic developers, and <a href="http://lalanaisage.com" target="_blank">lawyers who are developers and musicians on the side</a>. Wait, what? Like I  said, this is San Francisco after all.

And this was not your usual code-a-thon. After introductions, everyone split off into teams and began working on a project that interested them. For what you have to sacrifice spending most of a Saturday indoors at a computer, one of the benefits of participating in code-a-thons is that you can learn about a new technology in a relaxed and fun environment. So I decided to work on Code for America Fellow <a href="http://codeforamerica.org/author/jeremy/" target="_blank">Jeremy Canfield's</a> team, as his project seemed like it might involve some mapping visualizations; something I'm interested in learning more about. Jeremy's project, pitched on Friday by S.F. Dept. of Technology staff, was to make information regarding retailers that accepts food stamps (<a href="http://www.fns.usda.gov/snap/" target="_blank">SNAP</a> for Federal, or <a href="http://www.dss.cahwnet.gov/foodstamps/default.htm" target="_blank">CalFresh</a> in California), such as grocery stores, farmer's markets, and restaurants, more accessible to people using SNAP/CalFresh. We wanted to find a way to make sure that people who needed this important information could get it easily, immediately, and anywhere.

Jeremy and I were joined by two other local developers, <a href="http://www.codemass.com/">Aaron Bannert</a>, and <a href="http://www.ysiad.com/">Ysiad Ferreiras</a>. We had not met Aaron or Ysiad until the day of the code-a-thon, but our shared interest in the challenge of writing a food stamp retailer app made for quick bonding and a division of tasks to get to work immediately. Jeremy took on the telephony piece using a web service called <a href="https://www.tropo.com/home.jsp" target="_blank">Tropo</a>, Ysaid got to work building a <a href="https://github.com/ysiadf/AllIncomeFoods" target="_blank">GitHub</a> repo and the <a href="http://rubyonrails.org/" target="_blank">Ruby on Rails</a> framework, and Aaron and I set to work on importing into Rails, and providing query language for a dataset from the <a href="http://www.snapretailerlocator.com/" target="_blank">USDA</a> for retailers that accept food stamps from the State of California.
<div style="float: right; margin-left: 10px;">

[caption id="attachment_5674" align="alignright" width="300" caption="The quintessential heads down and coding pic. From left to right, Aaron Bannert, Ysaid Ferreiras, and Jeremy Canfield."]<a href="http://codeforamerica.org/wp-content/uploads/2011/05/codeathon2.jpg"><img class="size-medium wp-image-5674 " title="Heads down and working hard" src="http://codeforamerica.org/wp-content/uploads/2011/05/codeathon2-300x179.jpg" alt="" width="300" height="179" /></a>[/caption]

</div>
After the <em>usual</em> ice breaking -- <a href="http://twitter.com/#!/brianbehlendorf" target="_blank">Apache project people we've met</a>, why Rails is worthwhile to learn, and why <a href="https://www.eff.org/issues/patents" target="_blank">reexamination</a> is a great patent troll avoidance strategy -- Aaron and I set to work with our back-end data piece. Four hours later, we had the core app written, a strategy for finding nearest locations, and a query for getting the data from the database. Then we met up with our teammates and brought together all of our pieces. What we ended up with was the <strong>All Income Foods app: SMS-based service which you could text into with your location, and it'd reply back with the nearest grocery stores that accepted food stamps.</strong>

Around 5pm, each team presented their projects before the judges. Projects ranged from a simple phone app which allows Goodwill recipients easy access to information on job, health and other support services available to them, to a prototyped community stories app, enabling locals to share their anecdotes and educate students about the block they live on.

Out of all of <a href="http://applicationsforgood.org/contest-announcement/san-francisco/sf-comes-together-to-build-applications-for-good/">San Francisco which came together to build applications for good</a>, "PointRunner," an app to gamify outdoor running routines, won the Audience Favorite award, "Wellness Garden," an app to positively encourage health and recovery activities won third place, "Tap Cloud," an augmented reality app won second place, and our app, named the "All Income Foods" app, won first place. <strong>Our team was honored and excited to win first place! </strong>

Now the bigger task is before us to build more features into our app for submission to the <a href="http://applicationsforgood.org/contests/">National contest, which ends May 16, 2011</a>. More importantly, we want to make this app as useful and effective as possible for those who need it. Help us out on <a href="https://github.com/ysiadf/AllIncomeFoods">GitHub</a>.
