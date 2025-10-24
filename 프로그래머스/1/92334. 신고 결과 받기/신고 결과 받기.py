def solution(id_list, report, k):
    n = len(id_list)
    receivedReportInfo = {name:[] for name in id_list}
    
    for reportInfo in set(report):
        sender, receiver = reportInfo.split(" ")
        receivedReportInfo[receiver].append(sender)
    
    sendEmailInfo = {name:0 for name in id_list}
    for receiver, senders in receivedReportInfo.items():
        reportCount = len(senders)
        
        if reportCount>=k:
            for sender in senders:
                sendEmailInfo[sender] += 1
    
    answer = []
    for count in sendEmailInfo.values():
        answer.append(count)

    return answer