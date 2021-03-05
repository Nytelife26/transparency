# The Java-Docker Problem

The issue I encountered with Java on Docker was that it raised our image size to
around 380 MB. What did this image do, you ask? It simply needed to run a
Lavalink server. I think we can all agree that should not need a 380 MB image.

Lightweight is my philosophy, so I set out to reduce the image size, with a
target of ~80 MB, and specifically using OpenJDK 13 (as recommended by
Lavalink).

## Making the Plan of Attack

The Java build size is largely down to the system it is built on. This is why
Alpine versions of most Docker images exist - it is largely considered to be a
very lightweight distribution, resulting in much slimmer images than our good
friend Ubuntu.

However, clearly, the Alpine images weren't slim enough to tame Java.

With that, I went off to find the actual source size of the JDK, to see roughly
how much it got inflated in the build process. 182 MB - not promising.

I found Photon OS; a featherweight distribution, weighing in at 15 MB for the
base install. Beautiful. Now, I can move on to figuring out how to get them to
work together.

## Execution

I initially wrote a Dockerfile to install and build the JDK on Photon OS. It
ended up producing image sizes of around 100 MB - good, but not on target.

I concluded that using standard procedures it would be nigh on impossible to do.
That was, until I discovered AdoptOpenJDK's custom images.

AdoptOpenJDK build their own Java images using a modified source. In doing so,
they produce images at ~60MB or less in size typically.

# Conclusion

[AdoptOpenJDK] have currently the smallest Java images, and the best solutions
for my problem. My homebrew endeavours failed, however, there is already a
better solution in place, and thus that is what I recommend.

Thank you for following in this journey with me. I hope my conclusions prove
useful to anyone enduring the same problem.

[AdoptOpenJDK]: https://hub.docker.com/u/adoptopenjdk
