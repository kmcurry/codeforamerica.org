---
layout: post
status: publish
published: true
title: Securing the Louisville Dashboard
author: Shaunak Kashyap
author_login: shaunak
author_email: shaunak@codeforamerica.org
wordpress_id: 27765
wordpress_url: http://www.codeforamerica.org/?p=27765
date: 2013-11-21 17:13:38.000000000 +00:00
categories:
- Fellowship
- Open Source
- 2013 Fellow
- Louisville
tags: []
wordpress_html: true
wordpress_permalink: http://www.codeforamerica.org/2013/11/21/securing-the-louisville-app/
---

<p dir="ltr">Our Fellowship team, the Bourbon Planners, built a <a href="http://codeforamerica.org/?cfa_app=jail-population-management-dashboard" target="_blank">Jail Population Management Dashboard</a> for the city of Louisville, Ken. This dashboard lets decision makers in Louisville’s criminal justice system visualize and analyze the population in various corrections programs.</p>
<p dir="ltr">For reasons of privacy it became necessary to restrict access to the dashboard to certain people. These people represented various stakeholders in Louisville’s criminal justice system — from judges to corrections officials to public and private attorneys. Some stakeholders were government employees while others were private citizens. Some of the government employees worked for the City of Louisville while others worked for the State of Kentucky.</p>
<p dir="ltr">From a technical standpoint, this meant that there was no <em>single</em> source that could identify <em>all</em> these stakeholders. This made authentication and authorization a challenge but we were able to implement a single, fast, cheap and easy-to-use login method for all stakeholders.</p>
<h2 dir="ltr"></h2>
<h2 dir="ltr">Authentication</h2>
<p dir="ltr">Given the diverse set of stakeholders and the lack of a single identity provider, we briefly flirted with the idea of implementing our own authentication system. While this would certainly solve the single identity provider problem (because our application would play that role) it has a serious downside: correctly implementing a homegrown authentication system is tricky at best. We were dealing with some serious information here – think names of inmates in some cases — and could not risk a security breach. On a less serious note, we also faced the high opportunity cost of implementing a homegrown solution with only a handful of weeks left in the Fellowship.</p>
<p dir="ltr">We considered allowing users to sign-in using their Google, Yahoo, Facebook, or Twitter accounts. We felt each of these options were less than ideal for our application due to several reasons: Each of these services are not just identity providers; they also provide other functionality associated with the identity. Further, our users would have to either re-use their personal identities on one of these services or create a new one and have to remember it just so they could use our application.</p>
<p dir="ltr">After some internal discussion we proposed <a href="http://www.mozilla.org/en-US/persona/" target="_blank">Mozilla Persona</a> as a solution for authentication. It fit the constraints outlined previously: it is a single source of identity, it is not homegrown, it allows users to reuse their work email addresses as their unique identifiers and, finally, it is no more than simply an identity provider.</p>
<p><img alt="" height="313px;" src="https://lh3.googleusercontent.com/6MacQvlaabBUaKvOtCo3WqQGqmb29H6ji-XNNXbeAYyyNVlezGJ_HeJykJdmEj9d6pGpORDAByKa1sbijFsY0bomWEguJDz12f6gYYxrbf1lh0hDvqKWg4UY" width="624px;"/></p>
<h2 dir="ltr"></h2>
<h2 dir="ltr">Authorization</h2>
<p>While Persona solved our <em>authentication</em> problem (i.e. is this user who she claims to be?), we still needed a way to manage <em>authorization</em> (i.e. is this user allowed to access the Dashboard?). Since we had a relatively small set of users who needed access, we just needed to maintain a whitelist of these users somewhere and check against it when a user signed-in via Persona.</p>
<p>So now the authorization problem was reduced to these questions: where do we store this list of users and their rights and how do we restrict access to this list to certain administrative users?</p>
<p>Once again, we could have chosen to store this list within our application’s realm — either as a flat file or a database table — but that would then require providing the administrators of this list a user interface to manage it. Building this interface and training users on it would require time which, again, was an expensive commodity at that late point in our fellowship.</p>
<p>So instead we chose to store this list as a Google Spreadsheet. This had the obvious benefit of saving us implementation time on the front-end but it also provided administrators with a familiar, Microsoft Excel-like user interface which meant little to no training time. Of course, this meant an integration on the back-end of our application which did take some time and effort. Overall, however, I think we came out net positive and made the right choice.</p>
<p><img alt="" height="280px;" src="https://lh6.googleusercontent.com/FIJ-yV0LxvCxGiVVyyjIiVvEJcXYKNlzAZ0vKkJ1qCfjS39ItaZkmHqLlA__7WlZV654K6bVlr-_YSEWrCaqiD8Edcti9M0LAbGbomye0OBUB7jfOv8Mahie" width="624px;"/></p>
<h2 dir="ltr"></h2>
<h2 dir="ltr">How does it all work?</h2>
<p>When users visit the Dashboard, they are requested to sign-in. When they click the sign-in link, they are taken through the Persona sign-in flow. First-time users — or users with email providers that do not take advantage of Persona’s nifty <a href="http://identity.mozilla.com/post/56526022621/what-is-an-identity-bridge" target="_blank">Identity Bridging</a> feature — are requested to sign up.</p>
<p dir="ltr">Once a user successfully signs in, Persona redirects the user to the Dashboard website with a short-lived assertion token. The Dashboard web <em>server</em> sends this assertion token back to Persona for verification. This makes sure the assertion token was not tampered with on the client side.</p>
<p dir="ltr">Once Persona verifies the assertion token, a session is created on the Dashboard web server for the user to indicate that she is signed in to the Dashboard. Since HTTP is a stateless protocol, this session state is maintained across multiple HTTP requests via a cookie containing the session ID.</p>
<p dir="ltr">When the assertion token is verified by Persona, it responds with the user’s email address. The Dashboard web server uses the <a href="https://developers.google.com/drive/v2/reference/" target="_blank">Google Drive API</a> to securely retrieve the authorization list from the Google Spreadsheet set up by administrators and checks if the just-signed-in user’s email address exists in this authorization list. If it does not, the user is not authorized for access and an instructive error message is shown to her. If it does and the user has sufficient rights to view the Dashboard (stored alongside the user’s email address in the spreadsheet), the user is shown the Dashboard.</p>
<p dir="ltr">Users with <em>administrative</em> rights are shown additional links to edit the spreadsheet containing the list of authorized users. This spreadsheet is only shared with certain administrative users so even a malicious user who gets a hold of the link to the spreadsheet would not be able to access it.</p>
<h2 dir="ltr"><img alt="" height="592px;" src="https://lh5.googleusercontent.com/xtuf4L3PLrbDMayG2V-QvmhOUDI4z49pp4YtxM_04uUTA8YZ1jRbknf_28D5Frk6R_Q2oxdcXu0sqDr2fqipx40kXP7n4QFJdyFvQJgCWTG7RZe_WoLy-NoS" width="624px;"/></h2>
<h2 dir="ltr"></h2>
<h2 dir="ltr">Code references</h2>
<ul>
<li dir="ltr">
<p dir="ltr">The back-end API code attempting to authorize the signed-in user’s email address: <a href="https://github.com/codeforamerica/in-n-out/blob/master/public/api/v1/user.php#L87" target="_blank">https://github.com/codeforamerica/in-n-out/blob/master/public/api/v1/user.php#L87</a></p>
</li>
<li dir="ltr">
<p dir="ltr">The Authorization class with the ID of the Google Spreadsheet: <a href="https://github.com/codeforamerica/in-n-out/blob/master/include/authorization.class.php#L8" target="_blank">https://github.com/codeforamerica/in-n-out/blob/master/include/authorization.class.php#L8</a></p>
</li>
<li dir="ltr">
<p dir="ltr">Using the Google Drive API to fetch the Google Spreadsheet: <a href="https://github.com/codeforamerica/in-n-out/blob/master/include/gdrive_spreadsheet_proxy.class.php#L26-L32" target="_blank">https://github.com/codeforamerica/in-n-out/blob/master/include/gdrive_spreadsheet_proxy.class.php#L26-L32</a></p>
</li>
</ul>
<p> </p>
<hr/>
<p> </p>
<p>Questions? Comments? Hit us up <a href="http://twitter.com/codeforamerica" target="_blank">@codeforamerica</a>.</p>
