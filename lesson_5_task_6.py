subj = {}
with open('task_6_lectures.txt', encoding='utf-8') as task_6:
    for line in task_6:
        key, value = line.split(':')
        subj[key] = value

result = {}
for key in subj.keys():
    summary = 0
    subj[key] = subj[key].split()

    for i in range(0, len(subj[key])):

        if i % 2 == 0:

            summary = summary + int(subj[key][i].replace('—', '0'))
    result[key] = summary
print(result)
