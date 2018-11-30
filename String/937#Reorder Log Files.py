# https://leetcode.com/problems/reorder-log-files/description/
class Solution:
    def reorderLogFiles(self, logs):
        """
        :type logs: List[str]
        :rtype: List[str]
        """
        digit_logs = []
        letter_logs = []
        for log in logs:
            if log[-1].isdigit():
                digit_logs.append(log)
            else:
                letter_logs.append(log)
        letter_logs.sort(key=lambda a:a.split()[1:])
        return letter_logs+digit_logs

    def reorderLogFiles(self, logs):
        l = filter(lambda l: l[l.find(" ") + 1].isalpha(), logs)
        d = filter(lambda l: l[l.find(" ") + 1].isdigit(), logs)
        return sorted(l, key = lambda x: (x[x.find(" "):], x[:x.find(" ")])) + list(d)
                