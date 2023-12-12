This repository is an LLM-annotation course project.

ChatGPT 3.5 and/or Grok will be tasked with annotating parts of a short joke dataset. 
The LLM will be responsible for annotating the introduction and punchline of each joke 
and also explaining why the given joke is supposed to be funny/amusing.

While going through the dataset I noticed that some of the jokes tend to be somewhat 
politically incorrect and/or triggering, I also thought about annotating the political 
correctness of each joke and the subjective funniness of the joke on a scale according 
to the LLM. By doing this, I hope to gather more insight into the 'personality' and 
'political orientation' of both LLMs.

I want to create a smaller subset of the complete dataset and then 0-shot prompt the 
LLMs to annotate the subset as explained earlier. Afterward, I will manually check if 
the LLM 'got' the joke and annotated it correctly. Additionally, I want to check the funniness- 
and PC-score and see if there is some correlation between the two scores for each LLM. 
(My thesis would be that there is a correlation between the two scores, i.e. that ChatGPT 
would find politically incorrect jokes less funny and that Grok, given its edgy reputation, 
would find politically incorrect jokes more funny or at least as funny as 'normal jokes').
