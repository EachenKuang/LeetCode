# https://leetcode.com/problems/unique-email-addresses/description/
class Solution:
	# 1 
    def numUniqueEmails1(self, emails):
        """
        :type emails: List[str]
        :rtype: int
        """
        splited_eamils = [email.split('@') for email in emails]
        trans_emails = ['@'.join(email[0].split('+')[0].replace('.','')+email[1]) for email in splited_eamils]
        return len(set(trans_emails))
    # 2 使用set add 更快一些
    def numUniqueEmails2(self, emails):
        local_names = []
        for index, address in enumerate(emails):
            name = address.split('@')
            local_names.append(name[0].replace('.', '').split('+')[0] + '@' + name[1])
        return len(set(local_names))