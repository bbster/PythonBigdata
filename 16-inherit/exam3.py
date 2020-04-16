class Article:
    
    def __init__(self):
        self.num = 0
        self.title = 0
        
        
class FileArticle(Article):
    
    def __init__(self):
        self.fileName = 0
        
    def __str__(self):
        return '자료실 [번호= {}, 제목={}, 첨부파일={}'.format(
                self.num, self.title, self.fileName)
    

class QNAArticle(Article):
    
    def __init__(self):
        self.answer = 0
    
    def __str__(self):
        return '질문/답변 [글번호={}, 제목={}, 답변={}'.format(
            self.num, self.title, self.answer)
    
fileArticle = FileArticle()
fileArticle.num = 1
fileArticle.title = '첫번째 자료입니다.'
fileArticle.fileName = 'python.ppt'
print(fileArticle) # fileArticle.__str__()
print('-'*30)

qna = QNAArticle()
qna.num = 1
qna.title = '첫번째 질문입니다.'
qna.answer = '첫번째 답변입니다.'
print(qna)
print('-'*30)
