class Solution:
    def calPoints(self, operations: List[str]) -> int:
        record = []

        for ops in operations:
            if len(record)>=2 and ops == "+":
                record.append(record[-1]+record[-2])
            elif len(record)>=1 and ops == "D":
                record.append(2*record[-1])
            elif len(record)>=1 and ops == "C":
                record.pop()
            else:
                record.append(int(ops))
        return sum(record)