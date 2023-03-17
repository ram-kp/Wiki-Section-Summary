import os
import json
import requests
import argparse
import openai
from bs4 import BeautifulSoup

if __name__ == "__main__":
    openai.api_key = os.environ["OPEN_AI_KEY"]
    parser = argparse.ArgumentParser()
    parser.add_argument('--link', type=str, required=True, help='Enter website link to scrap')
    parser.add_argument('--keywords', type=str, required=True, help='Enter keyword to search')
    parser.add_argument('--out', type=str, required=False, help='Enter name of output json file')
    args = parser.parse_args()
    link = args.link
    title = args.keywords
    jsonFile = args.out

    html_text = requests.get(f'{link}').text
    soup = BeautifulSoup(html_text, 'lxml')
    start = soup.find('h2', string=title)
    start = start.next_sibling
    biodiversity = ""
    while start.name != 'h2':
        if start.name == 'p':
            biodiversity += start.text

        start = start.next_sibling

    # print(biodiversity)
    prompt = f""" Summarize this text in brief: {biodiversity}"""

    # response = openai.Completion.create(
    #     model="text-davinci-003",
    #     prompt=prompt,
    #     temperature=0.6,
    #     max_tokens=1000
    # )

    response = openai.ChatCompletion.create(
      model="gpt-3.5-turbo",
      messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": f'{prompt}'},
        ]
    )
    # print(response.choices[0].message.content)
    summarizedText = response.choices[0].message.content

    data = [{
        "link": f"{link}",
        "title": f"{title}",
        "Description": summarizedText
    }]
    with open(jsonFile, 'w') as f:
        json.dump(data, f, indent=4)












