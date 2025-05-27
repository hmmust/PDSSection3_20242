import requests
import pandas as pd
from pyquery import PyQuery as pq

kooora = requests.get(
    url="https://www.kooora.com/%D9%83%D8%B1%D8%A9-%D8%A7%D9%84%D9%82%D8%AF%D9%85/%D9%85%D9%88%D8%A7%D8%B9%D9%8A%D8%AF-%D9%86%D8%AA%D8%A7%D8%A6%D8%AC/2025-05-26")

kooora_doc = pq(kooora.text)
matches =  kooora_doc("div.fco-match-row")  
match_today= []
for match in matches:
    match= pq(pq(match)("div.fco-match-team-and-score"))
    team_a = pq(match("div.fco-match-team-and-score__team-a"))
    team_a = pq(team_a("div.fco-match-team-with-crest"))
    team_a = pq(team_a("div.fco-long-name"))
    team_a = team_a.text()
    team_b = pq(match("div.fco-match-team-and-score__team-b"))
    team_b = pq(team_b("div.fco-match-team-with-crest"))
    team_b = pq(team_b("div.fco-long-name"))
    team_b = team_b.text()
    scores = pq(match("div.fco-match-score__container"))
    scores = pq(match("div.fco-match-score"))
    score_a= pq(scores[0]).text()
    score_b = pq(scores[1]).text()
    match_today.append({'team_a':team_a,
                        'score_a':score_a,
                        "team_b":team_b,
                        "score_b":score_b})

    #print(team_a,score_a," --- ",score_b,team_b)

match_today_df = pd.DataFrame(match_today)
print(match_today_df)