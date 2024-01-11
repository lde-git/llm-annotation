This repository is an LLM-annotation course project.

datasets [  
    jester_items.csv //150 joke Dataset
    jester_ratings.csv //Over 1.7 million continuous ratings (-10.00 to +10.00) of 150 jokes from 59,132 users.  

    modified_jester_ratings.csv //Uses jokeID as primary key to see how many users voted on a given joke.
    avg_jester_rating.csv //Average rating for each joke

    shortjokes.csv //Different dataset with way more jokes used for further testing   
]

modelOutputs [
    GPT_punchline_annotation.csv //[jokeID, punchline, explanation, rating] 0-shot prompted 
    GPT_neutral_fr_pcr.csv // [jokeID, $fr, $pcr, $reasoning] few shot prompted 
    GPT_affiliative_fr_pcr.csv // [jokeID, $fr, $pcr, $reasoning] 0-shot prompted with affiliative humor injection
    GPT_aggressive_fr_pcr.csv // [jokeID, $fr, $pcr, $reasoning] 0-shot prompted with aggressive humor injection
    GPT_selfDefeating_fr_pcr.csv // [jokeID, $fr, $pcr, $reasoning] 0-shot prompted self defeating humor injection
    GPT_selfEnhancing_fr_pcr.csv // [jokeID, $fr, $pcr, $reasoning] 0-shot prompted self enhancing humor injection
]


ChatGPT 3.5 will be tasked with annotating parts of a short joke dataset. 
The LLM will be responsible for annotating the introduction and punchline of each joke 
and also explaining why the given joke is supposed to be funny/amusing.

After this initial testing it will be asked to evaluate the quality of the jokes (funniness rating ($fr) and
political correctness rating ($pcr)). 

For this different personalities will be induced (neutral, affiliative, aggressive, selfDefeating, selfEnhancing)
based on the four different types of humor: In particular, for the classification of jokes there are
four types of humour: affiliative, self-enhancing, aggressive and self-defeating  Affiliative humor is a non-hostile,
tolerant use of humor that is affirming of self and others. Self-enhancing humor is used to make people feel good about
themselves. Aggressive humor is the use of sarcasm, teasing, ridicule, derision, and put-downs. Finally, self-defeating
humor involves poking fun at oneself for the enjoyment of others.



While going through the dataset I noticed that some of the jokes tend to be somewhat 
triggering, I also thought about annotating the political correctness of each joke and 
the subjective funniness of the joke on a scale according to the LLM.


