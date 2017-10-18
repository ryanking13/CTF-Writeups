## looooong - 20

### Description

I heard you have some "delusions of grandeur" about your typing speed. How fast can you go at shell2017.picoctf.com:30277?

### Hint

  - Use the nc command to connect!
  - I hear python is a good means (among many) to generate the needed input.
  - It might help to have multiple windows open

### Write up

    $ nc localhost 30277
    To prove your skills, you must pass this test.
    Please give me the 'c' character '713' times, followed by a single '9'.
    To make things interesting, you have 30 seconds.

character and number differs each time you connect.

Using python is easy solution.

```python
  'c'*713 + '9'
```


> with_some_recognition_and_training_delusions_become_glimpses_493092611815c4e8f8eee8df7264c4c0
