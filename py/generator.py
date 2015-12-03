# -*- coding: utf-8 -*-
__author__ = 'Steve'
import random
import json
import os

script_dir = os.path.dirname(__file__)
rel_path = "input.json"
abs_file_path = os.path.join(script_dir, rel_path)


def random_out(any_list, prob=0.5):
    return random.choice(any_list) if random.random() < prob else ""


def random_pick(any_list, num=1):
    # Select like 1~3 sentences
    result = []
    new_list = []

    new_list.extend(any_list)
    for i in range(0, random.randint(1, num)):
        chosen = random_out(new_list, 1)
        if chosen != "":
            result.append(chosen)
            new_list.remove(chosen)

    return result


class Pattern:
    def __init__(self):
        with open(abs_file_path, "r") as input_file:
            self.input_json = json.load(input_file, encoding="utf-8")

            self.topics = self.input_json["patterns"].keys()

    def generate(self, pattern_type):
        result = []
        pattern = self.input_json["patterns"][pattern_type]
        greetings = pattern[0]
        firsts = pattern[1]
        seconds = pattern[2]
        ends = pattern[3]
        interjections = pattern[4]
        comma = self.input_json["comma"]
        period = self.input_json["period"]

        result.append(random_out(greetings, 0.5))
        first = random_pick(firsts, 1)
        second = random_pick(seconds, 3)
        main = first + second

        main = [x + random_out(interjections) for x in main]
        result.extend(main)

        result.append(random_out(ends, 0.7))

        result = filter(lambda y: y != "", result)

        return comma.join(result) + random_out(period)

    def generate_all(self, number_of_sentence):
        results = []
        for index, topic in enumerate(self.topics):
            result = {}
            result["topic"]=topic
            # print(str(topic))
            result["sentences"] = []

            for i in range(0, number_of_sentence):
                result["sentences"].append(self.generate(topic))
            results.append(result)
        return results


if __name__ == '__main__':
    p = Pattern()
    result = p.generate_all(5)
    x=json.dumps(result, ensure_ascii=False).encode('utf-8')
    print(x)
