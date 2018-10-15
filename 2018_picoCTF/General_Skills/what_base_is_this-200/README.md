## what base is this? - 200

### Description

> To be successful on your mission, you must be able read data represented in different ways, such as hexadecimal or binary. Can you get the flag from this program to prove you are ready? Connect with nc 2018shell1.picoctf.com 15853.

### Write up

It's a simple base conversion problem.

```
$ nc 2018shell1.picoctf.com 15853
We are going to start at the very beginning and make sure you understand how data is stored.
doctor
Please give me the 01100100 01101111 01100011 01110100 01101111 01110010 as a word.
To make things interesting, you have 30 seconds.
Input:
doctor
Please give me the 73746f7665 as a word.
Input:
stove
Please give me the  144 157 143 164 157 162 as a word.
Input:
doctor
You got it! You're super quick!
Flag: picoCTF{delusions_about_finding_values_3cc386de}
```
