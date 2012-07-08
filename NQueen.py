# -*- coding: utf-8 -*-
'''
Created on 2012/07/07

@author: ishii0514
'''
import copy

blockSize = 7

class Board:
    def __init__(self,n,initQueens):
        #盤の初期化
        self.board = [[0 for j in range(n)] for i in range(n)]
        #盤のサイズ
        self.size = n
        #空いてる位置の数
        self.ZeroNum = n*n
        #Queenの場所
        self.Queens =[]
        
        for q in initQueens:
            self.setQueen(q[0], q[1])
        
    def setQueen(self,m,n):
        if self.board[m][n] <> 0:
            return False
        self.Queens.append([m,n])
        
        #Queenをn,mにセットする
        #縦
        self.setCol(m,n)
        #横
        self.setRow(m,n)
        #斜め
        self.setCloss(m,n)
        #自分の所
        self.board[m][n] = 9
        
        return True
    
    def setCloss(self,m,n):
        #斜め方向
        i = 0
        for row in self.board:
            if i < m:
                point1 = n+(m-i)
                if point1 < self.size:
                    self.setOne(row, point1)
                point2 = n-(m-i)
                if point2 >=0:
                    self.setOne(row, point2)
            else:
                point1 = n+(i-m)
                if point1 < self.size:
                    self.setOne(row, point1)
                point2 = n-(i-m)
                if point2 >=0:
                    self.setOne(row, point2)
            i += 1
            
    def setCol(self,m,n):
        #縦方向
        for row in self.board:
            self.setOne(row, n)
    def setRow(self,m,n):
        #横方向
        for i in range(self.size):
            self.setOne(self.board[m], i)
            
    def setOne(self,row,n):
        if row[n] == 0:
            row[n] = 1
            self.ZeroNum -= 1
     
    def noPosition(self):
        #他におく場所があるか
        return self.ZeroNum == 0
    def QueenNum(self):
        #Queenの数
        return len(self.Queens)
    
    def getPosNum(self):
        #座標の積を取得する。
        return map(self.calcPosNum, self.Queens)
    
    def calcPosNum(self,pos):
        return [pos[0]+1,pos[1]+1,(pos[0] +1)*(pos[1] +1)]
    
    def getK(self):
        #座標の積の合計
        k=0
        for pos in self.getPosNum():
            k += pos[2]
        return k 
        
        
def searchPosition(b):
    #
    blist = []
    for i in range(b.size):
        for j in range(b.size):
            if b.board[i][j] <> 0:
                continue
            #コピー作成
            b2 = copy.deepcopy(b)
            b2.setQueen(i,j)
            if b2.noPosition() == False:
                blist = blist + searchPosition(b2)
            else:
                blist.append(b2)
                            
    return blist

def Maxboard(blist):
    #最大数と、最大の盤を選択
    maxQ =0
    maxB =[]
    for b in blist:
        if b.QueenNum() > maxQ:
            maxQ = b.QueenNum()
    for b in blist:
        if b.QueenNum() == maxQ:
            maxB.append(b)
    return maxB
    
    
if __name__ == '__main__':
    b = Board(blockSize,[[2,2],[4,3]])
    blist = searchPosition(b)
    
    b = Maxboard(blist)[0]
    print '0th'
    for row in b.board:
        print row

    print b.getK()
    for pos in b.getPosNum():
        print pos

"""
答え
2  h
6  e
9  a     
12 l
20 t
28 h
35 y

healthy-112
"""