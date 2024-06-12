---
layout: post
title: My first Advent of code problem :part2 in C++
date: 2024-02-10 # 10:14:00-0400
description: AOC day 13 in C++ and comparison with python
categories: programming logic
giscus_comments: true
related_posts: false
toc:
  sidebar: center
---
**Intended audience: Beginners not masters.**

Now, I will try to refactor the code for the problem and try to code the same logic in C++ and improve my understanding of programming concepts with this execercise. Followed by what I learned in this attempt, which might be useful for someone else reading it.

**NOTE:** This is no sense an attempt to compare the languages.
 <!-- Followed by the comparison between the two in terms of obviously runtime.  -->

[//]: add more sections: writing it with C++ later sometime rust

## Python code refactoring
{:data-toc-text="Python code refactoring"}
Although I had looked at the shortest form of solutions code, I refactored my code myself for two reasons:
1. It will help me understand what parts and logic of my code were redundant or could be better written in the first place. For example, I found that I can write code with less of my favorite "if statement", which is also recommended way. Another example is the "return statement" in combination with "if statement" is a point of play. One can add the return statement with the "if condition" and follow it with a return statement without using the "else condition" if no else logic is required and utilize this point of play as per requirement.
2. The short solutions are certainly good but my current coding style is more verbose than that. Copying the solution won't help in improving. I still need to learn with practice to write logic and flow in a more precise way but with good readability for myself and others. 

## Solving in C++

<!-- After starting to solve in C++, I got the obvious realization that the same logic cannot be followed as data structures used in python with numpy has a very different API than that of data structures in C++. So I tried to adopt my base logic to C++.  -->

I dont want to repeat what are the differences between python and C++, as there are already many blogs and videos over it some bad, some good. Even I have watched a couple of them, but none of them can give me the feeling/understanding that I get by writing some C++ code myself and experience the most obvious differences, which anyone can understand them by hello-world in both the languages, and the more strong differences that hit you when you move from python to c++ code, reinforcing some programming concepts by experiencing how different languages deal with them. *As experienced people say talking about the difference between two languages is unncessary and problem one is trying to solve is more important. Do what is more comfortable to you and more importantly align with the goals of the problem/task one is trying to solve.*

 <!-- Or one is trying to appreciate the beauty of how different languages deal and apply the same concepts improving general understanding. -->

After all this great talk above, i am still a novice and will try to write "thats interesting" that I can see in short time.
First of all, it was a tough job even to code the same logic in C++ due to the obvious lack of knowledge and practice with C++ containers and generic algorithms related to them.
Hence I used for loops at many places iterating element by element and even transposing a vector of strings. Oh boy, that was entertaining and frustrating at the same time.

I thought of attaching my solution in C++ but right now I avoid you the headache of reading it and in addition to that I am still on the journey of being comfortable sharing my not so good code. Hence moving to more important stuff in the next section.


## Lessons learned/ That's interesting
As I start writing this section, I discovered more important questions that I needed to look into. 

- why i even use vectors instead of arrays in c++: with list() and numpy array() one can easily create arrays as required. but in c++ one uses vectors if one does not the size of array beforehand 
- why create new arrays (in the findlor function) instead of using the slice as in python : is this issue of pass by value(copy with extra space) and pass by refernce for functions --> read the book
- concept of view and shallow copy when passing objects in python

1. As c++ requires type of the object that container holds, I have to write "vector<vector<string>> all_patterns;" which on the first sight looks extra work but in other look it promotes to think before about what are you going to store in the container which in turn promotes "think before you write code". This guide of type allows to think what type of contaianer, what it will be storing and what operations can be performed on it. In python, in my experience I create a list and simply keep on appending to it whatever type is required and later during further operations or in case of debugging I can think over the types etc. Again both have their uses.
2. 


<!-- 
## Some mistakes which I did and their solution
  - not setting the server name to "0.0.0.0" for the webapplication and hence could not connect to the host port
  [as discussed on stackoverflow question](https://stackoverflow.com/questions/39525820/docker-port-forwarding-not-working)
  - not creating a workdir in the container which can cause problem if your following command has to do with the files in the directory 
  - using docker cp to copy a local file in container then launching the app. But I missed the obvious pitfall of using the docker cp command that it only make temp change to a container which is still missing from the image and wont work when the image is deployed again locally or on cloud -->


