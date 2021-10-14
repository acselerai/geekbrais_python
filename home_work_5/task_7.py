from json import dump

FIRM_INDEX = 0
PROFIT_INDEX = 2
EXPENCE_INDEX = 3


def process_firm_info(line):
    firm_attrs = line.split()
    return [
        firm_attrs[FIRM_INDEX],
        int(firm_attrs[PROFIT_INDEX]) - int(firm_attrs[EXPENCE_INDEX])
    ]


with open('task_7.txt', 'r') as file:
    firms_profit = dict(
        map(
            process_firm_info,
            file
        )
    )

average_profit = sum(
    [profit for profit in firms_profit.values() if profit > 0]
)

result = [
    firms_profit,
    {
        'average_profit': average_profit
    }
]

with open('task_7.json', 'w') as json_file:
    dump(result, json_file)
