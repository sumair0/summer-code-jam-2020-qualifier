"""
Use this file to write your solution for the Summer Code Jam 2020 Qualifier.

Important notes for submission:

- Do not change the names of the two classes included below. The test suite we
  will use to test your submission relies on existence these two classes.

- You can leave the `ArticleField` class as-is if you do not wish to tackle the
  advanced requirements.

- Do not include "debug"-code in your submission. This means that you should
  remove all debug prints and other debug statements before you submit your
  solution.
"""
import datetime
import typing
import re


class ArticleField:
    """The `ArticleField` class for the Advanced Requirements."""

    def __init__(self, field_type: typing.Type[typing.Any]):
        pass


class Article:
    """The `Article` class you need to write for the qualifier."""


    def __init__(self, title: str, author: str, publication_date: datetime.datetime, content: str):
        self.title = title 
        self.author = author
        self.publication_date =publication_date
        self.content = content

    def __repr__(self):
        return '<Article title=' + repr(self.title) + ' author=' + repr(self.author) + ' publication_date=' + repr(self.publication_date.isoformat()) + '>'


    def __len__(self):
        return len(self.content)



    def short_introduction(self, n_characters):

        last_breakpoint_index = 0

        for index in range(n_characters):
          if self.content[index] == ' ' or self.content[index] == '\n' :
            last_breakpoint_index = index
            # print(last_breakpoint_index)

        return self.content[0:last_breakpoint_index] 

    def most_common_words(self, n_words):

        alphanumeric_string = re.sub(r'[^a-zA-Z ]', ' ' , self.content.lower() )

        words_list = alphanumeric_string.split(' ')

        frequency_dict = {}

        for word in words_list:
          if word in frequency_dict.keys():
            frequency_dict[word] += 1
          else:
            frequency_dict[word] = 1
        

        frequency_dict = dict(sorted(frequency_dict.items(), key=lambda x : x[1] , reverse=True))

        temp_dict = {} 

        counter = 0

        for key,value in frequency_dict.items() :
          if( counter < n_words and key != ''):
            temp_dict[key] = value
            counter += 1
        
        return temp_dict

        # return frequency_dict

        

########



# fairytale = Article(
#     title="The emperor's new clothes",
#     author="Hans Christian Andersen",
#     content="'But he has nothing at all on!' at last cried out all the people. The Emperor was vexed, for he knew that the people were right.",
#     publication_date=datetime.datetime(1837, 4, 7, 12, 15, 0),
#   )




# # print(fairytale.title)

# # print(len(fairytale))

# # print(fairytale.short_introduction(60))




# print(fairytale.content + '\n')

# print(fairytale.most_common_words(3))