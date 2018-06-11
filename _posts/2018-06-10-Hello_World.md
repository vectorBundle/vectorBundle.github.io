---
layout: post
title: Hello World!
---

## Executive Summary
My motivation for writing a blog is explained, and the choice for using Jekyll
and Github Pages is justified.


## Why Blogging?
I am at the stage of my life where I have little obligations to family, society
etc., yet care deeply about my career development and future prospects.
Reflecting back how I get to where I am, I see I benefited greatly from the
open source community; mainly from the Q&A sites such as [Stack
Exchange](https://stackexchange.com), and then occasionally from various blog
posts that provides more in-depth analysis or explanations.
I think I am at the stage where I have accumulated enough experience in the
field that I am working in, such that I have something interesting to share.
In addition I am a bit disappointed that this open source mentality mostly
exists in programming related fields, and traditional engineering disciplines
haven't adopted similar approaches.
Maybe I could bridge this gap.


My vision of this blog is to share non-sensitive, personal investigations into the
mathematics or programming concepts or challenges that arises from solving real
life engineering problems.
It could be:
<dl>
  <dt>Notes on mathematics learned</dt>
  <dd>As <a href="http://www.rao.im">Dr. Arvind Rao's Blog</a> demonstrates</dd>

  <dt>Annotated bibliography</dt>
  <dd>For example, <a href="https://www.r-bloggers.com/an-introduction-to-change-points-packages-ecp-and-breakoutdetection">this R blog entry</a></dd>

  <dt>Original research</dt>
  <dd>For example, <a href="https://maziarraissi.github.io/MultistepNNs">this paper</a></dd>
</dl>
I do admit that aforementioned works represent high level standard for a blog
entry.
Nonetheless I hope that aiming high would motivate me to continuously learn and
present new things, thus maintain a life-long development.


## Elements of a Technical Blog
Having in mind of writing a technical blog, then the following common elements
of scientific writings are essential:

* Lists
* Tables
* Graphics
* Equations
* Code Listings

Although I would love to also incorporate animations or interactions, for
example [this phase diagram illustration](http://demonstrations.wolfram.com/VaporLiquidLiquidEquilibriumVLLE/),
but that can wait in future upgrades.


Fortunately there are just tools available that allows me to easily write blog
entries with any of those elements included.
In fact, the entire procedure from content writing to publishing on the
internet has been streamlined, such that it doesn't take a front-end developer
to doing blogging.
All of that is thanks to Github Pages and Jekyll.


## Github Pages and Jekyll
I don't consider myself a web designer, so if possible I really don't want to
maintain my own server or design how my website or blog looks.
Being versed in writing in LaTeX, I would rather focus on the content of my
entries and let the software worry about how to display it.
Fortunately what [Jekyll](https://jekyllrb.com/docs/home/) to blog writing is
what LaTeX to math-heavy scientific reports.
It allows the user to write in the Markdown language, and takes care of the
transformation necessary to generate a static HTML file from it.
As a result the content of such webpage is thus separated from the style of the
presentation.


Jekyll handles the Markdown to HTML conversion.
To let the other computers access such HTML and hence my blog entry, I need to
host it somewhere so that the rest of the internet can visit it.
This is where [Github Pages](https://pages.github.com/) come in handy.
Essentially you create a Git repository storing the Markdown files, and Github
will render it to a webpage for you.
For example, the corresponding repository for this blog is at [here](https://github.com/vectorBundle/vectorBundle.github.io).


Finally to point out the obvious: Your local copy of Jekyll is to testing your
contents locally before pushing to Github.
Although there is nothing stopping you from pushing to Github as a way to
testing your contents, but that's against best software engineering practices.


## Getting Started
I didn't figure this out all by myself.
In this section I would like to document some of the blog entries that helped
me started using Github Pages and Jekyll.


A really good starting point would be [this blog entry](http://joshualande.com/jekyll-github-pages-poole).
It touches on the basic elements plus essential customizations.
However written in 2014 I found it no longer compatible with the latest
version of Jekyll especially in setting up the `_config.yml` file.
For me I referenced more actively maintained Jekyll + Github Pages blogs, for
example [this set up](https://github.com/MrDupin/mrdupin.github.io/blob/master/_config.yml).


And thus this blog was born.
