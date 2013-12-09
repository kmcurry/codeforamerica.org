---
layout: post
status: publish
published: true
title: Github pushes, Screaming Hawks, and a Culture of Collaboration
author: Talin Salway
author_login: talin
author_email: talin@codeforamerica.org
wordpress_id: 5091
wordpress_url: http://codeforamerica.org/?p=5091
date: 2011-04-26 09:00:00.000000000 +00:00
categories:
- CfA Labs
tags:
- labs
---
It's a busy day in the Code for America offices. Coders and Designers work in twos and threes, building out four or five different projects. Suddenly, over the bustle of discussion, a loud <a href="http://www.youtube.com/watch?v=33DWqRyAAUw">falcon scream</a> pierces the air, followed by a robotic voice reading out "Scott Silverman pushed to homework_notifier: Fixed secondary button gradient colors in Firefox." Around the office, some fellows stop and look up for a second, offering applause, congratulations, or just laughing at the absurdity of the sound.

What's happening here?

A couple weeks ago, some of the Fellows on Team Boston, myself included, were working late into the night on our <a href="http://codeforamerica.org/?cfa_project=whatsassign-me">"Homework Notifier</a>" app. I pushed a minor bugfix to our <a href="https://github.com/codeforamerica/homework_notifier">Github repository</a>, and a few seconds later, one of the other fellow's iPhone beeped. They had set up the github service hook to notify them via Notifo whenever someone updated our repository. "That's kind of interesting," I pondered, "but <em>why</em> would you want to do that?"

Their response kind of surprised me: "Well, it gives you an idea of what's going on with the project, so you know what the rest of the team is up to." Not long after, one of my teammates Max came up with an idea: "Hey, could we make those speakers scream out a hawk sound on every commit?" People here love the screaming hawk sound. I think it started with a homonym of my name, <em>Talin</em>, and grew from there.

My favorite projects are the simple scripts that directly accomplish what you want. Thus was born the Github Screamer: a little <a href="http://sinatrarb.com">Sinatra</a> script on the computer powering the speakers, with a github <a href="http://help.github.com/post-receive-hooks/">post-receive hook</a> to fire it off on every push. After setting this up for the homework notifier app, I decided to include other current projects as well. At the time, I figured it would just be a bit of an amusing annoyance the next day at work, and we'd run it for a day or so before someone shut it off. A good joke, but nothing more. (Although, unexpected to me, Scott ended up working even later that night. At 3am, he was the hawk scream's first victim. muahahaha!)

The actual response the next day, again, surprised me. After people figured out what was going on, it was actually something highly appreciated. Features were requested and added, the notifications gained a text-to-speech synthesizer, and user-customizable sounds.

Now, the audible "scream" notifications are a part of daily life here in the CfA offices. A hawk scream lets me know that a fellow Boston teammate has pushed to our project, and I should probably check out what's changed. But, in addition, there's now a Chewbacca cry when Alan updates the <a href="https://github.com/codeforamerica/engagement_toolkit">Engagement Toolkit</a>, an intercom noise when Aaron works on some <a href="https://github.com/codeforamerica/census2pgsql">open census data</a>, or a clip from Duck Soup's "<a href="http://youtu.be/uu_zwdmz0hE">Barbara Streissand</a>" when Michelle pushes to the <a href="https://github.com/codeforamerica/designforamerica">RedesignGov</a> repo. These sounds not only help us keep track of what everyone is up to, it really helps us bond as a class of fellows.

The source for our Github Screamer is available <a href="https://github.com/codeforamerica/github_scream">here</a>. You can copy that down and set this up in your office. Also, check out some of our other open source projects on our <a href="https://github.com/codeforamerica/">github profile</a> (you can also see an overview <a href="http://codeforamerica.org/projects/">here</a>). Write some code for America, and when you commit it, you can know that somewhere in San Francisco, you can surprise a CfA fellow with a full-volume hawk scream.
