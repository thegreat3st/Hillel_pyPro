import string
import re

story_title = 'THE BOY WHO LIVED'
story = "Mr. and Mrs. Dursley, of number four, Privet Drive, were \
        proud to say that they were perfectly normal, thank \
        you very much. They were the last people you’d expect to be involved in anything strange or mysterious, because they just didn’t \
        hold with such nonsense. \
        Mr. Dursley was the director of a fi rm called Grunnings, which \
        made drills. He was a big, beefy man with hardly any neck, although he did have a very large mustache. Mrs. Dursley was thin \
        and blonde and had nearly twice the usual amount of neck, which \
        came in very useful as she spent so much of her time craning over \
        garden fences, spying on the neighbors. The Dursleys had a small \
        son called Dudley and in their opinion there was no finer boy \
        anywhere."
story = ' '.join(story.split())
punc = string.punctuation
story_no_func = story
for ele in story:
    if ele in punc:
        story_no_func = story.replace(ele, "")
        #print(story_no_func)    
#story_list = [story]
#print(story_list)

story_words = story.split()
#print(story_words)
#print(type(story_words))

story_list = story.split(".")
print(story_list)

story_words_num = len(story_words)
print(story_words_num)

story_list_num = len(story_list)
print(story_list_num)

story_list.insert(0, story_title) 
full_text_list = story_list
print(full_text_list)

story_list.pop(0)
without_upper = story_list
print(without_upper)

