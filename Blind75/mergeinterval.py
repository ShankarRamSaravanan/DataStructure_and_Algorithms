def mergeInterval(intervals):

    intervals.sort(key=lambda i: i[0])

    output = [intervals[0]]

    print(output)

    for start, end in intervals[1:]:
        lastEnd = output[-1][1]

        if start <= lastEnd:
            output[-1][1] = max(lastEnd, end)

        else:
            output.append([start, end])

    return output


intervals = [[1, 3], [8, 10], [15, 18], [0, 6]]
print(mergeInterval(intervals))
