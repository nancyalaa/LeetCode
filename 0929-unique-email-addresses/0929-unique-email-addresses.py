class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        output = []
        for email in emails:
            domainIdx = email.index('@')
            temp = email[:domainIdx]
            if '+' in temp:
                plusIdx = temp.index('+')
                temp = temp[:plusIdx]
            temp = temp.replace('.','')
            tempMail = temp + email[domainIdx:]
            if tempMail not in output:
                output.append(tempMail)
        return len(output)
            
        