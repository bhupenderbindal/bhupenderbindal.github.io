---
layout: post
title: My first Advent of code problem
date: 2024-02-10 # 10:14:00-0400
description: experience of solving advent of code problem
categories: programming logic
giscus_comments: true
related_posts: false
toc:
  sidebar: center
---
This post is about my first take at Advent of Code in the winter of 2023. I came to know about this through some people talking about it. So I thought to give it a try. I started with the "[Day 13: Point of incidence](https://adventofcode.com/2023/day/13)" problem as coincidentally 13th, which is considered an unlucky number. 

[//]: add more sections: writing it with c++ later sometime rust

## Problem definition
{:data-toc-text="Problem definition"}

The AOC develops the whole set of problems in a story-based fashion which is great. However, as I was starting late in the story, I didn't understand much of it but still the individual problem can be understood owing to a nice explanation with the example, which is better than great, i.e., wonderful. Have a look at the [problem page](https://adventofcode.com/2023/day/13).

I will keep it simple here with the problem definition. The problem gives us an input in the form of a pattern consisting of "#" and "." and we need to return a positive integer as the result after solving. 

The example patterns are as below:

```
#.##..##.
..#.##.#.
##......#
##......#
..#.##.#.
..##..##.
#.#.##.#.

#...##..#
#....#..#
..##..###
#####.##.
#####.##.
..##..###
#....#..#
```
The LOR for both the patterns are shown below:

1. Here the line of refelection is between columns 5 and 6. Column one is not involved in the reflection as 9 is an odd number of columns, here column 1 is the extra and ignored.
```
123456789
       ><   
#.##..##.
..#.##.#.
##......#
##......#
..#.##.#.
..##..##.
#.#.##.#.
       ><
123456789
```
2. Here the LOR is between rows 4 and 5. Here row 1 is not involved in the reflection. 
```
1 #...##..# 1
2 #....#..# 2
3 ..##..### 3
4v#####.##.v4
5^#####.##.^5
6 ..##..### 6
7 #....#..# 7
```
```
RESULT = (Total number of columns to the left of each vertical LOR) 
         + 100 * (Total number of rows above horizontal LOR)
```
Result for the example = 5 + 100 * (4) = 405

Now the actual problem input is more than 1000 lines consisting of many such individual patterns and we need to calculate the output for this long input.

## My first solution

I noted that if a logic works horizontal patterns to find the LOR, then the same logic can be used on the transposed version of the patterns which will work as if it finds the vertical LOR. 

Now to use this logic I needed two versions of the input, one as it is and the other containing the transposed version of the patterns. Only the summation formula will be different for the two versions and the result will be the sum of the two summations.

As I need a transposed version of each pattern, I need a simple transpose operation which is available in numpy arrays. The numpy array supports different data types of the array elements. So I can directly create the array of the characters and avoid converting the input pattern into an array of 0s and 1s.



After this logic setup, comes the execution. 
First, we want to read the file and create the two versions of the input.
For that, we define a function as below:

```python

def create_patterns_arr():
    hor_patterns = []
    ver_patterns = []
    with open("./input.txt", mode="r") as f:
        # a is an temp array for each pattern
        a = []
        for line in f.readlines():
            if line == "\n":
                hor_patterns.append(np.array(a))
                ver_patterns.append(np.transpose(np.array(a)))
                a = []
            else:
                a.append(list(line[:-1]))

        hor_patterns.append(np.array(a))
        ver_patterns.append(np.transpose(np.array(a)))
    return hor_patterns, ver_patterns
```

Now we have a list of patterns (as a numpy array), we want to find the LOR. First I thought about checking whether a pattern has odd or even lines and then trying to find the LOR. However, as per the example, a row(s) can have no reflection depending on where the LOR occurs. 

Hence it's better to iterate over all the rows and find the possible LOR where a row and its next row are equal. Then check whether this line occurs before the middle of the pattern or after the middle of the pattern based on which we will consider only the reflected rows and reject the extra rows from the top or the bottom. Now we check whether two equal parts up and below the LOR are equal and if yes then add the amount as per the formula otherwise move to the next row.

First the simpler part of checking whether the two parts obtained are equal or not. Here, I simply wrote a function using numpy API.
```python
def are_nparr_mirror(a, b):
    b = b[::-1]
    if np.array_equal(a, b):
        return True
    else:
        return False
```

Then write the code for finding LOR in the horizontal LOR: 
```python
hor_patterns, ver_patterns = create_patterns_arr()
res = 0

for pattern in hor_patterns:

    for i in range(pattern.shape[0] - 1):
        if np.array_equal(pattern[i], pattern[i + 1]):
            if i >= int(len(pattern) / 2):
                common_len = len(pattern) - 1 - i

                if are_nparr_mirror(
                    pattern[i + 1 - common_len : i + 1], pattern[i + 1 :]
                ):
                    res += 100 * (i + 1)
            else:
                common_len = i + 1

                if are_nparr_mirror(
                    pattern[:common_len], pattern[common_len : common_len * 2]
                ):
                    res += 100 * (i + 1)
```

I checked this on the example pattern with horizontal LOR and iterated until I got the slicing logic correct. And then the same logic just with a changed summation formula for the vertical patterns as I already have the transposed version of them.
```python
for pattern in ver_patterns:
    for i in range(pattern.shape[0] - 1):
        if np.array_equal(pattern[i], pattern[i + 1]):
            if i >= int(len(pattern) / 2):
                common_len = len(pattern) - 1 - i

                if are_nparr_mirror(
                    pattern[i + 1 - common_len : i + 1], pattern[i + 1 :]
                ):
                    res += i + 1
            else:
                common_len = i + 1

                if are_nparr_mirror(
                    pattern[:common_len], pattern[common_len : common_len * 2]
                ):
                    res += i + 1
```

This gives the first solution, not very elegant, but works after 5 hours of fiddling with the problem. 

## Second part of the problem

While writing this blog, I realized that in December I only solved the first part of the problem. So I thought of solving the second part now, to save my pride.
Solving the second part was not easy either, and trying to solve it the first time looked at other solutions in the Reddit thread of the problem to find "Have I made the problem even more complex than it is ?; There must be another efficient way for the logic". So I found out that my first logic of transposing and using the same logic for vertical LOR is correct, but could be written without repeating code, duh yeah! The more interesting was the second logic to find the LOR, instead of using a common length or repeated pattern, at every index a simpler minimum function between the index and the remaining length can be used. Moreover, rather than checking the equality of two sides of LOR, a difference between the two sides can be checked to be 0 for the first part and 1 for the second part (numpy has a function for character difference too if I avoid using 0 and 1 encoding), which involves minor change between two parts and is logical as the second should built on top of one.  
I could now add my solution for the second part and go over it but more important are the lessons learned.

## Lessons learned
1. Thinking over the logic is more important than straight away writing code unless one has with practice decreased that gap sufficiently. This will avoid **many iterations of execution and expecting a correct answer**. Obviously without writing code the correctness of logic cannot be checked but logic deserves at least some mental work before being written in code form. 
2. Observe the first code and try to simplify the logic and refactor if the code seems too big for the problem.
3. Practice more! or in other words "Übung macht den Meister". Producing an elegant solution takes more practice. 

<!-- 
## Some mistakes which I did and their solution
  - not setting the server name to "0.0.0.0" for the webapplication and hence could not connect to the host port
  [as discussed on stackoverflow question](https://stackoverflow.com/questions/39525820/docker-port-forwarding-not-working)
  - not creating a workdir in the container which can cause problem if your following command has to do with the files in the directory 
  - using docker cp to copy a local file in container then launching the app. But I missed the obvious pitfall of using the docker cp command that it only make temp change to a container which is still missing from the image and wont work when the image is deployed again locally or on cloud -->


