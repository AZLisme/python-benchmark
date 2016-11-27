# -*- encoding: utf-8 -*-
"""

@author: AZLisme <helloazl@icloud.com>
@time: 2016/11/27 上午10:21
"""

import timeit


def simple_load(json):
    simple = '{"hello": "world", "count": 2}'
    json.loads(simple)


def complex_load(json):
    complex = """[{"id": "0001","type": "donut","name": "Cake","ppu": 0.55,"batters":{"batter":[{ "id": "1001", "type": "Regular" },{ "id": "1002", "type": "Chocolate" },{ "id": "1003", "type": "Blueberry" },{ "id": "1004", "type": "Devil's Food" }]},"topping":[{ "id": "5001", "type": "None" },{ "id": "5002", "type": "Glazed" },{ "id": "5005", "type": "Sugar" },{ "id": "5007", "type": "Powdered Sugar" },{ "id": "5006", "type": "Chocolate with Sprinkles" },{ "id": "5003", "type": "Chocolate" },{ "id": "5004", "type": "Maple" }]},{"id": "0002","type": "donut","name": "Raised","ppu": 0.55,"batters":{"batter":[{ "id": "1001", "type": "Regular" }]},"topping":[{ "id": "5001", "type": "None" },{ "id": "5002", "type": "Glazed" },{ "id": "5005", "type": "Sugar" },{ "id": "5003", "type": "Chocolate" },{ "id": "5004", "type": "Maple" }]},{"id": "0003","type": "donut","name": "Old Fashioned","ppu": 0.55,"batters":{"batter":[{ "id": "1001", "type": "Regular" },{ "id": "1002", "type": "Chocolate" }]},"topping":[{ "id": "5001", "type": "None" },{ "id": "5002", "type": "Glazed" },{ "id": "5003", "type": "Chocolate" },{ "id": "5004", "type": "Maple" }]},{"id": "0004","type": "donut","name": "New Fashioned","ppu": 0.56,"batters":{"batter":[{ "id": "1001", "type": "Regular" },{ "id": "1002", "type": "Chocolate" }]},"topping":[{ "id": "5001", "type": "None" },{ "id": "5002", "type": "Glazed" },{ "id": "5003", "type": "Chocolate" },{ "id": "5004", "type": "Maple" }]}]"""
    json.loads(complex)


def simple_dump(json):
    simple = {"hello": "world", "count": 2}
    json.dumps(simple)


def complex_dump(json):
    complex = [{"id": "0001","type": "donut","name": "Cake","ppu": 0.55,"batters":{"batter":[{ "id": "1001", "type": "Regular" },{ "id": "1002", "type": "Chocolate" },{ "id": "1003", "type": "Blueberry" },{ "id": "1004", "type": "Devil's Food" }]},"topping":[{ "id": "5001", "type": "None" },{ "id": "5002", "type": "Glazed" },{ "id": "5005", "type": "Sugar" },{ "id": "5007", "type": "Powdered Sugar" },{ "id": "5006", "type": "Chocolate with Sprinkles" },{ "id": "5003", "type": "Chocolate" },{ "id": "5004", "type": "Maple" }]},{"id": "0002","type": "donut","name": "Raised","ppu": 0.55,"batters":{"batter":[{ "id": "1001", "type": "Regular" }]},"topping":[{ "id": "5001", "type": "None" },{ "id": "5002", "type": "Glazed" },{ "id": "5005", "type": "Sugar" },{ "id": "5003", "type": "Chocolate" },{ "id": "5004", "type": "Maple" }]},{"id": "0003","type": "donut","name": "Old Fashioned","ppu": 0.55,"batters":{"batter":[{ "id": "1001", "type": "Regular" },{ "id": "1002", "type": "Chocolate" }]},"topping":[{ "id": "5001", "type": "None" },{ "id": "5002", "type": "Glazed" },{ "id": "5003", "type": "Chocolate" },{ "id": "5004", "type": "Maple" }]},{"id": "0004","type": "donut","name": "New Fashioned","ppu": 0.56,"batters":{"batter":[{ "id": "1001", "type": "Regular" },{ "id": "1002", "type": "Chocolate" }]},"topping":[{ "id": "5001", "type": "None" },{ "id": "5002", "type": "Glazed" },{ "id": "5003", "type": "Chocolate" },{ "id": "5004", "type": "Maple" }]}]
    json.dumps(complex)


def benchmark():
    json_order = ('json', 'simplejson', 'flask.json')
    test_order = ('simple_load', 'complex_load', 'simple_dump', 'complex_dump')
    print("%10s\t%10s\t%10s\t%10s\t%10s\t" % ("", *test_order))
    for json in json_order:
        print('%10s' % json, end='\t')
        for test in test_order:
            timer = timeit.Timer('{}({})'.format(test, json), "from __main__ import %s; import %s" % (test, json))
            print("%.10fs" % timer.timeit(100000), end='\t')
        print("")


if __name__ == "__main__":
    benchmark()
