# -*- coding: utf-8 -*-

import shutil
import os
import pdb
import random
import string
import codecs
import re


ocString = re.compile(r'@"[^"]+"')


def getResourcePath(targetpath):
    # print("=====================Find all Files=========================")
    filelist = []
    # pdb.set_trace()
    os.listdir(targetpath)
    for fileName in os.listdir(targetpath):
        filePath = targetpath + '/' + fileName
        # print(filePath)
        if os.path.isdir(filePath):
            # renameDir(filePath)
            files = getResourcePath(filePath)
            filelist.extend(files)
        else:
            if "DS_Store" not in filePath:
                filelist.append(filePath)
                           
    return filelist


def main():
    print("this main run")
    dir = os.getcwd() + "/Demo"
    files = getResourcePath(dir)
    sourceArr = getSoureHeadHM(files)
    ergodicM(sourceArr)



def getSoureHeadHM(files):#过滤 遍历获取.h.m所有文件。  第一层元祖(.h .m)第二层:所有的元祖集合
    sourceArr = []
    for fileName in files:#遍历所有文件
        if not ".h" in fileName:#不是.h的文件continue
            # print("fileName is not .h" + fileName)
            continue

        if "Pods" in fileName: #is cocoapod
            # print("fileName is pods" + fileName)
            continue

        fileNameText = os.path.splitext(fileName)
        # print("fileNameText:" + fileNameText[0]);
        fileNameM = fileNameText[0] + ".m"
        if fileNameM in files:#.h.m同一个文件目录下情况,正常情况要遍历整个项目找到.m
            tupe = (fileName,fileNameM)
            sourceArr.append(tupe)
            continue
        else:
            print(".h .m不是同一文件夹暂不处理:" + fileNameM);
    # print("sourceArr:" + str(sourceArr))
    return sourceArr


def ergodicM(sourceArr):#遍历.M的所有方法替换成
    for tupes in sourceArr:
        filePathH = tupes[0]
        filePathM = tupes[-1]
        sourceM = ""
        with codecs.open(filePathM, 'r', 'utf-8') as f:
            try:
                sourceM = f.read() 
                f.close()
            except :
                print("fileMMMname:" + filePathM)
                continue
     
        patternMArr = re.findall(ocString,sourceM)
        # print("strArr:" + str(patternMArr))
        patternOtherMArr = []
        for ocstr in patternMArr:
            patternStr = ""
            print("ocstr:" + ocstr)
            for i,ch in enumerate(ocstr):
                print("ch:" + ch)
                if i == 0 or i == 1 or i == len(ocstr) - 1:
                    patternStr += ch
                    continue
                if ch == '\\':
                    patternStr = patternStr + randomStr() + '*'
                    continue
                patternStr = patternStr + randomStr() + ch
            patternStr = "[TTStrUnConfusion getOtherStr:" + patternStr + "]"
            print("patternStr:" + patternStr)
            sourceM = sourceM.replace(ocstr,patternStr)
            # print("sourceM" + sourceM)

        with codecs.open(filePathM, 'w', 'utf-8') as t:
            try:
                t.write(sourceM)
                t.close() 
            except :
                print("fileHHHname:" + filePathH)
                continue

      
        		# print("x:" + x)


        # print("pattern:" + str(patternMArr))
    

def randomStr():#随机1位的字符串
	salt = ''.join(random.sample(string.ascii_letters + string.digits, 1))
	return salt




if __name__ == "__main__":
	main()

